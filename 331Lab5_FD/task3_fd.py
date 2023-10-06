# import statements
from functions_fd import *

# define the boundary and initial conditions
x0 = {'type': 'dirichlet', 'function': lambda x, t: 0.}
x1 = {'type': 'dirichlet', 'function': lambda x, t: 0.5}
t0 = {'type': 'initial', 'function': lambda x, t: np.sin(3.*np.pi*x)+0.5*x}
dt0 = {'type': 'initial_derivative', 'function': lambda x, t: 0.}

# TODO: your code below
