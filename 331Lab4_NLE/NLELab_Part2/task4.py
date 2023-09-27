## Task 4 - System of Nonlinear Equations
from core import *
from newton_multi import newton_multi
from functions2 import f5

# initialisation
tol = 1.0e-6;       # numerical tolerance
h = 1.0e-5;         # step size for central difference
max_iter = 100;     # maximum number of iterations
x0 = [0.8,2]        # initial root estimate

# 2D Newton's method and verification
print(f'Starting at point (x0,y0) = ({x0[0]},{x0[1]})')
xn,exit_flag = newton_multi(2, f5, x0, h, max_iter, tol);
if exit_flag==ExitFlag.Converged:
    print(f'Converged to root at (x,y) = ({xn[-1][0]:9.4e},{xn[-1][1]:9.4e}) in {len(xn)} iterations')
else:
    print(f'Failed to converge: {exit_flag:s}')
