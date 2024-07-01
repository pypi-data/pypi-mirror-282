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

"""
Scipy/JAX-scipy optimizers from `scipy.optimize.minimize` and
`jax.scipy.optimize.minimize`.
"""

from typing import TYPE_CHECKING
import warnings

import jax
import jax.numpy as jnp

from .base import Optimizer, Optimizable

from ...lazy_loader import LazyLoader

if TYPE_CHECKING:
    import jax.scipy.optimize as jaxopt
    import scipy.optimize as sciopt
else:
    jaxopt = LazyLoader("jaxopt", globals(), "jax.scipy.optimize")
    sciopt = LazyLoader("sciopt", globals(), "scipy.optimize")

ACCEPTS_GRAD = [
    "CG",
    "BFGS",
    "Newton-CG",
    "L-BFGS-B",
    "TNC",
    "SLSQP",
    "dogleg",
    "trust-ncg",
    "trust-krylov",
    "trust-exact",
    "trust-constr",
]

SUPPORTS_BOUNDS = [
    "Nelder-Mead",
    "L-BFGS-B",
    "TNC",
    "SLSQP",
    "Powell",
    "trust-constr",
    "COBYLA",
]

SUPPORTS_CONSTRAINTS = [
    "COBYLA",
    "SLSQP",
    "trust-constr",
]


class Scipy(Optimizer):
    """
    Scipy/JAX-scipy optimizers.

    Parameters:
        optimizable (Optimizable):
            The optimizable object.
        opt_method (str):
            The optimization method to use.
        tol (float):
            Tolerance for termination. For detailed control, use `opt_method_config`.
        opt_method_config (dict):
            Configuration for the optimization method.
        use_autodiff_grad (bool):
            Whether to use autodiff for gradient computation.
        use_jax_scipy (bool):
            Whether to use JAX's version of `optimize.minimize`.
    """

    def __init__(
        self,
        optimizable: Optimizable,
        opt_method,
        tol=None,
        opt_method_config=None,
        use_autodiff_grad=True,
        use_jax_scipy=False,
    ):
        self.optimizable = optimizable
        self.opt_method = opt_method
        self.tol = tol
        self.opt_method_config = opt_method_config or {}
        self.use_autodiff_grad = use_autodiff_grad
        self.use_jax_scipy = use_jax_scipy
        self.optimal_params = None

    def optimize(self):
        """Run optimization"""
        params = self.optimizable.params_0_flat
        objective = jax.jit(self.optimizable.objective_flat)

        if self.use_jax_scipy:
            warnings.warn(
                "`use_jax_scipy` is True. JAX's version of optimize.minimize will be "
                "used. Consequently, `opt_method` will be set of `BFGS` and autodiff "
                "will be used for gradient computation. Constraints and bounds will "
                "be ignored. If you want to use scipy's version of minimize, set "
                " `use_jax_scipy` to False."
            )
            opt_res = jaxopt.minimize(
                objective,
                params,
                method="BFGS",
                tol=self.tol,
                options=self.opt_method_config,
            )
            params = opt_res.x

        else:
            use_jac = False
            if self.opt_method in ACCEPTS_GRAD and self.use_autodiff_grad:
                jac = jax.jit(jax.grad(objective))
                use_jac = True

            # Handle bounds
            bounds = self.optimizable.bounds_flat

            # Jobs from UI would put (-jnp.inf, jnp.inf) as defualt bounds. The user
            # may also have specified bounds this way. Scipy expects `None` to imply
            # unboundedness.
            if bounds is not None:
                bounds = [
                    (
                        None if b[0] == -jnp.inf else b[0],
                        None if b[1] == jnp.inf else b[1],
                    )
                    for b in bounds
                ]

                # Check if all bounds are None, i.e. no bounds at all, and hence
                # algorithms that do not support bounds can be used.
                flattened_bounds = [element for tup in bounds for element in tup]
                all_none = all(element is None for element in flattened_bounds)
                bounds = None if all_none else bounds

            if bounds is not None and self.opt_method not in SUPPORTS_BOUNDS:
                raise ValueError(
                    f"Optimization method scipy:{self.opt_method} "
                    "does not support bounds."
                )

            # Handle constraints
            if (
                self.optimizable.has_constraints
                and self.opt_method not in SUPPORTS_CONSTRAINTS
            ):
                raise ValueError(
                    f"Optimization method scipy:{self.opt_method} "
                    "does not support constraints."
                )

            if self.optimizable.has_constraints:
                constraints = jax.jit(self.optimizable.constraints_flat)
                constraints_jac = jax.jit(jax.jacrev(constraints))
                constraints = sciopt.NonlinearConstraint(
                    constraints, 0.0, jnp.inf, jac=constraints_jac
                )
            else:
                constraints = None

            opt_res = sciopt.minimize(
                objective,
                params,
                method=self.opt_method,
                jac=jac if use_jac else None,
                bounds=bounds,
                constraints=constraints,
                tol=self.tol,
                options=self.opt_method_config,
            )

            params = opt_res.x

        self.optimal_params = self.optimizable.unflatten_params(params)
        if self.optimizable.transformation is not None:
            self.optimal_params = self.optimizable.transformation.inverse_transform(
                self.optimal_params
            )
        return self.optimal_params
