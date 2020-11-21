import math
import random


def bernoulli(p):
    return int(random.random() < p)


def binomial(n, p):
    return sum([bernoulli(p) for _ in range(n)])


def geometric(p):
    count = 1
    while True:
        if bernoulli(p) == 1:
            return count
        count += 1


def neg_binomial(k, p):
    return sum([geometric(p) for _ in range(k)])


def poisson(L):
    thres = math.exp(-L)
    u = 1.0
    k = 0
    while True:
        u *= random.random()
        if u < thres:
            return k
        k += 1


def arb_discrete(probs):
    u = random.random()
    cdf = 0
    for i, prob in enumerate(probs):
        cdf += prob
        if cdf > u:
            return i


def uniform(a, b):
    return a + random.random() * (b - a)


def exponential(L):
    u = random.random()
    return -math.log(1 - u) / L


def gamma(a, L):
    return sum([exponential(L) for _ in range(a)])


def normal(u, s):
    u1, u2 = random.random(), random.random()
    A = -2 * math.log(u1)
    B = 2 * math.pi * u2
    z1 = math.sqrt(A) * math.cos(B)
    z2 = math.sqrt(A) * math.sin(B)
    return u + s * z1, u + s * z2
