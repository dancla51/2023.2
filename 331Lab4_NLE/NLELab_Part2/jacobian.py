import numpy as np

#Computes the numerical derivative of a function, using central differences
#and a step size of h.

# Inputs
# f      : function handle for a nonlinear function
# x      : vector corresponding to the point at which the derivatives should
#          be computed
# n      : number of dimensions for the function input: x
# h      : step size for numerical estimate of partial derivative

# Outputs
# J      : partial derivative matrix (Jacobian)
def jacobian(f, x, h, n):
    # WORKING
    J = np.zeros((n,n))

    for j in range(n):
        # complete code (the answers have three lines of code here)
        upper = np.copy(x)
        upper[j] = upper[j] + h

        lower = np.copy(x)
        lower[j] = lower[j] - h

        dfdj = ( f(upper)-f(lower) ) / (2*h)
        J[:, j] = dfdj

    return J