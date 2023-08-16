from core import *
import numpy as np

# Inputs
# f        : nonlinear function
# [a, b]   : initial interval of uncertainty
# max_iter : maximum number of iterations performed
# tol      : requred interval of uncertainty
# showlog  : True to output detailed steps
# Outputs
# [a,b]    : the result, i.e. the final interval of uncertainty
# xlist    : list containing all x values where f(x) was evaluated
# flist    : list containing f(x) for all x in xmin
# k        : number of iterations (number of bisections)
# e        : ExitFlag (enumeration)
def golden(f, ab, max_iter, tol, showlog):
    a,b = ab # Unpack initial interval of uncertainty
    tau = 0.5*(np.sqrt(5) - 1)
    exit_flag = ExitFlag.MaxIterations

    # We start by setting x'=alpha; our first iteration below will end up setting x''=beta
    alpha = a + (1 - tau)*(b - a)
    xd = alpha
    fd = f(xd)

    xlist=[xd]
    flist=[fd]

    for k in range(max_iter):
        ## Your code goes here
        ## Calculate a second point x'' and do the various updates
        ## You should add logging to help you debug and check the code; 
        ## and for diagnosing the algorithm's behaviour
        if xd <= (a+b)/2:
            xdd = a + tau*(b - a)
        else:
            xdd = a + (1 - tau) * (b - a)

        fdd = f(xdd)
        xlist.append(xdd)
        flist.append(fdd)

        # Implement table of possibilities
        if xd <= (a+b)/2:
            logiteration(k, a, xd, xdd, b, fd, fdd, showlog)
            if fdd <= fd:
                # Beta --> Alpha
                a = xd
                xd = xdd
                fd = fdd
            else:
                # Alpha --> Beta
                b = xdd
        else:
            logiteration(k, a, xdd, xd, b, fdd, fd, showlog)
            if fdd <= fd:
                # Alpha --> Beta
                b = xd
                xd = xdd
                fd = fdd
            else:
                # Beta -> Alpha
                a = xdd

        # Test for convergence, break if so.
        if b - a < tol:

            exit_flag = ExitFlag.Converged
            break

    return [a,b], xlist, flist, k, exit_flag

def logiteration(k,a,alpha,beta,b, falpha, fbeta, showlog):
    if showlog:
        print(f'{k:2}: {a:20.15f}{"*" if falpha <= fbeta else " "} {alpha:20.15f}* {beta:20.15}* {b:20.15f}{"*" if falpha > fbeta else " "}')
        print(f'                          {falpha:20.15f}  {fbeta:20.15f}  ')
