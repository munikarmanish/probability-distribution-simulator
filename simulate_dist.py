#!/usr/bin/env python3

import math
import random
import statistics
import sys
import time

import sample_generators
from helpers import abort, parse_arguments


def print_report(samples):
    samples = list(samples)
    mean = statistics.mean(samples)
    var = statistics.variance(samples)

    samples_str = "["
    for i, x in enumerate(samples):
        if i > 0:
            samples_str += ", "
        if isinstance(x, int):
            samples_str += f"{x}"
        else:
            samples_str += f"{x:.2f}"
    samples_str += "]"

    print(f"samples:\n\t{samples_str}")
    print(f"sample mean:\n\t{mean:.4f}")
    print(f"sample variance:\n\t{var:.4f}")


def main():
    n, dist, params = parse_arguments()

    # random seed
    seed = time.time()
    random.seed(seed)

    try:
        generator = getattr(sample_generators, f"generate_{dist}_samples")
        samples = generator(n, params)
    except KeyError:
        abort("distribution not recognized")

    print_report(samples)


if __name__ == "__main__":
    main()
