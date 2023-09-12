# import statements
import numpy as np
from matplotlib import pyplot as plt


def explicit_solver_fixed_step(func, y0, t0, t1, h, alpha, beta, gamma, *args):
    """
    Compute solution(s) to ODE(s) using any explicit RK method with fixed step size.

    Args:
        func (callable): derivative function that returns an ndarray of derivative values.
        y0 (ndarray): initial condition(s) for dependent variable(s).
        t0 (float): start value of independent variable.
        t1 (float):	stop value of independent variable.
        h (float): fixed step size along independent variable.
        alpha (ndarray): weights in the Butcher tableau.
        beta (ndarray): nodes in the Butcher tableau.
        gamma (ndarray): RK matrix in the Butcher tableau.
        *args : optional system parameters to pass to derivative function.

    Returns:
        t (ndarray): independent variable values at which dependent variable(s) calculated.
        y (ndarray): dependent variable(s) solved at t values.
    """
    tabsize = len(alpha)

    t = np.arange(t0, t1+h, h)
    yheight = len(y0)
    ywidth = len(t)
    y = np.zeros([yheight, ywidth])   # yk = y[:,k]
    y[:,0] = y0

    # k is iteration
    for k in range(len(t)-1):
        # Calculate functions evaluations
        fs = np.zeros([yheight, tabsize])
        for i in range(tabsize):

            # Calc sum of gammaij * fj
            fjs=np.zeros(yheight)
            for j in range(i):
                fjs += gamma[i,j] * fs[:,j]
            fs[:,i] = func(t[k] + h*beta[i], y[:,k] + h*fjs, *args)

        y_next = np.copy(y[:,k])
        for i in range(tabsize):
            y_next += h*alpha[i] * fs[:,i]

        y[:,k+1] = np.array(y_next)

    return (t, y)


def dp_solver_adaptive_step(func, y0, t0, t1, atol, *args):
    """
    Compute solution to ODE using the Dormand-Prince embedded RK method with an adaptive step size.

    Args:
        func (callable): derivative function that returns an ndarray of derivative values.
        y0 (ndarray): initial conditions for each solution variable.
        t0 (float): start value of independent variable.
        t1 (float):	stop value of independent variable.
        atol (float): error tolerance for determining adaptive step size.
        *args : optional system parameters to pass to derivative function.

    Returns:
        t (ndarray): independent variable values at which dependent variable(s) calculated.
        y (ndarray): dependent variable(s).
    """
    pass


def derivative_bungy(t, y, gravity, length, mass, drag, spring, gamma):
    """
    Compute the derivatives of the bungy jumper motion.

    Args:
        t (float): independent variable, time (s).
        y (ndarray): y[0] = vertical displacement (m), y[1] = vertical velocity (m/s).
        gravity (float): gravitational acceleration (m/s^2).
        length (float):	length of the bungy cord (m).
        mass (float): the bungy jumper's mass (m).
        drag (float): coefficient of drag (kg/m).
        spring (float): spring constant of the bungy cord (N/m).
        gamma (float): coefficient of damping (Ns/m).

    Returns:
        f (ndarray): derivatives of vertical position and vertical velocity.
    """
    f = np.zeros(2)
    f[0]=y[1]
    if y[0]<length:
        f[1] = gravity - np.sign(y[1]) * drag * y[1] ** 2 / mass
    else:
        f[1] = gravity - np.sign(y[1]) * drag * y[1]**2 / mass - spring/mass*(y[0]-length) - gamma*y[1]/mass

    return f



def derivative_lorenz(t, y, sigma, rho, beta):
    """
    Compute the derivatives for the Lorenz system.

    Args:
        t (float): independent variable, time.
        y (ndarray): dependent variables x, y and z in Lorenz system.
        sigma (float): system parameter of Lorenz system.
        rho (float): system parameter of Lorenz system.
        beta (float): system parameter of Lorenz system.

    Returns:
        f (ndarray): derivatives of x, y and z in Lorenz system.
    """
    pass


# Test Solver with Improved Euler Method
if __name__ == "__main__":
    func = derivative_bungy
    t0 = 0
    y0 = np.array([0, 1])
    t1 = 1
    h = 1
    alpha = np.array([0.5, 0.5])
    beta = np.array([0, 1])
    gamma = np.array([[0, 0], [1, 0]])
    #args = [9.8, 16, 67, 0.75, 50, 8]    #Short50
    args = [10, 20, 50, 1, 50, 8]    #Short50
    # gravity, length, mass, drag, spring, gamma

    t, y = explicit_solver_fixed_step(func, y0, t0, t1, h, alpha, beta, gamma, *args)

    print(t, "\n", y)

    # Plot
    fig, ax = plt.subplots()
    ax.plot(t,y[0,:], "-r")
    ax.invert_yaxis()
    plt.show()

