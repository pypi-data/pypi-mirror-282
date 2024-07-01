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

from .base import SymKind

# from .base import Sym, Eqn, SymKind, EqnKind
# from .component_base import ComponentBase
# from .electrical import ElecTwoPin
from .rotational import RotationalOnePort

# from .thermal import ThermalOnePort
import numpy as np

if TYPE_CHECKING:
    import sympy as sp
else:
    sp = LazyLoader("sp", globals(), "sympy")

"""
components here are just sandbox development. they will either go away,
or be moved to a proper domain library.
"""


class TorqueSwitch(RotationalOnePort):
    """
    Ideal torque source in rotational domain.

    Args:
        tau (number):
            Torque value when enable_torque_port=False.
        enable_torque_port (bool):
            When true, the torque value is from a input signal. When false,
            torque value is from 'tau'.
        enable_flange_b (bool):
            When flange_b enabled, applies torque between flange_a and flange_b.
            when flange_b disbaled, applies absolute torque to flange_a.
    """

    def __init__(
        self,
        ev,
        name=None,
        tau=0.0,
        wThr=10.0,
        onTrq=-5.0,
        offTrq=10.0,
    ):
        self.name = self.__class__.__name__ if name is None else name
        super().__init__(ev, self.name)

        # trqOn = self.declare_symbol(ev, "trqOn", self.name, kind=SymKind.var)
        # trqOn = self.declare_symbol(
        #     ev, "trqOn", self.name, kind=SymKind.param, val=True
        # )
        wThr = self.declare_symbol(ev, "wThr", self.name, kind=SymKind.param, val=wThr)
        onTrq = self.declare_symbol(
            ev, "onTrq", self.name, kind=SymKind.param, val=onTrq
        )
        offTrq = self.declare_symbol(
            ev, "offTrq", self.name, kind=SymKind.param, val=offTrq
        )

        # switch_f = sp.Function("jax.numpy.where")(
        #     trqOn.s,
        #     onTrq.s,
        #     offTrq.s,
        # )
        switch_f = sp.Piecewise(
            (onTrq.s, self.w.s <= wThr.s),
            (offTrq.s, self.w.s > wThr.s),
        )
        switch_sym = self.declare_symbol(
            ev,
            "switch_f",
            self.name,
            sym=switch_f,
            kind=SymKind.lut,  # FIXME: needs to expand this category, or make new one
        )

        # FIXME: for some reason, the first equation below never appeared in 'original equations'
        # from DiagramProcessing.
        # self.add_eqs(
        #     [sp.Eq(trqOn.s, self.w.s >= wThr.s), sp.Eq(self.t.s, switch_sym.s)]
        # )
        self.add_eqs([sp.Eq(self.t.s, switch_sym.s)])


def process_peak_trq(
    name,
    peaktrq_spd=None,
    peaktrq_trq=None,
    peak_trq=None,
    peak_pwr=None,
):
    if peaktrq_spd is None:
        peaktrq_spd = np.arange(0, 1000, 50)
    if peaktrq_trq is None:
        if peak_pwr is None:
            peak_pwr = 100e3  # Watts
        if peak_trq is None:
            peak_trq = 200  # Nm
        peak_trq_v = np.ones_like(peaktrq_spd) * peak_trq  # Nm
        peak_pwrTrq_v = peak_pwr / np.minimum(peaktrq_spd, 1.0)  # Nm
        peaktrq_trq = np.minimum(peak_trq_v, peak_pwrTrq_v)

    return peaktrq_spd, peaktrq_trq


# class BLDC(ComponentBase):
#     """
#     This is still WIP. Not tested.
#     FIXME: equation 4 below is not implemented yet.
#     Brushless Direct Current Motor (BLDC).
#     Combined Motor-Inverter model for a 4 Quadrant BLDC motor. The governing equations:
#         1. trq = min(trq_req, peaktrq_lut(speed))
#         2. mech_pwr = trq * speed
#         3. eff_1quad = eff_table(abs(trq),abs(speed))
#         4. eff = if sign(trq*speed) > 0 then eff_1quad, else 1/eff_1quad
#         5. elec_pwr = mech * eff
#         6. I = elec_pwr/V
#     optionally:
#         7. heat = abs(elec_pwr - mech_pwr)

#     This component requires the following lookup tables:
#         peaktrq: 1D lookup from speed[0:inf] to trq[0:inf]
#         eff_table: 2D lookup from (speed[0:inf],trq[0:inf]) to eff[0:1]
#     where [a:b] means the range of the variable.

#     Inputs:
#         trq_req: causal signal for torque request from external controller.

#     From the rotational domain, the components is like a torque source, from the
#     electrical domain, the component is like a current source. And optionally, from
#     the thermal domain, the component is like a heat source.

#     Note on sign convention. We use I1 everywhere, to maintain consistent
#     sign of the current in the equations.
#     """

#     def __init__(
#         self,
#         eqn_env,
#         name=None,
#         peaktrq_spd=None,
#         peaktrq_trq=None,
#         peak_trq=None,
#         peak_pwr=None,
#         eff_spd=None,
#         eff_trq=None,
#         eff_eff=None,
#         enable_heat_port=False,
#     ):
#         self.name = "bldc" if name is None else name

#         self.electrical = ElecTwoPin(eqn_env, self.name, p1="pos", p2="neg")
#         self.shaft = RotationalOnePort(eqn_env, self.name, p="shaft")

#         self.ports = {**self.electrical.ports, **self.shaft.ports}
#         self.syms = self.electrical.syms | self.shaft.syms
#         self.eqs = self.electrical.eqs | self.shaft.eqs

#         # process user provided parameters
#         self.peaktrq_spd, self.peaktrq_trq = process_peak_trq(
#             self.name,
#             peaktrq_spd,
#             peaktrq_trq,
#             peak_trq,
#             peak_pwr,
#         )

#         if len(self.peaktrq_spd) != len(self.peaktrq_trq):
#             raise ValueError(
#                 f"Component BLDC {self.name} peaktrq_spd and peaktrq_trq must be same length."
#             )

#         eff_params = [eff_spd, eff_trq, eff_eff]
#         if any(eff_params) and not all(eff_params):
#             raise ValueError(
#                 f"Component BLDC {self.name} eff_spd, eff_trq and eff_eff must be all defined, or all None."
#             )
#         if None in eff_params:
#             self.eff_spd = np.linspace(0, np.max(self.peaktrq_spd), 20)
#             self.eff_trq = np.linspace(0, np.max(self.peaktrq_trq), 20)
#             self.eff_eff = np.ones((len(self.eff_spd), len(self.eff_trq))) * 0.9

#         # create component symbols
#         self.peaktrq_spd_s = Sym(
#             eqn_env,
#             self.name + "_peaktrq_spd",
#             kind=SymKind.param,
#             val=self.peaktrq_spd,
#         )
#         self.peaktrq_trq_s = Sym(
#             eqn_env,
#             self.name + "_peaktrq_trq",
#             kind=SymKind.param,
#             val=self.peaktrq_trq,
#         )
#         self.eff_spd_s = Sym(
#             eqn_env, self.name + "_eff_spd", kind=SymKind.param, val=self.eff_spd
#         )
#         self.eff_trq_s = Sym(
#             eqn_env, self.name + "_eff_trq", kind=SymKind.param, val=self.eff_trq
#         )
#         self.eff_eff_s = Sym(
#             eqn_env, self.name + "_eff_eff", kind=SymKind.param, val=self.eff_eff
#         )

#         self.Pmech = Sym(eqn_env, self.name + "_Pmech", kind=SymKind.var)
#         self.Pelec = Sym(eqn_env, self.name + "_Pelec", kind=SymKind.var)
#         self.Treq = Sym(eqn_env, self.name + "_Treq", kind=SymKind.inp)
#         self.Eff1Quad = Sym(eqn_env, self.name + "_Eff1Quad", kind=SymKind.var)
#         self.Eff = Sym(eqn_env, self.name + "_Eff", kind=SymKind.var)

#         # create component specific lookup table function symbols
#         self.peak_trq_lut = sp.Function("interp")(
#             self.shaft.w.s,
#             self.peaktrq_spd_s.s,
#             self.peaktrq_trq_s.s,
#         )
#         self.eff_lut = sp.Function("interp2d")(
#             self.shaft.w.s,
#             self.shaft.t.s,
#             self.eff_spd_s.s,
#             self.eff_trq_s.s,
#             self.eff_eff_s.s,
#         )
#         self.syms.update(
#             {
#                 self.peaktrq_spd_s,
#                 self.peaktrq_trq_s,
#                 self.eff_spd_s,
#                 self.eff_trq_s,
#                 self.eff_eff_s,
#                 self.Pmech,
#                 self.Pelec,
#                 self.Treq,
#                 self.Eff1Quad,
#                 self.Eff,
#                 self.peak_trq_lut,
#                 self.eff_lut,
#             }
#         )

#         self.eqs.update(
#             {
#                 Eqn(
#                     e=sp.Eq(self.shaft.t.s, sp.min(self.Treq.s, self.peak_trq_lut)),
#                     kind=EqnKind.comp,
#                 ),  # eqn 1
#                 Eqn(
#                     e=sp.Eq(self.Pmech.s, self.shaft.t.s * self.shaft.w.s),
#                     kind=EqnKind.comp,
#                 ),  # eqn 2
#                 Eqn(
#                     e=sp.Eq(self.Eff.s, self.eff_lut),
#                     kind=EqnKind.comp,
#                 ),  # eqn 3
#                 # FIXME: eqn 4 is missing, so energy is not conserved
#                 Eqn(
#                     e=sp.Eq(self.Pelec.s, self.Pmech.s * self.Eff.s),
#                     kind=EqnKind.comp,
#                 ),  # eqn 5
#                 Eqn(
#                     e=sp.Eq(self.electrical.I1.s, self.Pelec.s / self.electrical.V.s),
#                     kind=EqnKind.comp,
#                 ),  # eqn 6
#             }
#         )

#         if enable_heat_port:
#             self.heat = ThermalOnePort(eqn_env, self.name, p="heat")

#             self.ports.update(self.heat.ports)
#             self.syms.update(self.heat.syms)
#             self.eqs.update(
#                 {
#                     Eqn(
#                         e=sp.Eq(self.heat.Q.s, sp.abs(self.Pelec.s - self.Pmech.s)),
#                         kind=EqnKind.comp,
#                     ),
#                 }
#             )
