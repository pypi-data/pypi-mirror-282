# Copyright (C) 2024 Collimator, Inc.
# SPDX-License-Identifier: AGPL-3.0-or-later
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU Affero General Public License as published by the Free
# Software Foundation, version 3. This program is distributed in the hope that it
# will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General
# Public License for more details.  You should have received a copy of the GNU
# Affero General Public License along with this program. If not, see
# <https://www.gnu.org/licenses/>.

from typing import TYPE_CHECKING
from collimator.lazy_loader import LazyLoader
from .base import (
    SymKind,
    EqnKind,
)
from .component_base import ComponentBase

if TYPE_CHECKING:
    import sympy as sp
else:
    sp = LazyLoader("sp", globals(), "sympy")

"""
Discussion on the design of the electrical components relative to Modelica Standard Library (MLS).

MSL Pin.mo defines the I(flow), and V(potential). We do the similar in ElecPort, but the symbols are passed in from
the component, to the port, so we get I1, I2, V1, V2.

MSL TwoPin.mo and OnePort.mo define the component I and V symbols. We do similar, but define V in ElecTwoPin,
and use the I1 from component for I.

In this way, the Resistor and Capacitor end up with essentially an analogous set of symbols, and
an equivalent set of equations relative to the MSL components.

Elecdtrical Domain variables:
flow:Units = current:Amps
potential:Units = voltage:Volts
"""


class ElecTwoPin(ComponentBase):
    """Partial component class for an electrical component with two
    pins, or two electrical terminals.
    """

    def __init__(
        self,
        ev,
        name,
        p1="p",
        p2="n",
        V_ic=None,
        V_ic_fixed=False,
        I_ic=None,
        I_ic_fixed=False,
    ):
        super().__init__()
        self.Vp, self.Ip = self.declare_electrical_port(
            ev, p1, I_ic=I_ic, I_ic_fixed=I_ic_fixed
        )
        self.Vn, self.In = self.declare_electrical_port(ev, p2)
        self.V = self.declare_symbol(
            ev, "V", name, kind=SymKind.var, ic=V_ic, ic_fixed=V_ic_fixed
        )

        self.add_eqs(
            [
                sp.Eq(self.Vp.s - self.Vn.s, self.V.s),
                sp.Eq(0, self.Ip.s + self.In.s),
            ]
        )
        # This defines that, in the WebApp, p1 is on the left and p2 on the right of the block.
        self.port_idx_to_name = {-1: p1, 1: p2}


class Battery(ElecTwoPin):
    """
    Simple battery cell model.
    State of charge is tracked by coulomb counting.
    Open Circuit Voltage (OCV) is computed by OCV_min + (OCV_max - OCV_min)*SOC.
    Terminal voltage is computed by Vt = OCV - I*R.

    This component is overly simplistic and meant for demo purposes only.
    """

    def __init__(
        self,
        ev,
        name=None,
        AH=1.0,
        OCV_min=10.0,
        OCV_max=15.0,
        R=0.01,
        initial_soc=0.5,
        initial_soc_fixed=False,
        enable_soc_port=False,
    ):
        self.name = self.__class__.__name__ if name is None else name
        super().__init__(ev, self.name)
        AH = self.declare_symbol(
            ev,
            "AH",
            self.name,
            kind=SymKind.param,
            val=AH,
            validator=lambda AH: AH > 0.0,
            invalid_msg=f"Component {self.__class__.__name__} {self.name} must have AH>0",
        )
        # FIXME: OCV_min and OCV_max should really have a relative range validation check,
        # but the way param validation is implemented to fit in the scheme described i parameter.py,
        # this presently is not possible due to the complexity of tracking the relationship all the
        # way into the AcausalSystem initialize method.
        OCV_min = self.declare_symbol(
            ev,
            "OCV_min",
            self.name,
            kind=SymKind.param,
            val=OCV_min,
            validator=lambda OCV_min: OCV_min > 0.0,
            invalid_msg=f"Component {self.__class__.__name__} {self.name} must have OCV_min>0",
        )
        OCV_max = self.declare_symbol(
            ev,
            "OCV_max",
            self.name,
            kind=SymKind.param,
            val=OCV_max,
            validator=lambda OCV_max: OCV_max > 0.0,
            invalid_msg=f"Component {self.__class__.__name__} {self.name} must have OCV_max>0",
        )
        R = self.declare_symbol(
            ev,
            "R",
            self.name,
            kind=SymKind.param,
            val=R,
            validator=lambda R: R > 0.0,
            invalid_msg=f"Component {self.__class__.__name__} {self.name} must have R>0",
        )
        SOC = self.declare_symbol(
            ev,
            "SOC",
            self.name,
            kind=SymKind.var,
            ic=initial_soc,
            ic_fixed=initial_soc_fixed,
        )
        dSOC = self.declare_symbol(
            ev,
            "dSOC",
            self.name,
            kind=SymKind.var,
            int_sym=SOC,
            ic=0.0,
        )
        SOC.der_sym = dSOC
        self.add_eqs(
            [
                sp.Eq(dSOC.s, self.Ip.s / AH.s / 3600),
                sp.Eq(
                    self.V.s,
                    OCV_min.s + (OCV_max.s - OCV_min.s) * SOC.s + R.s * self.Ip.s,
                ),
            ]
        )

        if enable_soc_port:
            soc = self.declare_symbol(ev, "soc", self.name, kind=SymKind.outp)
            self.declare_equation(sp.Eq(soc.s, SOC.s), kind=EqnKind.outp)


class Capacitor(ElecTwoPin):
    """
    Ideal capacitor in electrical domain. The characteristic equation is:
    Derivative(v(t)) = i(t)*C, where C is the capacitance in Farads.

    Args:
        C (number):
            Capacitance in Farads.
        initial_voltage (number):
            Initial voltage of the capacitor.
    """

    def __init__(
        self, ev, name=None, C=1.0, initial_voltage=0.0, initial_voltage_fixed=False
    ):
        self.name = self.__class__.__name__ if name is None else name
        super().__init__(
            ev, self.name, V_ic=initial_voltage, V_ic_fixed=initial_voltage_fixed
        )
        C = self.declare_symbol(
            ev,
            "C",
            self.name,
            kind=SymKind.param,
            val=C,
            validator=lambda C: C > 0.0,
            invalid_msg=f"Component {self.__class__.__name__} {self.name} must have C>0",
        )
        dV = self.declare_symbol(
            ev,
            "dV",
            self.name,
            kind=SymKind.var,
            int_sym=self.V,
            ic=0.0,
        )
        self.V.der_sym = dV
        self.add_eqs([sp.Eq(self.Ip.s, C.s * dV.s)])


class CurrentSensor(ElecTwoPin):
    """
    Ideal current sensor in electrical domain.
    """

    def __init__(self, ev, name=None):
        self.name = self.__class__.__name__ if name is None else name
        super().__init__(ev, self.name)
        i = self.declare_symbol(ev, "i", self.name, kind=SymKind.outp)
        # the current output is the current at either pin. chose Ip.s at pin 'p'
        # for sign convention. Use declare_equation() so we can set the EqnKind
        # as 'output'.
        self.declare_equation(sp.Eq(i.s, self.Ip.s), kind=EqnKind.outp)
        # current sensor has no effect on the system. it is inline, but has not
        # voltage across it, this is the 'ideal' part.
        self.declare_equation(sp.Eq(self.Vp.s, self.Vn.s))


class CurrentSource(ElecTwoPin):
    """
    Ideal current source in electrical domain.
    """

    def __init__(
        self,
        ev,
        name=None,
        i=1.0,  # noqa
        enable_current_port=False,
        **kwargs,
    ):
        raise NotImplementedError("Electrical CurrentSource not implemented.")
        # Although this appears to be implemented, it has never been successful
        # in a test.

        self.name = self.__class__.__name__ if name is None else name
        super().__init__(ev, self.name)

        if enable_current_port:
            i = self.declare_symbol(ev, "i", self.name, kind=SymKind.inp, val=i)
        else:
            i = self.declare_symbol(ev, "i", self.name, kind=SymKind.param, val=i)

        self.add_eqs([sp.Eq(self.Ip.s, i.s)])


class Ground(ComponentBase):
    """
    *ground* reference in electrical domain.

    Note: the only 'single' pin component in electrical domain.
    """

    def __init__(self, ev, name=None):
        super().__init__()
        self.name = self.__class__.__name__ if name is None else name
        v, i = self.declare_electrical_port(ev, "p")
        self.add_eqs([sp.Eq(0, v.s)])
        self.port_idx_to_name = {-1: "p"}


class IdealMotor(ComponentBase):
    """
    Ideal 4-quadrant motor with inertia, but no visous losses. The governing equations:
        trq = Kt*I
        backEMF = Ke*w
        V - backEMF = I*R
        heatflow = I*I*R

    Note on efficiency. In this simple case, power loss is I*I*R,
    but this is not explicitly computed, unless the heat_port is enabled.
    Because there are no electro-magnetic losses, this means mech power and
    BackEMF power are equal. Some algebra shows that Kt=Ke; therfore the
    component has only K as a parameter.

    Note on sign convention. I1 is used everywhere, to maintain consistent
    sign of the current in the equations.
    BackEFM and rotation velocity always have the same sign.
    Current and Torque always have the same sign.

    Args:
        R (number):
            Armateur resistance in Ohms.
        K (number):
            Torque constant with unit Nm/Amp, and Back ElectrocMotive Force
            (backEMF) constant with units Volts/(rad/s).
        L (number):
            Armateur inductance in Henry.
        J (number):
            Armateur inertia in Kg*m^2.
        enable_heat_port (bool):
            When true, exposes a thermal port which acts as a heatflow source.
        initial_angle (number):
            Initial angle of the armateur.
        initial_velocity (number):
            Initial velocity of the armateur.
    """

    def __init__(
        self,
        ev,
        name=None,
        R=1.0,
        K=1.0,
        L=1e-6,
        J=1.0,
        initial_velocity=0.0,
        initial_velocity_fixed=False,
        initial_angle=0.0,
        initial_angle_fixed=False,
        initial_current=0.0,
        initial_current_fixed=False,
        enable_heat_port=False,
    ):
        self.name = self.__class__.__name__ if name is None else name
        super().__init__()

        Vp, Ip = self.declare_electrical_port(
            ev,
            "pos",
            I_ic=initial_current,
            I_ic_fixed=initial_current_fixed,
        )
        Vn, In = self.declare_electrical_port(ev, "neg")
        trq, ang, w, alpha = self.declare_rotational_port(
            ev,
            "shaft",
            w_ic=initial_velocity,
            w_ic_fixed=initial_velocity_fixed,
            ang_ic=initial_angle,
            ang_ic_fixed=initial_angle_fixed,
        )
        self.port_idx_to_name = {-1: "pos", -2: "neg", 1: "shaft"}

        R = self.declare_symbol(
            ev,
            "R",
            self.name,
            kind=SymKind.param,
            val=R,
            validator=lambda R: R > 0.0,
            invalid_msg=f"Component {self.__class__.__name__} {self.name} must have R>0",
        )
        K = self.declare_symbol(
            ev,
            "K",
            self.name,
            kind=SymKind.param,
            val=K,
            validator=lambda K: K > 0.0,
            invalid_msg=f"Component {self.__class__.__name__} {self.name} must have K>0",
        )
        L = self.declare_symbol(
            ev,
            "L",
            self.name,
            kind=SymKind.param,
            val=L,
            validator=lambda L: L > 0.0,
            invalid_msg=f"Component {self.__class__.__name__} {self.name} must have L>0",
        )
        J = self.declare_symbol(
            ev,
            "J",
            self.name,
            kind=SymKind.param,
            val=J,
            validator=lambda J: J > 0.0,
            invalid_msg=f"Component {self.__class__.__name__} {self.name} must have J>0",
        )
        backEMF = self.declare_symbol(
            ev, "backEMF", self.name, kind=SymKind.var, ic=0.0
        )
        dI = self.declare_symbol(
            ev, "dI", self.name, kind=SymKind.var, int_sym=Ip, ic=0.0
        )

        self.add_eqs(
            [
                # NOTE: flow vars are negative for flow going out of the component,
                # since torque flows out of the motor when I1 is positive, we
                # need the minus sign on 't'.
                sp.Eq(-trq.s, K.s * Ip.s - J.s * alpha.s),  # torque balance
                sp.Eq(backEMF.s, K.s * w.s),
                sp.Eq(
                    Vp.s - Vn.s - backEMF.s, Ip.s * R.s + dI.s * L.s
                ),  # voltage balance
                sp.Eq(0, Ip.s + In.s),
            ]
        )

        if enable_heat_port:
            port_name = "heat"
            T, Q = self.declare_thermal_port(ev, port_name)
            # NOTE: flow vars are negative for flow going out of the component,
            # since heat flows out of the resistor, we
            # need the minus sign on 'Q'.
            self.add_eqs([sp.Eq(-Q.s, Ip.s * Ip.s * R.s)])
            self.port_idx_to_name[2] = port_name


class Inductor(ElecTwoPin):
    """
    Ideal inductor in electrical domain. The characteristic equation is:
    Derivative(i(t))*L = v(t), where L is the inductance in Henry.

    Args:
        L (number):
            Inductance in Henry.
        initial_current (number):
            Initial current flowing through inductor.
    """

    def __init__(
        self, ev, name=None, L=1.0, initial_current=0.0, initial_current_fixed=False
    ):
        self.name = self.__class__.__name__ if name is None else name
        super().__init__(
            ev, self.name, I_ic=initial_current, I_ic_fixed=initial_current_fixed
        )
        L = self.declare_symbol(
            ev,
            "L",
            self.name,
            kind=SymKind.param,
            val=L,
            validator=lambda L: L > 0.0,
            invalid_msg=f"Component {self.__class__.__name__} {self.name} must have L>0",
        )
        dI = self.declare_symbol(
            ev, "dI", self.name, kind=SymKind.var, int_sym=self.Ip, ic=0.0
        )
        self.Ip.der_sym = dI
        self.add_eqs([sp.Eq(self.V.s, L.s * dI.s)])


class Resistor(ElecTwoPin):
    """
    Ideal resistor in electrical domain. The characteristic equation is:
    v(t) = i(t)*R, where R is the resistance in Ohms.

    When heat port is enabled, the thermal equation is:
    heatflow(t) = i(t)*i(t)*R.

    Args:
        R (number):
            Electrical resistance in Ohms.
        enable_heat_port (bool):
            When true, exposes a thermal port which acts as a heatflow source.
    """

    def __init__(self, ev, name=None, R=1.0, enable_heat_port=False):
        self.name = self.__class__.__name__ if name is None else name

        super().__init__(ev, self.name)
        R = self.declare_symbol(
            ev,
            "R",
            self.name,
            kind=SymKind.param,
            val=R,
            validator=lambda R: R > 0.0,
            invalid_msg=f"Component {self.__class__.__name__} {self.name} must have R>0",
        )
        self.add_eqs([sp.Eq(self.V.s, self.Ip.s * R.s)])

        if enable_heat_port:
            port_name = "heat"
            T, Q = self.declare_thermal_port(ev, port_name)
            # NOTE: flow vars are negative for flow going out of the component,
            # since heat flows out of the resistor, we
            # need the minus sign on 'Q'.
            self.add_eqs([sp.Eq(-Q.s, self.Ip.s * self.Ip.s * R.s)])
            self.port_idx_to_name[2] = port_name


class VoltageSensor(ElecTwoPin):
    """
    Ideal voltage sensor in electrical domain.
    """

    def __init__(self, ev, name=None):
        self.name = self.__class__.__name__ if name is None else name
        super().__init__(ev, self.name)

        v = self.declare_symbol(ev, "v", self.name, kind=SymKind.outp)
        self.declare_equation(sp.Eq(v.s, self.V.s), kind=EqnKind.outp)
        # ensure the sensor does not contribute to flow balance equations.
        self.add_eqs(
            [
                sp.Eq(self.Ip.s, 0),
                sp.Eq(self.In.s, 0),
            ]
        )


class VoltageSource(ElecTwoPin):
    """
    Ideal voltage source in electrical domain.

    Args:
        v (number):
            Voltage value when enable_voltage_port=False.
        enable_voltage_port (bool):
            When true, the voltage value is from a input signal. When false, voltage
            value is from 'v'.
    """

    def __init__(self, ev, name=None, v=1.0, enable_voltage_port=False, **kwargs):
        self.name = self.__class__.__name__ if name is None else name
        super().__init__(ev, self.name)

        if enable_voltage_port:
            v = self.declare_symbol(ev, "v", self.name, kind=SymKind.inp)
        else:
            v = self.declare_symbol(ev, "v", self.name, kind=SymKind.param, val=v)

        self.add_eqs([sp.Eq(self.V.s, v.s)])
