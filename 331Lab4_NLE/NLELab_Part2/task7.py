## Task 7 - Laguerre's Method
import numpy as np
import random
from deflate import deflate
from laguerre import laguerre

# Print formatted polynomial with complex coefficents
def printPolynomial(c):
    n=len(c)-1
    for j in range(n+1):
        if np.imag(c[j])>=0:
            ch='+'
        else:
            ch='-'

        if c[j].real>=0:
            if j>0:
                ch2=' + '
            else:
                ch2='   '
        else:
            ch2=' - '

        if j==0:
            start="The current polynomial is: "
        elif j%3==0:
            print('')
            start="                           "
        else:
            start=""
            
        print(start+f'{ch2:s}({abs(c[j].real):9.3e} {ch:s} {abs(c[j].imag):9.3e}i)x^{n-j:d}',end='')

    print('\n')

# Print formatted complex coefficents
def printRoots(x):
    n=len(x)
    for i in range(n):
        if np.imag(x[i])>=0:
            ch='+'
        else:
            ch='-'
        if abs(x[i].real)<10e-15:
            x[i]=x[i].imag*1j

        if abs(x[i].imag)<10e-15:
            x[i]=x[i].real      
        if i==0:
            start="\nThe roots of the polynomial are: "
        else:
            start="                                 "

        print(start+f'{x[i].real: 9.3e} {ch:s} {abs(x[i].imag):9.3e}i')

# Initialisation
c=[1,1,1,1,1,1,1] # set the coefficients of polynomial in order of decreasing power
tol = 10e-10         # stopping tolerance
max_iter = 100       # maximum number of iterations to find each root
success = True       # status flag

random.seed(12345) # set the random seed

n=len(c) - 1 # number of roots

x=np.zeros(n,dtype = "complex_") # initialise the vector of roots

for i in range(n): # for each root
    # Display current coefficients (after deflation)
    print(f'\nFinding root {i+1:d}')
    printPolynomial(c)

    # Iterate to next root
    x[i], success = laguerre(c, max_iter, tol)

    if not success:
        print('Laguerre\'s method failed')
        break

    # Deflate most recent root
    c, rem = deflate(c, x[i]);
    if abs(rem) > tol:
        print('Non-zero remainder after deflation.')

printRoots(x)

