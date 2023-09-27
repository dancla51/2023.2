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
    k = 1

    while True:
        # New x value
        xnew = x[k] - (x[k]-x[k-1]) * f(x[k]) / (f(x[k]) - f(x[k-1]))
        x.append(xnew)
        # Test
        if x[-1] < x0 or x[-1] > x1:
            return x, k, ExitFlag.NoRoot
        elif abs(f(x[-1])) < tol:
            return x, k, ExitFlag.Converged
        elif k - 1 == max_iter:
            return x, k, ExitFlag.MaxIterations
        # Iterate
        k += 1




def regula_falsi(f, xl, xr, max_iter, tol):
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
    x = [xl, xr]
    k = 1

    while True:
        # New x value and update bracket
        xnew = (xl * f(xr) - xr * f(xl)) / (f(xr) - f(xl))
        if f(xnew)*f(xr) > 0:
            xr = xnew
        else:
            xl = xnew
        x.append(xnew)
        # Test
        if x[-1] < xl or x[-1] > xr:
            return x, k, ExitFlag.NoRoot
        elif abs(f(x[-1])) < tol:
            return x, k, ExitFlag.Converged
        elif k - 1 == max_iter:
            return x, k, ExitFlag.MaxIterations
        # Iterate
        k += 1


def newton(f, g, x0, max_iter, tol):
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
    x = [x0]
    k = 0
    while True:
        xnew = x[k] - f(x[k]) / g(x[k])
        x.append(xnew)

        if abs(f(x[-1])) < tol:
            return x, k, ExitFlag.Converged
        elif k == max_iter:
            return x, k, ExitFlag.MaxIterations

        k += 1




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
