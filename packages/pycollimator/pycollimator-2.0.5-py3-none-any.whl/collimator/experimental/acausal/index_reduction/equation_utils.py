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

from functools import partial

import jax
import jax.numpy as jnp
import numpy as np

from collimator.lazy_loader import LazyLoader

if TYPE_CHECKING:
    import sympy as sp
    import sympy.core.function as scf
else:
    sp = LazyLoader("sp", globals(), "sympy")
    scf = LazyLoader("scf", globals(), "sympy.core.function")


jax.config.update("jax_enable_x64", True)


def extract_vars(eq, known_vars):
    """
    Extract variables from equations in their precise form, differentiating between
    non-derivatives and derivatives, and excluding known_vars.

    x(t) + y(t) = 0 -> {}, {x, y}
    x(t).diff(t) + y(t) = 0 -> {dx/dt}, {y}
    x(t).diff(t) + y(t).diff(t) = 0 -> {dx/t, dy/dt}, {}
    x(t) + x(t).diff(t) + y(t) = 0 -> {dx/t}, {x,y}
    x(t) + x(t).diff(t,t) + y(t).diff(t) = 0 -> {d2x/dt2, dy/dt}, {x}

    Parameters
    ----------
    eq : sympy equation
        A sympy equation from which variables need to be extracted
    known_vars : set
        Set of known variables

    Returns
    -------
    d_vars : set
        Set of differential variables
    a_vars : set
        Set of algebraic variables
    """

    d_vars = set()
    a_vars = set()

    def is_known(var):
        if var in known_vars:
            return True
        # check if the integrals of the variable are known
        if isinstance(var, sp.Derivative):
            return var.expr in known_vars
        # check if the derivatives of the variable are known
        if isinstance(var, scf.AppliedUndef):
            return any(
                var == known.expr
                for known in known_vars
                if isinstance(known, sp.Derivative)
            )
        return False

    # Create a dummy equation by replacing all the derivatives
    true_to_dummy = {}
    for der in eq.atoms(sp.Derivative):
        dummy = sp.Symbol("d_" + str(der))
        true_to_dummy[der] = dummy
    dummy_eq = eq.subs(true_to_dummy)

    # Find algebraic variables in the dummy equation
    a_vars = dummy_eq.atoms(scf.AppliedUndef)
    a_vars = {var for var in a_vars if not is_known(var)}

    d_vars = eq.atoms(sp.Derivative)
    d_vars = {var for var in d_vars if not is_known(var)}

    return d_vars, a_vars


def process_equations(eqs, known_vars):
    """
    f(x, x_dot, y ) = 0

    extract lists of x, x_dot, and y from the list of eqs representing `f`
    """

    d_vars = set()
    a_vars = set()

    vars_in_eqs = {}
    eqs_idx = {}
    for idx, eq in enumerate(eqs):
        eq_d_vars, eq_a_vars = extract_vars(eq, known_vars)
        d_vars.update(eq_d_vars)
        a_vars.update(eq_a_vars)
        vars_in_eqs[eq] = eq_d_vars.union(eq_a_vars)
        eqs_idx[idx] = eq

    x_dot = d_vars
    x = {var.expr for var in x_dot}
    y = a_vars.difference(x)
    X = set().union(x, x_dot, y)

    return list(x), list(x_dot), list(y), list(X), vars_in_eqs, eqs_idx


def _make_fixed_point_homotopy(f, x_0):
    """
    Create a fixed point homotopy function.
    h = phi * f(x) + (1 - phi) * (x - x_0), where phi is the homotopy parameter

    Args:
        f (callable): Function returning the residual of the system of equations
        x_0 (array): Initial guess for the solution
    """

    @jax.jit
    def homotopy(x, phi):
        return phi * f(x) + (1.0 - phi) * (x - x_0)

    jac_x = jax.jit(jax.jacfwd(homotopy))
    jac_phi = jax.jit(jax.jacfwd(homotopy, argnums=1))

    return homotopy, jac_x, jac_phi


def _make_newton_homotopy(f, x_0):
    """
    Create a Newton homotopy function.
    h = phi * f(x) + phi * (f(x) - f(x_0)), where phi is the homotopy parameter

    Args:
        f (callable): Function returning the residual of the system of equations
        x_0 (array): Initial guess for the solution
    """

    @jax.jit
    def homotopy(x, phi):
        return phi * f(x) + (1.0 - phi) * (f(x) - f(x_0))

    jac_x = jax.jit(jax.jacfwd(homotopy))
    jac_phi = jax.jit(jax.jacfwd(homotopy, argnums=1))

    return homotopy, jac_x, jac_phi


def _make_affine_homotopy(f, x_0):
    """
    Create an affine homotopy function.
    h = phi * f(x) + (1 - phi) * f'(x_0) . (x-x_0), where phi is the homotopy parameter

    Args:
        f (callable): Function returning the residual of the system of equations
        x_0 (array): Initial guess for the solution
    """

    fp = jax.jacfwd(f)
    fp_x0 = fp(x_0)

    @jax.jit
    def homotopy(x, phi):
        return phi * f(x) + (1.0 - phi) * jnp.dot(fp_x0, x - x_0)

    jac_x = jax.jit(jax.jacfwd(homotopy))
    jac_phi = jax.jit(jax.jacfwd(homotopy, argnums=1))

    return homotopy, jac_x, jac_phi


def _newton_raphson(f, x_0, jac, tol=1e-10, max_iter=100):
    """
    Use Newton-Raphson iteration to find roots of `f(x)=0` starting from `x=x_0`.
    `jac=df/dx` is the Jacobian of `f`.
    """

    def newton_step(x):
        return x - jnp.linalg.solve(jac(x), f(x))

    x = x_0
    for _ in range(max_iter):
        x_new = newton_step(x)
        if jnp.linalg.norm(x_new - x) < tol:
            break
        x = x_new
    else:
        raise ValueError(f"Newton's method did not converge for {f=}")
    return x


def _corrector_newton_solve(h, x_0, phi, jac_x, tol=1e-10, max_iter=100):
    """
    Use Newton-Raphson iteration to find roots of `h(x,phi)` for a fixed `phi`, and
    starting from `x_0`.

    `jac_x=dh/dx` is the Jacobian of `h`.
    """

    partial_h = partial(h, phi=phi)
    parital_jac_x = partial(jac_x, phi=phi)

    x = _newton_raphson(partial_h, x_0, parital_jac_x, tol=tol, max_iter=max_iter)

    return x


def predictor_corrector_homotopy(
    h, jac_x, jac_phi, x_0, num_steps=100, tol=1e-10, max_iter=100
):
    phi_arr = jnp.linspace(0, 1.0, num_steps)
    dphi = phi_arr[1] - phi_arr[0]

    dx_dphi = jax.jit(lambda x, phi: jnp.linalg.solve(jac_x(x, phi), -jac_phi(x, phi)))

    for phi in phi_arr:
        # Correct
        sol_x = _corrector_newton_solve(h, x_0, phi, jac_x, tol, max_iter)

        # Predict
        x_0 = sol_x + dx_dphi(sol_x, phi) * dphi

    return sol_x


def pseudo_arclength_homotopy(
    h, jac_x, jac_phi, x_0, ds=0.1, num_steps=100, tol=1e-10, max_iter=100
):
    """
    Use pseudo-arclength continuation to find roots of h starting from x_0.

    `s` is the pseudo-arclength parameter.

    `y = [x(s), phi(s)]` are the augmented variables.

    We need to solve the augmented system:
    ```
    H = [ h(x, phi) = 0,
          v (x - x_0) + w (phi - phi_0) - (s-s_0) = 0 ]
    ```

    where `v` and `w` are the normalized components of the tangent vector (v', w')
    to the solution curve at `(x, phi)`.

    ```
    v' = d x(s) / ds
    w' = d phi(s) / ds
    ```

    and satisfy:

    ```
    dh/dx v' + dh/dphi w' = 0
    ```
    """

    def normalized_tangent_vector(x, phi):
        """
        Obtain normalized tangent vector (v,w) at (x, phi)
        """
        wp = 1.0

        A = jac_x(x, phi)
        b = -jac_phi(x, phi)

        vp = jnp.linalg.solve(A, b)

        tangent = jnp.hstack([vp, wp])
        norm = jnp.linalg.norm(jnp.hstack([vp, wp]))

        normalized_tangent = tangent / norm
        v, w = normalized_tangent[:-1], normalized_tangent[-1]

        return v, w

    # Define the augmented system
    def H(y, x_0, phi_0, ds, v, w):
        """
        x_0 and phi_0 are solutions at s_0, and
        ds = s - s_0
        """
        x, phi = y[:-1], y[-1]
        return jnp.hstack([h(x, phi), v @ (x - x_0) + w * (phi - phi_0) - ds])

    # Jacobian of the augmented system
    jac_H = jax.jit(jax.jacfwd(H))

    # Initialize the solution
    s_0 = 0.0
    phi_0 = 0.0

    # Solve the homotopy for phi=0.0
    x_0 = _corrector_newton_solve(h, x_0, phi_0, jac_x, tol, max_iter)

    phi_arr = np.zeros(num_steps + 1)
    x_arr = np.zeros((num_steps + 1, len(x_0)))
    s_arr = np.zeros(num_steps + 1)

    phi_arr[0] = phi_0
    x_arr[0, :] = x_0
    s_arr[0] = s_0

    reached_phi_equals_1 = False
    for sol_idx in range(num_steps):
        v, w = normalized_tangent_vector(x_0, phi_0)

        x_pred = x_0 + ds * v
        phi_pred = phi_0 + ds * w
        s_0 += ds

        y_0 = jnp.hstack([x_pred, phi_pred])

        partial_H = partial(H, x_0=x_0, phi_0=phi_0, ds=ds, v=v, w=w)
        partial_jac_H = partial(jac_H, x_0=x_0, phi_0=phi_0, ds=ds, v=v, w=w)
        y = _newton_raphson(partial_H, y_0, partial_jac_H, tol, max_iter)

        x_0, phi_0 = y[:-1], y[-1]

        s_arr[sol_idx + 1] = s_0
        x_arr[sol_idx + 1, :] = x_0
        phi_arr[sol_idx + 1] = phi_0

        if phi_0 >= 1.0:
            print(f"Reached phi = {phi_0} at step {sol_idx+1}")
            reached_phi_equals_1 = True
            break

    if not reached_phi_equals_1:
        raise ValueError(
            "Homotopy did not converge to lambda=1.0. The iteration reached "
            f"lambda={phi_0} with {ds=} and {num_steps=}. "
            "Consider increasing `num_steps` and/or decreasing `ds`."
        )

    # Do a final solve for phi=1.0
    sol_x = _corrector_newton_solve(h, x_0, 1.0, jac_x, tol, max_iter)

    return sol_x


def homotopy_roots(
    f,
    x_0,
    homotopy_type="newton",
    solver="pseudo_arclength",
    ds=0.1,
    num_steps=100,
    tol=1e-10,
    max_iter=100,
):
    """
    Find the roots of a system of equations gf(x)=0` starting from `x=x_0`
    using homotopy methods.

    If `g(x)` is the simpler system of equations (determined by `homopty_type`),
    then the homotopy function `h(x, phi)` is defined as
    ```
    h = phi * f(x) + (1 - phi) * g(x)
    ```
    where `phi` is the homotopy parameter, classically denoted by `lambda`.
    """

    get_make_homotopy = {
        "fixed_point": _make_fixed_point_homotopy,
        "newton": _make_newton_homotopy,
        "affine": _make_affine_homotopy,
    }

    make_homotopy = get_make_homotopy[homotopy_type]

    h, jac_x, jac_phi = make_homotopy(f, x_0)

    if solver == "predictor_corrector":
        sol_x = predictor_corrector_homotopy(
            h, jac_x, jac_phi, x_0, num_steps, tol, max_iter
        )
    elif solver == "pseudo_arclength":
        sol_x = pseudo_arclength_homotopy(
            h, jac_x, jac_phi, x_0, ds, num_steps, tol, max_iter
        )

    return sol_x


def scipy_roots(f, x_0, method="lm", tol=None):
    """
    Find the roots of a system of equations `f(x)=0` starting from `x=x_0`
    with `scipy.optimize.root`
    """
    from scipy.optimize import root

    f = jax.jit(f)
    df_dx = jax.jit(jax.jacfwd(f))

    res = root(f, x_0, jac=df_dx, method=method, tol=tol)

    if not res.success:
        raise ValueError(
            "Numerical solution of ICs with root finding failed with "
            f"final residual = {res.fun}"
        )

    return res.x


def compute_condition_number(t, eqs, X, ics, ics_weak, knowns):
    """
    For a set of equations equations representing `F(X)=0`, if X_0 is the
    union of ics and ics_weak, compute the condition number of the Jacobian
    matrix `dF/dX` at `X_0`.
    """

    dummy_ics = {**ics, **ics_weak}
    dummy_knowns = knowns.copy()
    dummy_X = []

    # Convert derivatives to dummy algebraic variables for safe subsitution
    true_to_dummy = {}
    dummy_to_true = {}

    for var in X:
        if isinstance(var, sp.Derivative):
            dummy = sp.Symbol("d_" + str(var))
            true_to_dummy[var] = dummy
            dummy_to_true[dummy] = var

            if var in dummy_ics:
                dummy_ics[dummy] = dummy_ics.pop(var)
            if var in dummy_knowns:
                dummy_knowns[dummy] = dummy_knowns.pop(var)

            dummy_X.append(dummy)
        else:
            dummy_X.append(var)

    dummy_eqs = [eq.subs(true_to_dummy) for eq in eqs]

    # create F matrix, which will be a function of the dummy_X
    F_sym = sp.Matrix(dummy_eqs)

    dummy_knowns_ders = {
        k: v for k, v in dummy_knowns.items() if isinstance(k, sp.Derivative)
    }
    dummy_knowns_others = {
        k: v for k, v in dummy_knowns.items() if not isinstance(k, sp.Derivative)
    }

    F_sym = sp.Matrix(F_sym.subs(dummy_knowns_ders))
    F_sym = sp.Matrix(F_sym.subs(dummy_knowns_others))

    dummy_X_0 = jnp.array([dummy_ics[var] for var in dummy_X])

    # Lamdify to create a function for root finding and solve numerically
    F_t_x = sp.lambdify([[t, *dummy_X]], F_sym, modules="jax")

    def F(x):
        return jnp.ravel(F_t_x(jnp.insert(x, 0, 0.0)))

    jac_F = jax.jacfwd(F)(dummy_X_0)

    return jnp.linalg.cond(jac_F)


def order_vars_by_impact(t, eqs, X, ics, ics_weak, knowns):
    """
    Order the vars in `ics` in increaseing order of impact on the solution of the
    system of equations representing `F(X)=0`.

    For a set of equations equations representing `F(X)=0`, we want to find the
    variables that have minimal impact on the system of equations. These are the
    variables corresponding to the smallest "maximum absolute value of the columns" of
    the Jacobian matrix `dF/dX`, evaluated at `X_eval = ics U ics_weak`.
    """

    dummy_ics = ics.copy()
    dummy_ics_weak = ics_weak.copy()
    dummy_knowns = knowns.copy()
    dummy_X = []

    # Convert derivatives to dummy algebraic variables for safe subsitution
    true_to_dummy = {}
    dummy_to_true = {}

    for var in X:
        if isinstance(var, sp.Derivative):
            dummy = sp.Symbol("d_" + str(var))
            true_to_dummy[var] = dummy
            dummy_to_true[dummy] = var

            if var in dummy_ics:
                dummy_ics[dummy] = dummy_ics.pop(var)
            if var in dummy_ics_weak:
                dummy_ics_weak[dummy] = dummy_ics_weak.pop(var)
            if var in dummy_knowns:
                dummy_knowns[dummy] = dummy_knowns.pop(var)

            dummy_X.append(dummy)
        else:
            dummy_X.append(var)

    dummy_eqs = [eq.subs(true_to_dummy) for eq in eqs]

    # create F matrix, which will be a function of the dummy_X
    F_sym = sp.Matrix(dummy_eqs)

    dummy_knowns_ders = {
        k: v for k, v in dummy_knowns.items() if isinstance(k, sp.Derivative)
    }
    dummy_knowns_others = {
        k: v for k, v in dummy_knowns.items() if not isinstance(k, sp.Derivative)
    }

    F_sym = sp.Matrix(F_sym.subs(dummy_knowns_ders))
    F_sym = sp.Matrix(F_sym.subs(dummy_knowns_others))

    dummy_X_eval = jnp.array(
        [
            dummy_ics[var] if var in dummy_ics.keys() else dummy_ics_weak[var]
            for var in dummy_X
        ]
    )

    # Lamdify to create a function for root finding and solve numerically
    F_t_x = sp.lambdify([[t, *dummy_X]], F_sym, modules="jax")

    def F(x):
        return jnp.ravel(F_t_x(jnp.insert(x, 0, 0.0)))

    jac_F = jax.jacfwd(F)(dummy_X_eval)

    metric = jnp.max(jnp.abs(jac_F), axis=0)
    sorted_X_indices = jnp.argsort(metric)

    sorted_X = [X[idx] for idx in sorted_X_indices]

    ordered_ics = {key: val for key, val in ics.items() if key in sorted_X}

    return ordered_ics


def check_solvability_with_added_ics(t, eqs, X, ics, new_vars, ics_weak, knowns):
    """
    Append new_vars (list) to ics (dict) and check if the system of equations
    is non-singular at t=0.0
    """

    new_ics_dict = {var: ics_weak[var] for var in new_vars}
    combined_ics = {**ics, **new_ics_dict}

    F, _, x_free, _, true_to_dummy = _make_system_of_ics(
        t, eqs, X, combined_ics, knowns
    )

    dummy_ics_weak = {
        true_to_dummy[var] if var in true_to_dummy.keys() else var: val
        for var, val in ics_weak.items()
    }

    x_0 = jnp.array([dummy_ics_weak[var] for var in x_free])
    jac_F = jax.jacfwd(F)(x_0)

    return jnp.linalg.cond(jac_F)


def _make_system_of_ics(t, eqs, X, ics, knowns):
    ics_and_knowns = ics.copy()
    ics_and_knowns.update(knowns)

    # Convert derivatives to dummy algebraic variables for safe substitution
    true_to_dummy = {}

    for var in X:
        if isinstance(var, sp.Derivative):
            dummy = sp.Symbol("d_" + str(var))
            true_to_dummy[var] = dummy
            if var in ics_and_knowns:
                ics_and_knowns[dummy] = ics_and_knowns.pop(var)

    dummy_eqs = [eq.subs(true_to_dummy) for eq in eqs]

    # create F matrix and x_free vector to solve F(t, x_free) = 0
    F = sp.Matrix(dummy_eqs)

    ics_and_knowns_ders = {
        k: v for k, v in ics_and_knowns.items() if isinstance(k, sp.Derivative)
    }
    ics_and_knowns_others = {
        k: v for k, v in ics_and_knowns.items() if not isinstance(k, sp.Derivative)
    }

    F = sp.Matrix(F.subs(ics_and_knowns_ders))
    F = sp.Matrix(F.subs(ics_and_knowns_others))

    x = [true_to_dummy.get(var, var) for var in X]
    x_free = [var for var in x if var not in ics_and_knowns]  # Variables free to solve

    # Lamdify to create a function for root finding and solve numerically
    residual = sp.lambdify([[t, *x_free]], F, modules="jax")

    # Function whose roots are to be found, `t=0.0` and thus `t` is not a parameter
    def root_func(x):
        # set the first element of x to 0, i.e. t=0.0
        # and call the residual function
        return jnp.ravel(residual(jnp.insert(x, 0, 0.0)))

    return root_func, x, x_free, ics_and_knowns, true_to_dummy


def compute_consistent_initial_conditions(
    t, eqs, X, ics, ics_weak, knowns, config=None
):
    """
    Numerically solve for initial conditions
    """

    if config is None:
        # Config for direct scipy.optimize.root solution
        config = {
            "method": "scipy_root",
            "scipy_root_options": {"solver": "lm", "tol": None},
        }

        # # Config for homotopy based solution
        # config = {
        #     "method": "homotopy",
        #     "homotopy_options": {
        #         "type": "newton",
        #         "solver": "pseudo_arclength",
        #         "ds": 0.1,
        #         "num_steps": 2000,
        #         "tol": 1e-10,
        #         "max_iter": 100,
        #     },
        # }

    root_func, x, x_free, ics_and_knowns, true_to_dummy = _make_system_of_ics(
        t, eqs, X, ics, knowns
    )

    dummy_ics_weak = {
        true_to_dummy[var] if var in true_to_dummy.keys() else var: val
        for var, val in ics_weak.items()
    }

    x_0 = jnp.array([dummy_ics_weak[var] for var in x_free])

    if config["method"] == "scipy_root":
        options = config["scipy_root_options"]
        x_ic = scipy_roots(
            root_func,
            x_0,
            method=options.get("solver", "lm"),
            tol=options.get("tol", None),
        )
    elif config["method"] == "homotopy":
        options = config["homotopy_options"]
        x_ic = homotopy_roots(
            root_func,
            x_0,
            homotopy_type=options.get("type", "newton"),
            solver=options.get("solver", "pseudo_arclength"),
            ds=options.get("ds", 0.1),
            num_steps=options.get("num_steps", 500),
            tol=options.get("tol", 1e-10),
            max_iter=options.get("max_iter", 100),
        )
    else:
        raise ValueError(
            f"Solution configuration {config} is unavailable" " for IC computation"
        )

    # Reconstruct full variable set X_ic with solved values and known ics
    X_ic = []
    x_ic_counter = 0
    for var in x:
        if var in x_free:
            # If the variable was free (solved for), use the solved value
            X_ic.append(x_ic[x_ic_counter])
            x_ic_counter += 1
        else:
            # If the variable was not free (had initial conditions), use the known value
            X_ic.append(ics_and_knowns[var])

    return X_ic
