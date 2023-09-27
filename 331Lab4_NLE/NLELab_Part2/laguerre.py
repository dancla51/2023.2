import numpy as np
import random
from horner import horner
# [x, success]=Laguerre(c,tol) finds a root of the polynomial x using Laguerre's
# method, also indicates the success/failure with logical variable success.
# Inputs
# c        : The coefficients of the polynomial from the highest order to the lowest
# max_iter : The maximum number of iterations
# tol      : The residual test toleration
# Outputs
# x        : The root that has been found (as a complex number)
# success  : True / False, return True if the root is found and false otherwise
def laguerre(c, max_iter, tol):
    x = complex(random.random(), random.random()) # Initial random iterate

    # Polynomial degree (highest power)
    n = len(c) - 1;

    print('it    re(x)          im(x)       |p(x)|   |p\'(x)|  |p\'\'(x)|    |step|')
    # -----12-(123456789,-123456789)-123456789-123456789.-123456789..-123456789--

    success = False
    for it in range(max_iter):
        # Evaluate the polynomial
        [p, dp, ddp] = horner(c, x)
    
        if np.imag(x)<0:
            ch='-'
        else:
            ch='+'

        output = f'{it:2d} {np.real(x):9.4f}    {ch:s} {abs(np.imag(x)):9.4f}i  {abs(p):9.4f} {abs(dp):9.3f} {abs(ddp):9.3f}'
        
        # Check for root before division, below, by polynomial's value
        if abs(p) <= tol:
            print(output)
            success = True
            break
    
        ## Your code goes here

        # find alpha

        # divide-by-zero is possible, if it encounters this then choose a random (complex) point from which to start the next iteration
        
        # compute the new root estimate
    
        print(output+f' {abs(alpha):9.3f}')

    return x, success