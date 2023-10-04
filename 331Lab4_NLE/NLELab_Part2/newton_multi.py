import numpy as np
from core import *
from jacobian import jacobian

def newton_multi(n, f, x0, h, max_iter, tol):
    # n = number of dimensions of system
    # h = step size for manual deriv
    x = [x0]
    k = 0
    while True:
        xk = x[k]
        fk = f(xk)
        # Test for convergence
        if max(fk) <= tol and max(-fk) <= tol:
            return x, ExitFlag.Converged
            break
    
        # find jacobian
        jac = jacobian(f, xk, h, n)
        #print("evualting at", xk, "jacobian gets\n", jac)
        delta = np.linalg.solve(jac, fk)

        # Update x
        xnew = xk - delta
        x.append(xnew)

        k+=1
        # Test for max iterations
        if k == max_iter:
            return x, ExitFlag.MaxIterations
            break