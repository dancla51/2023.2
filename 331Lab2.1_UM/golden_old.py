from core import *
import numpy as np


# Inputs
# f        : nonlinear function
# [a, b]   : initial interval of uncertainty
# max_iter : maximum number of iterations performed
# tol      : required interval of uncertainty
# showlog  : True to output detailed steps
# Outputs
# [a,b]    : the result, i.e. the final interval of uncertainty
# xlist    : list containing all x values where f(x) was evaluated
# flist    : list containing f(x) for all x in xmin
# k        : number of iterations (number of bisections)
# e        : ExitFlag (enumeration)
def golden(f, ab, max_iter, tol, showlog):
    a, b = ab  # Unpack initial interval of uncertainty
    tau = 0.5 * (np.sqrt(5) - 1)
    exit_flag = ExitFlag.MaxIterations

    # I set both alpha and beta for the initial iteration

    for k in range(max_iter):
        # Log
        logiteration(k, a, alpha, beta, b, falpha, fbeta, showlog)

        # Test for convergence, break if so.
        if b - a < tol:
            max_iter = k+1
            exit_flag = ExitFlag.Converged
            break
    print(xlist)
    print(flist)

    return [a, b], xlist, flist, max_iter, exit_flag


def logiteration(k, a, alpha, beta, b, falpha, fbeta, showlog):
    if showlog:
        print(
            f'{k:2}: {a:20.15f}{"*" if falpha <= fbeta else " "} {alpha:20.15f}* {beta:20.15}* {b:20.15f}{"*" if falpha > fbeta else " "}')
        print(f'                          {falpha:20.15f}  {fbeta:20.15f}  ')
