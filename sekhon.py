#!/usr/bin/env python

import random
import time
import scipy


__version__ = "0.0.1"


def sekhon2(a, b, c, d, n=10000, tolerance=0.0):
    samples = []
    for i in xrange(0, n):
        samples.append((random.betavariate(a+1, b+1), 1))
        samples.append((random.betavariate(c+1, d+1) + tolerance, 2))

    samples.sort()
    count = 0
    total = 0
    for sample in samples:
        if sample[1] == 2:
            count += 1
        else:
            total += count

    return float(total)/n**2


def sekhon(a, b, c, d, samples=10000, tolerance=0.0, significance_level=0.95,
        ensure_convergence=True, ensure_samples=1000000, ensure_radius=0.007):
    successes = 0.0
    for i in xrange(0, samples):
        successes += random.betavariate(a + 1, b + 1) - random.betavariate(c + 1, d + 1) > tolerance

    result = successes / samples

    if ensure_convergence and abs(result - significance_level) < ensure_radius:
        result = sekhon(a, b, c, d, samples=ensure_samples, tolerance=tolerance, ensure_convergence=False)

    return result


def convergence_test(test, samples, trials):
    t0 = time.time()
    results = []
    for i in xrange(0, trials):
        results.append(test(8, 250, 3, 250, samples))

    t1 = time.time()

    print "Mean:", scipy.mean(results)
    print "Std Dev:", scipy.std(results)
    print "Range:", max(results) - min(results)
    print "Time:", t1 - t0, "\n"


def cli():
    import argparse
    parser = argparse.ArgumentParser(description=
            "Sekhon Fisher test for table [[a,c],[b,d]]")

    parser.add_argument('a', type=int, help='# sucesses in X1')
    parser.add_argument('b', type=int, help='# failures in X1')
    parser.add_argument('c', type=int, help='# sucesses in X2')
    parser.add_argument('d', type=int, help='# failures in X2')

    parser.add_argument('--samples', type=int, default=10000, help='Number of samples to take')
    parser.add_argument('--tolerance', type=float, default=0.0, help='Test that P1 - P2 > tolerance')

    args = parser.parse_args()


    a, b, c, d = [getattr(args, x) for x in ['a', 'b', 'c', 'd']]

    t0 = time.time()
    result = sekhon(a, b, c, d, samples=args.samples, tolerance=args.tolerance)
    t1 = time.time()

    print "Ran", args.samples, "simulations in", t1 - t0, "seconds"
    print "Result is:", result


if __name__ == '__main__':
    sekhon2(8, 250, 3, 250, 2000000)

