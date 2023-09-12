# import statements
from ode_functions import *

# set parameters needed to solve ODE
func = derivative_bungy
t0 = 0
t1 = 50
h = 0.05
y0 = np.array([0., 2.])
gravity = 9.81
drag = 0.75
gamma = 8.0
mass = 67.0

# Butcher tableau: Classic RK4 explicit method
rk_alpha = np.array([1./6., 1./3., 1./3., 1./6.])
rk_beta = np.array([0., 1./2., 1./2., 1.])
rk_gamma = np.array([[0., 0., 0., 0.], [1./2., 0., 0., 0.], [0., 1./2., 0., 0.], [0., 0., 1., 0.]])

# TODO - your code here
# Part 3
args = [gravity, 16, mass, drag, 50, gamma]
t, y = explicit_solver_fixed_step(func, y0, t0, t1, h, rk_alpha, rk_beta, rk_gamma, *args)

# Plot Results
plt.show()
fig, ax = plt.subplots()
ax.plot(t,y[0,:], "-b")
ax.invert_yaxis()
plt.show()


# Part 4



