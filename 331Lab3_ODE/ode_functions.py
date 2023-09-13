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
    # Dormand prince values
    alpha = np.array([35/384, 0, 500/1113, 125/192, -2187/6784, 11/84, 0])
    alphastar = np.array([5179/57600, 0, 7571/16695, 393/640, -92097/339200, 187/2100, 1/40])
    beta = np.array([0, 1/5, 3/10, 4/5, 8/9, 1, 1])
    gamma = np.array([ [0,0,0,0,0,0,0], [1/5,0,0,0,0,0,0], [3/40,9/40,0,0,0,0,0],
                       [44/45,-56/15,32/9,0,0,0,0],
                       [19372/6561,-25360/2187,64448/6561,-212/729,0,0,0],
                       [9017/3168,-355/33,46732/5247,49/176,-5103/18656,0,0],
                       [35/384,0,500/1113,125/192,-2187/6784,11/84,0] ])

    # Setup initial values
    yheight = len(y0)
    t_cur = t0
    y_cur = y0
    t = np.array(t_cur)
    y = np.zeros([yheight, 1])
    y[:, 0] = y_cur

    # Initial stepsize
    h = 10**-3
    sf = 0.9

    while t_cur < t1:
                        # use    y = np.append(y, y_new, axis=1)
        # until successful iteration
        success=False
        while success == False:
            # Do function calls
            fs = np.zeros([yheight, 7])
            for i in range(7):
                fs
                # Calc sum of gammaij * fj
                fjs = np.zeros(yheight)
                for j in range(i):
                    fjs += gamma[i, j] * fs[:, j]

                fs[:, i] = func(t_cur + h * beta[i], y_cur + h * fjs, *args)

            # Error comparison
            y_p1 = np.copy(y_cur)
            y_p2 = np.copy(y_cur)
            for i in range(7):
                y_p1 += h * alpha[i] * fs[:, i]
                y_p2 += h * alphastar[i] * fs[:, i]

            err = np.mean(abs(y_p1-y_p2))       # Using mean absolute error
            if err <= atol:
                success = True
                t_cur += h
                y_cur = y_p2
                t=np.append(t, t_cur)
                y = np.append(y, y_cur.reshape((yheight,1)), axis=1)
                h = sf * h * (atol/err)**0.2
                #print("successful timestep, h_new is:",h)
            else:
                success = False
                h = sf * h * (atol / err) ** (1/6)
                #print("unsuccessful timestep, h_new is:", h)

    return t, y

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
    dydt = np.array([0., 0., 0.])
    dydt[0] = sigma * (y[1] - y[0])
    dydt[1] = y[0] * (rho - y[2]) - y[1]
    dydt[2] = y[0] * y[1] - beta * y[2]

    return dydt


# Test Solver with Improved Euler Method and RK4
if __name__ == "__main__":
    func = derivative_bungy
    t0 = 0
    y0 = np.array([0, 2])
    t1 = 50
    h = 0.35
    alpha = np.array([0.5, 0.5])
    beta = np.array([0, 1])
    gamma = np.array([[0, 0], [1, 0]])
    #args = [9.8, 16, 67, 0.75, 50, 8]    # Short50
    args = [10, 20, 50, 1, 50, 8]    # test
    # gravity, length, mass, drag, spring, gamma

    t_ie, y_ie = explicit_solver_fixed_step(func, y0, t0, t1, h, alpha, beta, gamma, *args)
    # RK4
    alpha = np.array([1/6, 1/3, 1/3, 1/6])
    beta = np.array([0, 0.5, 0.5, 1])
    gamma = np.array([[0, 0, 0, 0], [0.5, 0, 0, 0], [0, 0.5, 0, 0], [0, 0, 1, 0]])
    t_rk4, y_rk4 = explicit_solver_fixed_step(func, y0, t0, t1, h, alpha, beta, gamma, *args)

    # Plot
    fig, ax = plt.subplots()
    ax.plot(t_ie,y_ie[0,:], "-r", label="improved euler")
    ax.plot(t_rk4,y_rk4[0,:], ":b", label="rk4")
    ax.invert_yaxis()
    plt.legend()
    plt.show()

