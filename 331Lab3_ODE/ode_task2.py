# import statements
from ode_functions import *

# Part 3


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

t, y = dp_solver_adaptive_step(func, y0, t0, t1, atol, *args)


# Part 4

plt.plot(y[0],y[2])
plt.title("Phase plot of lorenz system in xz-plane")
plt.xlabel("x")
plt.ylabel("z")
plt.show()


# Part 5

# Timeseries plots
for i in range(3):
    letter = chr(i+120)
    plt.plot(t, y[i])
    plt.title("Timeseries plot of lorenz system, "+letter+"(t)")
    plt.xlabel("t")
    plt.ylabel(letter)
    plt.show()

# No, I do not expect the system to settle down into a steady state long-term, because it is
# a chaotic system. Systems that exhibit chaotic behaviour do not tend to converge to steady
# state solutions, and will instead bounce around in an unexpected manner, never reaching
# a steady state.


# Part 6
y02 = np.array([1.001, 1.001, 1.001])

t2, y2 = dp_solver_adaptive_step(func, y02, t0, t1, atol, *args)

plt.plot(y[0],y[2], label="y0=[1,1,1]")
plt.plot(y2[0],y2[2], ":", label="y0=[1.001,1.001,1.001]")
plt.title("Phase plot of lorenz systems in xz-plane by initial y")
plt.xlabel("x")
plt.ylabel("z")
plt.legend()
plt.show()

for i in range(3):
    letter = chr(i+120)
    plt.plot(t, y[i], label="y0=[1,1,1]")
    plt.plot(t2, y2[i], ":", label="y0=[1.001,1.001,1.001]")
    plt.title("Timeseries plot of lorenz systems by initial y, "+letter+"(t)")
    plt.xlabel("t")
    plt.ylabel(letter)
    plt.show()

# The plots from step 6 show that a very slight change in starting condition can
# give drastically different results after a period of time. This means that any
# numerical error that is introduced by our numerical solvers will become compounded
# over time. AKA it will be highly sensitive to the numerical accuracy of our
# solution method. Therefore we cannot expect to accurately predict the exact values
# for x, y, and z at times that are far into the future, for a chaotic system like
# this.
