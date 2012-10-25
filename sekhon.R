#!/usr/bin/env Rscript

suppressMessages(library(stats))

sekhon.test <- function(a, b, c, d, prob.diff=0.0) {
    f <- function(t) {
        (1 - pbeta(t + prob.diff, a+1, c+1))*dbeta(t, b+1, d+1)
    }
    integrate(f, lower = 0.0, upper=1.0)
}

