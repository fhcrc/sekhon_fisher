# Sekhon Fisher Test

A principled Bayesian contingency table test.

## Background

Fisher's exact test is often considered the gold standard for testing the statistical significance of contingency tables in cases of small sample sizes. However, the test conditions on the marginals being fixed (such as the classic "Lady Tasting Tea", where the lady knows the number of teas in each category), and as such is not appropriate for situations where one is comparing two binomial distributions. In addition, simulations have demonstrated that in practice the test often performs poorly[1].

Jasjeet Sekhon proposed a Bayesian alternative to Fisher's exact test which avoids these issues. This software is an implementation of his beta difference distribution solution. Primarily, this is a python module, but I have thrown in an R implementation as well.

## Python

### Building

If you have python installed, you should be able to download this source and use `python setup.py install` to install the module within your python environment.

### CLI

Building this module and installing to your python distribution should give you access to the `sekhon.py` CLU. For usage, type `sekhon.py -h`.

### Module

Sample usage:

    import sekhon
    
    # Simple test of table [[a, c], [b, d]]
    sekhon.test(a, b, c, d)

    # Specify 10,000,000 samples and test the probability that `P1 - P2 > prob_diff`
    sekhon.test(a, b, c, d, prob_diff=0.05)

Additionally, if you are feeling playful, you can toy around with an early sampling solution using the `simulation` and `simulation_convergence_test` functions.


## R

For now Copy-Paste from `sekhon_fisher.R`. If there is enough demand, I can throw together a little R package though.


## References

[1] Jasjeet S. Sekhon, 2005 "Making Inferences from 2×2 Tables: The Inadequacy of the Fisher Exact Test for Observational Data and a Principled Bayesian Alternative"

