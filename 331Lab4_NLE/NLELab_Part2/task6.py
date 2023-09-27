import numpy as np
import time
import random
import matplotlib.pyplot as plt
from scipy import optimize
from multiprocessing import Pool, freeze_support
from functions2 import f8
from newton_multi import newton_multi

## Task 6 - Performance comparision

def main():
    # Initialisation
    tol = 1.0e-8              # numerical tolerance
    h = 1.0e-4                # step size for central difference
    max_iter = 50             # maximum number of iterations
    n = 3   		      # number of variables / equations
    x0_p = []                 # declare initial root estimate dictionary
    t = 10                    # number of random starting points
    func = f8                 # specify the vector of multivariate functions

    random.seed(12345) # set the random seed
    
    # Generate t random starting points
    for i in range(t):
        x0_p.append([random.random()*8-4,random.random()*8-4,random.random()*8-4]) # random starting point

    # Newton's method for function f8, for each starting location
    xn_p=[]
    time1=time.perf_counter()
    for i in range(t):
        x,exit_flag = newton_multi(n, func, x0_p[i], h, max_iter, tol)
    time2=time.perf_counter()
    print(f'Performance of Newton\'s method: {time2-time1}') 
    
    # Using scipy's in-built non-linear equation solver
    time1=time.perf_counter()
    for i in range(t):
        x = optimize.fsolve(func,x0_p[i])
    time2=time.perf_counter()
    print(f'Performance of fsolve: {time2-time1}') 
    time1=time.perf_counter()

    ## Using multithreading pool to solve problems in parallel using newton_method
    with Pool(8) as p:
      output=p.starmap(newton_multi, [(n, func, x0_p[i], h, max_iter, tol) for i in range(t)])

    time2=time.perf_counter()
    print(f'Performance of Netwon\'s method in parallel: {time2-time1}')

if __name__=="__main__":
    freeze_support()
    main()
