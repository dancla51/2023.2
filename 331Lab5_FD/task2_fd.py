# import statements
from functions_fd import *

# define the boundary and initial conditions
x0 = {'type': 'dirichlet', 'function': lambda x, t: 200.}
x1 = {'type': 'dirichlet', 'function': lambda x, t: 200.}
t0 = {'type': 'initial', 'function': lambda x, t: np.piecewise(x, [x <= 0., x >= 5., 0. < x < 5.], [200., 200., 30.])}

# set up the x and t dimensions, as well as desired mesh spacing.
xlim = np.array([0., 5.])
tlim = np.array([0., 4.])

# TODO: your code below
