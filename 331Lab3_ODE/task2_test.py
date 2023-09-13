
from ode_functions import *



func = derivative_bungy
t0 = 0.
t1 = 50.
h = 0.05
y0 = np.array([0., 2.])  # Jumping 2m/s down
gravity = 9.8
drag = 0.75
gamma = 8.0
mass = 67.0

# Butcher tableau: Classic RK4 explicit method
rk_alpha = np.array([1./6., 1./3., 1./3., 1./6.])
rk_beta = np.array([0., 1./2., 1./2., 1.])
rk_gamma = np.array([[0., 0., 0., 0.], [1./2., 0., 0., 0.], [0., 1./2., 0., 0.], [0., 0., 1., 0.]])

args = [gravity, 16, mass, drag, 50, gamma]
t, y = explicit_solver_fixed_step(func, y0, t0, t1, h, rk_alpha, rk_beta, rk_gamma, *args)
t2, y2 = dp_solver_adaptive_step(func, y0, t0, t1, 10**-5, *args)

# Plot Results
fig, ax = plt.subplots()
ax.plot(t,y[0,:], "-b", linewidth=3)
ax.plot(t2,y2[0,:], ":r", linewidth=6)
ax.invert_yaxis()
plt.show()


