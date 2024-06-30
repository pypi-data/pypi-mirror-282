from functools import cmp_to_key
from operator import itemgetter

from pytest import approx

from hypothesis import given, note, event, assume, example
from hypothesis.strategies import floats, complex_numbers

from numpy import isnan, inf, conj, isreal, abs as np_abs, isfinite, array

from root_solver import solve_cubic, compute_cubic_with_error_estimate
from root_solver._cubic import (
    get_quotients_near_double, get_quotients_near_triple,
)

sensible_floats = floats(allow_nan=False, allow_infinity=False)
sensible_complex = complex_numbers(allow_nan=False, allow_infinity=False)


def generate_coefficents_from_roots(x_1, x_2, x_3):
    x_1, x_2, x_3 = sorted(
        [x_1, x_2, x_3], key=cmp_to_key(pairwise_complex_cmp)
    )
    a = - (x_1 + x_2 + x_3)
    b = x_1 * x_2 + x_3 * (x_1 + x_2)
    c = - x_1 * x_2 * x_3
    return a, b, c


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


def sort_roots(roots, errors):
    return array([
        (root, error) for root, error in sorted(
            zip(roots, errors), key=itemgetter(0)
        )
    ])


@given(sensible_floats, sensible_floats, sensible_floats)
@example(3., 1., 2.)
@example(0, 1., 2.)
@example(-1., -1., -1.)
@example(-1., 1., 1.)
def test_solve_cubic_all_real(x_1, x_2, x_3):
    A = 1
    B, C, D = generate_coefficents_from_roots(x_1, x_2, x_3)
    assume(all(isfinite([B, C, D])))
    note("B = {}".format(B))
    note("C = {}".format(C))
    note("D = {}".format(D))

    note("triple quotients: [{}, {}, {}]".format(*get_quotients_near_triple(
        A, B, C, D
    )))
    note("double quotients: [{}, {}]".format(*get_quotients_near_double(
        A, B, C, D
    )))

    case, roots = solve_cubic(A, B, C, D)
    note("Roots before ordering: [{}, {}, {}]".format(x_1, x_2, x_3))
    note("Computed roots before ordering: [{}, {}, {}]".format(*roots))
    note("Case is {}".format(case))
    event("Case is {}".format(case))

    orig_roots = array([x_1, x_2, x_3])

    Q_orig, Δ_orig = compute_cubic_with_error_estimate(orig_roots, A, B, C, D)
    Q_comp, Δ_comp = compute_cubic_with_error_estimate(roots, A, B, C, D)

    note("Q for original roots: [{}, {}, {}]".format(*Q_orig))
    note("Δ for original roots: [{}, {}, {}]".format(*Δ_orig))
    note("Q for computed roots: [{}, {}, {}]".format(*Q_comp))
    note("Δ for computed roots: [{}, {}, {}]".format(*Δ_comp))

    # If this is not approximately 0, then we've lost too much precision in
    # calculating B, C, D
    assume(Q_orig == approx(array([0, 0, 0])))

    # if the roots are not real, then we've likely lost precision when
    # calculating B or C, which isn't what we're checking for
    assume(all(isreal(roots)))

    # if we've got inf/nan, then we've got overflow and there's not much we can
    # do about it
    # TODO: CHECK THIS, may not be true
    assume(all(isfinite(roots)))

    pairs = sort_roots(roots, Δ_comp)
    sorted_roots = pairs[:, 0]
    sorted_errors = pairs[:, 1]

    for orig_root, comp_root, comp_err in zip(
        sorted(orig_roots), sorted_roots, sorted_errors
    ):
        assert orig_root == approx(comp_root, abs=comp_err)


@given(sensible_floats, sensible_complex)
def test_solve_cubic_all_complex(x_1, x_2):
    if isreal(x_2):
        x_2 = x_2.real
        x_3 = x_2
    else:
        x_3 = conj(x_2)

    A = 1
    B, C, D = generate_coefficents_from_roots(x_1, x_2, x_3)
    assume(all(isreal([B, C, D])))
    assume(all(isfinite([B, C, D])))
    note("B = {}".format(B))
    note("C = {}".format(C))
    note("D = {}".format(D))

    note("triple quotients: [{}, {}, {}]".format(*get_quotients_near_triple(
        A, B, C, D
    )))
    note("double quotients: [{}, {}]".format(*get_quotients_near_double(
        A, B, C, D
    )))

    case, roots = solve_cubic(A, B, C, D)
    note("Given roots before ordering: [{}, {}, {}]".format(x_1, x_2, x_3))
    note("Roots before ordering: [{}, {}, {}]".format(*roots))
    note("Case is {}".format(case))
    event("Case is {}".format(case))

    Q_orig, Δ_orig = compute_cubic_with_error_estimate(
        array([x_1, x_2, x_3]), A, B, C, D
    )
    Q_comp, Δ_comp = compute_cubic_with_error_estimate(roots, A, B, C, D)

    note("Q for computed roots: [{}, {}, {}]".format(*Q_comp))
    note("Δ for computed roots: [{}, {}, {}]".format(*Δ_comp))

    sorted_out_roots = sorted(roots, key=cmp_to_key(pairwise_complex_cmp))
    sorted_in_roots = sorted(
        [x_1, x_2, x_3], key=cmp_to_key(pairwise_complex_cmp)
    )

    assert sorted_out_roots == approx(sorted_in_roots)
