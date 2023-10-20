# import statements
from functions_fd import *

# define the boundary and initial conditions
bc_x0 = {'type': 'dirichlet', 'function': lambda x, t: 200.}
bc_x1 = {'type': 'dirichlet', 'function': lambda x, t: 200.}
ic_t0 = {'type': 'initial', 'function': lambda x, t: np.piecewise(x, [x <= 0., x >= 5., 0. < x < 5.], [200., 200., 30.])}

# set up the x and t dimensions, as well as desired mesh spacing.
xlim = np.array([0., 5.])
tlim = np.array([0., 4.])
dx = 0.05
dt = 0.01

alpha = 1
theta = 0.5

solver3 = SolverHeatXT(xlim, tlim, dx, dt, alpha, theta, bc_x0, bc_x1, ic_t0)
solver3.solve_implicit()
solver3.plot_solution()