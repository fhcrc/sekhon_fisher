# Sekhon Fisher Test

A principled contingency table test.

## Background

Fisher's exact test is often considered the gold standard for testing the statistical significance of contingency tables in cases of small sample sizes. However, the test conditions on the marginals being fixed (such as the classic "Lady Tasting Tea", where the lady knows the number of teas in each category), and as such is not appropriate for situations where one is comparing two binomial distributions. In addition, simulations have demonstrated that in practice the test often performs poorly[1].

Jasjeet Sekhon proposed a Bayesian alternative to Fisher's exact test which avoids these issues. This software is an implementation of his difference of beta distributions which employs sampling.

## Building

If you have python installed, you should be able to download this source and use `python setup.py install` to install the module within your python environment. This will give you a command line interface (`sekhon.py -h` for usage) and a module for importing in python code.

## Module

Sample usage:

    import sekhon
    
    # Simple test
    sekhon.test(a, b, c, d)

    # Specify 10,000,000 samples and test the probability that `P1 - P2 > prob_diff`
    sekhon.test(a, b, c, d, samples=10000000, prob_diff=0.05)

    # Test the convergance at a specified number of samples and trails (1000 and 15, resp.):
    sekhon.convergence_test(1000, 15)


Additionally, you can specify `ensure_samples`, `ensure_radius`, and `ensure_convergence` and
`significance_level` if you would like to make sure that the test is converging at some significance level.


## References

[1] Jasjeet S. Sekhon, 2005 "Making Inferences from 2×2 Tables: The Inadequacy of the Fisher Exact Test for Observational Data and a Principled Bayesian Alternative"

