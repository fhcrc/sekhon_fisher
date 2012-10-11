#!/usr/bin/env python
from __future__ import division
from scipy.stats import beta
import time
import scipy


__version__ = "0.0.1"

def test(a, b, c, d, samples=100000, prob_diff=0.0, significance_level=0.95,
        ensure_convergence=False, ensure_samples=10000000, ensure_radius=0.005):
    difference = beta.rvs(a + 1, b + 1, size=samples) - beta.rvs(c + 1, d + 1, size=samples)
    successes = (difference > prob_diff).sum()

    result = successes / samples

    if ensure_convergence and abs(result - significance_level) < ensure_radius:
        result = test(a, b, c, d, samples=ensure_samples, prob_diff=prob_diff, ensure_convergence=False)

    return result


def convergence_test(samples, trials):
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
            """Sekhon Fisher test for table [[a,c],[b,d]]. See
            "Making Inferences from 2x2 Tables: The Inadequacy of the Fisher Exact Test
            for Observational Data and a Principled Bayesian Alternative" by
            Jasjeet S. Sekhon, 2005""")

    parser.add_argument('a', type=int, help='# sucesses in X1')
    parser.add_argument('b', type=int, help='# failures in X1')
    parser.add_argument('c', type=int, help='# sucesses in X2')
    parser.add_argument('d', type=int, help='# failures in X2')

    parser.add_argument('--samples', type=int, default=10000, help='Number of samples to take')
    parser.add_argument('--prob_diff', type=float, default=0.0, help='Test that P1 - P2 > prob_diff')

    args = parser.parse_args()


    a, b, c, d = [getattr(args, x) for x in ['a', 'b', 'c', 'd']]

    t0 = time.time()
    result = test(a, b, c, d, samples=args.samples, prob_diff=args.prob_diff)
    t1 = time.time()

    print "Ran", args.samples, "simulations in", t1 - t0, "seconds"
    print "Result is:", result


if __name__ == '__main__':
    cli()

