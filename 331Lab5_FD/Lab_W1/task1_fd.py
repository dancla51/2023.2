# import statements
from functions_fd import *


# define the Poisson function
def poisson(x, y):
    return x - y


# set up the x and y dimensions.
xlim = np.array([-2., 2.])
ylim = np.array([-3., 3.])

# set up the boundary conditions
bc_x0 = {'type': 'neumann', 'function': lambda x, y: x}
bc_x1 = {'type': 'neumann', 'function': lambda x, y: y}
bc_y0 = {'type': 'dirichlet', 'function': lambda x, y: x * y}
bc_y1 = {'type': 'dirichlet', 'function': lambda x, y: x * y - 1.}

# create an object of SolverPoissonXY and then solve it
solver1 = SolverPoissonXY(xlim, ylim, 2., bc_x0, bc_x1, bc_y0, bc_y1, poisson)

# TODO: your code below
