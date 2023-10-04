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
        G = g(x[k])
        if abs(G) < 10**-8:
            return x, k+1, ExitFlag.DivideByZero
        xnew = x[k] - f_carry / G

        print("step=", -f_carry/G, "  xnew=", xnew)

        x.append(xnew)
        f_carry = f(xnew)
        if abs(f_carry) < tol:
            return x, k+1, ExitFlag.Converged
        elif k == max_iter:
            return x, k+1, ExitFlag.MaxIterations

        k += 1

def newton_damped(f, g, x0, max_iter, tol, beta):
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
        G = g(x[k])
        if abs(G) < 10**-8:
            return x, k+1, ExitFlag.DivideByZero
        delta = f_carry / G
        alpha = 1 / ( 1 + beta*abs(delta) )
        xnew = x[k] - alpha * delta

        x.append(xnew)
        f_carry = f(xnew)

        if abs(f_carry) < tol:
            return x, k+1, ExitFlag.Converged
        elif k == max_iter:
            return x, k+1, ExitFlag.MaxIterations

        k += 1

