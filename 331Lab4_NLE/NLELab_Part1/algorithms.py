from core import *


# Nonlinear equation root finding by the bisection method.
# Inputs
# f        : nonlinear function
# xl, xr   : initial root bracket
# max_iter : maximum number of iterations performed
# tol      : numerical tolerance used to check for root
# Outputs
# x        : one-dimensional array containing estimates of root
# i        : number of iterations (number of bisections)
# e        : ExitFlag (enumeration)

# Hint 1: 
# Iterate until either a root has been found or maximum number of iterations has been reached

# Hint 2:
# Check for root each iteration, making use of tol

# Hint 3:
# Update the bracket each iteration

def bisection(f, xl, xr, max_iter, tol):
    x = xl
    fxl = f(xl)

    # check the left side of interval for convergence
    if abs(fxl) <= tol:
        return x, 0, ExitFlag.Converged

    x = [x, xr]

    fxr = f(xr)

    # check the right side of interval for convergence / check that the l/r function values have different signs.
    if abs(fxr) <= tol:
        return x, 0, ExitFlag.Converged
    elif fxl * fxr > 0:
        return x, 0, ExitFlag.NoRoot

    i = 1
    x_carry = x[0]
    while True:
        i += 1

        # compute new estimate appending to x, and evaluate the function value fx
        # Your code goes here #
        newx = (x[-1]+x_carry) / 2

        fx = f(newx)
        if fx*f(x_carry) < 0:
            x_carry = x_carry
        else:
            x_carry = x[-1]

        x.append(newx)

        if abs(fx) <= tol:
            return x, i - 1, ExitFlag.Converged
        elif i - 1 == max_iter:
            return x, i - 1, ExitFlag.MaxIterations

        # update interval
        # Your code goes here #


def secant(f, x0, x1, max_iter, tol):
    # Nonlinear equation root finding by the secant method.
    # Inputs
    # f        : nonlinear function
    # x0, x1   : initial root bracket
    # max_iter : maximum number of iterations performed
    # tol      : numerical tolerance used to check for root
    # Outputs
    # x        : one-dimensional array containing estimates of root
    # k        : number of iterations (number of times a new point is attempted to be estimated)
    # e        : ExitFlag (enumeration)

    x = [x0, x1]
    k = 0










# Nonlinear equation root finding by the Regula falsi method.
# Inputs
# f        : nonlinear function
# xl, xr   : initial root bracket
# max_iter : maximum number of iterations performed
# tol      : numerical tolerance used to check for root
# Outputs
# x        : one-dimensional array containing estimates of root
# i        : number of iterations (number of times a new point is attempted to be estimated)
# e        : ExitFlag (enumeration)

def regula_falsi(f, xl, xr, max_iter, tol):
    return


# Nonlinear equation root finding by Newton's method
# Inputs
# f        : nonlinear function
# g        : nonlinear function derivative (gradient)
# x0       : initial root estimate
# max_iter : maximum number of iterations performed
# tol      : numerical tolerance used to check for root
# Outputs
# x        : one-dimensional array containing estimates of root
# i        : number of iterations (number of times a new point is attempted to be estimated)
# e        : ExitFlag (enumeration)

def newton(f, g, x0, max_iter, tol):
    return


# Nonlinear equation root finding by the combined bisection/Newton's method
# Inputs
# f        : nonlinear function
# g        : nonlinear function derivative (gradient)
# xl, xr   : initial root bracket
# max_iter : maximum number of iterations performed
# tol      : numerical tolerance used to check for root
# Outputs
# x        : one-dimensional array containing estimates of root
# i        : number of iterations (number of times a new point is attempted to be estimated)
# e        : ExitFlag (enumeration)

def combined(f, g, xl, xr, max_iter, tol):
    return
