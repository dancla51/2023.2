import numpy as np
from core import *
from jacobian import jacobian

def newton_multi(n, f, x0, h, max_iter, tol):
    x = [x0]
    k = 0
    while True:
        xk = x[k]
        fk = f(xk)

        if max(fk) <= tol and max(-fk) <= tol:
            return x, ExitFlag.Converged
            break
    
        ## Your code goes here

        # You'll need to use np.linalg.det and np.linalg.solve
        
        k+=1
        if k == max_iter:
            return x, ExitFlag.MaxIterations
            break