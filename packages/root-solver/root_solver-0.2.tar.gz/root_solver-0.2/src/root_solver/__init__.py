"""
root-solver provides solvers for polynomials of orders 2 and 3, using the
algorithms of Kahan and others. See
http://www.cs.berkeley.edu/~wkahan/Math128/Cubic.pdf for more information about
the algorithms included.

Additionally root-solver includes support for tracking a single root as the
coefficients of the polynomial changes.
"""

from ._cubic import (
    solve_cubic, CubicTracker, compute_cubic_with_error_estimate,
)
from ._quadratic import solve_quadratic

from . import _version
__version__ = _version.get_versions()['version']

__all__ = [
    "__version__",
    "solve_cubic",
    "solve_quadratic",
    "CubicTracker",
]
