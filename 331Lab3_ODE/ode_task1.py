# import statements
from ode_functions import *


plotPt3=False
plotPt5=False
plotPt6=True


# set parameters needed to solve ODE
func = derivative_bungy
t0 = 0
t1 = 50
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

# TODO - your code here
# Part 3
args = [gravity, 16, mass, drag, 50, gamma]
t, y = explicit_solver_fixed_step(func, y0, t0, t1, h, rk_alpha, rk_beta, rk_gamma, *args)

# Plot Results
if plotPt3:
    plt.show()
    fig, ax = plt.subplots()
    ax.plot(t,y[0,:], "-b")
    ax.invert_yaxis()
    plt.show()


# Part 4

max_disp = np.zeros([2, 6])
# Each rope
for i, length in enumerate(range(16, 26, 5)):     # 16 = Short, 21 = Reg
    for j, spring in enumerate(range(50, 110, 10)):
        args = [gravity, length, mass, drag, spring, gamma]
        t, y = explicit_solver_fixed_step(func, y0, t0, t1, h, rk_alpha, rk_beta, rk_gamma, *args)
        max_disp[i,j] = max(y[0])

print(max_disp)


# Part 5
if plotPt5:
    # Add some text for labels, title and custom x-axis tick labels, etc.
    plt.bar(np.arange(48, 108, 10), max_disp[0], width=4, label="Short Bungy Cord")
    plt.bar(np.arange(52, 112, 10), max_disp[1], width=4, label="Regular Bungy Cord")
    plt.plot([45, 105], [44.8, 44.8], '-.k', label="Full Dunk")
    plt.plot([45, 105], [43, 43], ':k', label="Partial Dunk")
    plt.legend()
    plt.ylim(0, 63)
    plt.xlabel("Stiffness of Bungy Cord [N/m]")
    plt.ylabel("Maximum Bungy Jump Depth [m]")
    plt.title("Maximum Bungy Jump Depth by Cord length and stiffness")
    plt.show()


# Task 6


# The Bungy cords that will fully dunk the engineering student are the Reg50 and Reg60
# cords. I will choose to use the Reg60 cord as it dunks the engineering student for
# the least amount of time, so is the safer option of the two.
length = 21
spring = 60
args = [gravity, length, mass, drag, spring, gamma]
t_reg60, y_reg60 = explicit_solver_fixed_step(func, y0, t0, t1, h, rk_alpha, rk_beta, rk_gamma, *args)

if plotPt6:
    # Displacement and Velocity vs time
    fig, ax1 = plt.subplots()
    ax1.set_xlabel('time [s]')
    ax1.set_ylabel('Displacement [m]', color="blue")
    ax1.plot(t_reg60, y_reg60[0], color="blue")
    ax2 = ax1.twinx()
    ax2.set_ylabel('Velocity [m/s]', color="green")
    ax2.plot(t_reg60, y_reg60[1], color="green")
    ax1.invert_yaxis()
    ax2.invert_yaxis()
    ax1.set_title("Displacement and Velocity vs Time of Reg60 Bungy")
    plt.show()
    # Phase Plot
    plt.plot(y_reg60[0], y_reg60[1])
    plt.xlabel("Displacement [m]")
    plt.ylabel("Velocity [m/s]")
    plt.title("Phase Plot of Reg60 Bungy")
    plt.show()

