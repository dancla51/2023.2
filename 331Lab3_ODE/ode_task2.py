# import statements
from ode_functions import *

# Lorenz system parameters
func = derivative_lorenz
sigma = 10.
rho = 28.
beta = 8. / 3.
args = [sigma, rho, beta]
atol = 10**-5

t0 = 0
t1 = 40
y0 = np.array([1., 1., 1.])

dp_solver_adaptive_step(func, y0, t0, t1, atol, *args)

