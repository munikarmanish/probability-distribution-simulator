import math

from distributions import (
    arb_discrete,
    bernoulli,
    binomial,
    exponential,
    gamma,
    geometric,
    neg_binomial,
    normal,
    poisson,
    uniform,
)
from helpers import abort


def generate_bernoulli_samples(n, params):
    try:
        assert len(params) == 1
        p = float(params[0])
        assert 0 <= p <= 1
    except (ValueError, AssertionError):
        abort("invalid bernoulli parameters")

    for _ in range(n):
        yield bernoulli(p)


def generate_binomial_samples(n, params):
    try:
        assert len(params) == 2
        N = int(params[0])
        p = float(params[1])
        assert N >= 1
        assert 0 <= p <= 1
    except (ValueError, AssertionError):
        abort("invalid binomial parameters")

    for _ in range(n):
        yield binomial(N, p)


def generate_geometric_samples(n, params):
    try:
        assert len(params) == 1
        p = float(params[0])
        assert 0 <= p <= 1
    except (ValueError, AssertionError):
        abort("invalid geometric parameters")

    for _ in range(n):
        yield geometric(p)


def generate_neg_binomial_samples(n, params):
    try:
        assert len(params) == 2
        k = int(params[0])
        p = float(params[1])
        assert k >= 1
        assert 0 <= p <= 1
    except (ValueError, AssertionError):
        abort("invalid neg_binomial parameters")

    for _ in range(n):
        yield neg_binomial(k, p)


def generate_poisson_samples(n, params):
    try:
        assert len(params) == 1
        L = float(params[0])
        assert L > 0
    except (ValueError, AssertionError):
        abort("invalid poisson parameters")

    for _ in range(n):
        yield poisson(L)


def generate_arb_discrete_samples(n, params):
    try:
        assert len(params) >= 1
        probs = [float(p) for p in params]
        assert math.isclose(sum(probs), 1.0, abs_tol=0.001)
    except (ValueError, AssertionError):
        abort("invalid arb_discrete parameters")

    for _ in range(n):
        yield arb_discrete(probs)


def generate_uniform_samples(n, params):
    try:
        assert len(params) == 2
        a = float(params[0])
        b = float(params[1])
        assert a <= b
    except (ValueError, AssertionError):
        abort("invalid uniform parameters")

    for _ in range(n):
        yield uniform(a, b)


def generate_exponential_samples(n, params):
    try:
        assert len(params) == 1
        L = float(params[0])
        assert L > 0
    except (ValueError, AssertionError):
        abort("invalid exponential parameters")

    for _ in range(n):
        yield exponential(L)


def generate_gamma_samples(n, params):
    try:
        assert len(params) == 2
        a = int(params[0])
        L = float(params[1])
        assert a >= 1
        assert L > 0
    except (ValueError, AssertionError):
        abort("invalid gamma parameters")

    for _ in range(n):
        yield gamma(a, L)


def generate_normal_samples(n, params):
    try:
        assert len(params) == 2
        u = float(params[0])
        s = float(params[1])
        assert s >= 0
    except (ValueError, AssertionError):
        abort("invalid normal parameters")

    count = 0
    while count < n:
        for x in normal(u, s):
            yield x
            count += 1
