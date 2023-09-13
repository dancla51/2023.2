# import statements
from ode_functions import *

# Lorenz system parameters
sigma = 10.
rho = 28.
beta = 8. / 3.

print(derivative_lorenz(0, np.array([1., 2., 5.]), sigma, rho, beta))
# TODO - your code here
