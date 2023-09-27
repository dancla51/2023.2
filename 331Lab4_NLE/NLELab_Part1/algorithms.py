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
    x = [x, xr]
    fxr = f(xr)
    # check the left side of interval for convergence
    if abs(fxl) <= tol:
        return [xl], 0, ExitFlag.Converged

    # check the right side of interval for convergence / check that the l/r function values have different signs.
    if abs(fxr) <= tol:
        return x, 0, ExitFlag.Converged
    elif fxl * fxr > 0:
        return x, 0, ExitFlag.NoRoot

    i = 1
    x_carry = x[0]
    f_carry = f(x[0])
    while True:
        i += 1

        # compute new estimate appending to x, and evaluate the function value fx
        # Your code goes here #
        newx = (x[-1]+x_carry) / 2

        fx = f(newx)
        if fx*f_carry > 0:
            x_carry = x[-1]
            f_carry = f(x_carry)

        x.append(newx)

        if abs(fx) <= tol:
            return x, i - 1, ExitFlag.Converged
        elif i - 1 == max_iter:
            return x, i - 1, ExitFlag.MaxIterations


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

    # Set up values
    x = [x0, x1]
    k = 1
    f_carry = f(x1)
    f_double_carry = f(x0)

    while True:
        # New x value
        xnew = x[k] - (x[k]-x[k-1]) * f_carry / (f_carry - f_double_carry)
        x.append(xnew)
        # Carry over function evals for efficiency
        f_double_carry = f_carry
        f_carry = f(xnew)
        # Tests and returns if successful
        if x[-1] < x0 or x[-1] > x1:
            return x, k, ExitFlag.NoRoot
        elif abs(f_carry) < tol:
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
    fxl = f(xl)
    fxr = f(xr)

    while True:
        # New x value and update bracket
        xnew = (xl * fxr - xr * fxl) / (fxr - fxl)
        fxnew = f(xnew)
        if fxnew*fxr > 0:
            xr = xnew
            fxr = fxnew
        else:
            xl = xnew
            fxl = fxnew
        x.append(xnew)
        # Test
        if x[-1] < xl or x[-1] > xr:
            return x, k, ExitFlag.NoRoot
        elif abs(fxnew) < tol:
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
    f_carry = f(x0)
    while True:
        xnew = x[k] - f_carry / g(x[k])
        x.append(xnew)
        f_carry = f(xnew)
        if abs(f_carry) < tol:
            return x, k+1, ExitFlag.Converged
        elif k == max_iter:
            return x, k+1, ExitFlag.MaxIterations

        k += 1



def combined(f, g, xl, xr, max_iter, tol):
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

    fxr = f(xr)
    fxl = f(xl)
    # Initial step midpoint
    x = [(xl+xr)/2]
    k = 0

    f_carry = f(x[0])
    while True:
        # Try to do NEWTON step
        xnew = x[k] - f_carry / g(x[k])

        if xnew > xl and xnew < xr:
            f_carry = f(xnew)
            # Update bracket
            if f_carry*fxr>0:
                xr = xnew
                fxr = f_carry
            else:
                xl = xnew
                fxl = f_carry
        else:
            # If it fails, do bisection step
            xnew = (xl + xr) / 2

            f_carry = f(xnew)
            if f_carry * fxr > 0:
                xr = xnew
                fxr = f_carry
            else:
                xl = xnew
                fxl = f_carry

        x.append(xnew)


        if abs(f_carry) <= tol:
            return x, k+1, ExitFlag.Converged
        elif k == max_iter:
            return x, k+1, ExitFlag.MaxIterations

        k += 1



