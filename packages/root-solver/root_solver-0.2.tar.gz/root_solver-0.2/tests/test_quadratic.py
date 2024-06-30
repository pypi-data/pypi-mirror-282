from functools import cmp_to_key

from pytest import approx

from hypothesis import given, note, event, assume, example
from hypothesis.strategies import floats, complex_numbers

from numpy import isnan, inf, conj, isreal, abs as np_abs, isfinite

from root_solver import solve_quadratic

sensible_floats = floats(allow_nan=False, allow_infinity=False)
sensible_complex = complex_numbers(allow_nan=False, allow_infinity=False)


def generate_coefficents_from_roots(x_1, x_2):
    b = - (x_1 + x_2)
    c = x_1 * x_2
    return b, c


def bool_to_cmp(cond):
    return 1 if cond else -1


def pairwise_complex_cmp(a, b):
    if a == b:
        return 0
    if np_abs(a) == np_abs(b):
        if a.real == b.real:
            return bool_to_cmp(a.imag > b.imag)
        return bool_to_cmp(a.real > b.real)
    return bool_to_cmp(np_abs(a) > np_abs(b))


@given(sensible_floats, sensible_floats)
@example(-1., 1.,)
@example(-2., 2.,)
@example(-3., 3.,)
@example(-4., 4.,)
def test_solve_quadratic_all_real(x_1, x_2):
    A = 1
    B, C = generate_coefficents_from_roots(x_1, x_2)
    assume(all(isfinite([B, C])))
    note("B = {}".format(B))
    note("C = {}".format(C))

    roots = solve_quadratic(A, B, C)
    note("Roots before ordering: [{}, {}]".format(x_1, x_2))
    note("Computed roots before ordering: [{}, {}]".format(*roots))

    # if the roots are not real, then we've likely lost precision when
    # calculating B, which isn't what we're checking for
    assume(all(isreal(roots)))

    assert sorted(roots) == approx(sorted([x_1, x_2]))


@given(sensible_complex)
def test_solve_quadratic_all_complex(x_1):
    if isreal(x_1):
        x_1 = x_1.real
        x_2 = x_1
    else:
        x_2 = conj(x_1)

    A = 1
    B, C = generate_coefficents_from_roots(x_1, x_2)
    assume(all(isreal([B, C])))
    assume(all(isfinite([B, C])))
    note("B = {}".format(B))
    note("C = {}".format(C))

    # Just in case we get complex numbers with 0 imaginary component
    B = B.real
    C = C.real

    roots = solve_quadratic(A, B, C)
    note("Roots before ordering: [{}, {}]".format(x_1, x_2))
    note("Computed roots before ordering: [{}, {}]".format(*roots))

    sorted_out_roots = sorted(roots, key=cmp_to_key(pairwise_complex_cmp))
    sorted_in_roots = sorted(
        [x_1, x_2], key=cmp_to_key(pairwise_complex_cmp)
    )

    assert sorted_out_roots == approx(sorted_in_roots)
