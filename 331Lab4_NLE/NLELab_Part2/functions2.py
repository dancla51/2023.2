import numpy as np

def f5(x):
        return np.array([x[0]*x[0]-2*x[0]+x[1]*x[1]+2*x[1]-2*x[0]*x[1]+1,x[0]*x[0]+2*x[0]+x[1]*x[1]+2*x[1]+2*x[0]*x[1]+1])

def f6(x):
    return np.array([x[0]*x[0]-x[1],x[0]*x[0]+x[1]*x[1]-2])

def f7(x):
    return np.array([x[0]*x[0]-x[1],x[0]*x[0]+x[1]*x[1]])

def f8(x):
    return np.array([x[0]*x[0]+x[1]*x[1]+x[2]*x[2]-6,x[0]*x[0]-x[1]*x[1]+2.*x[2]*x[2]-2,2*x[0]*x[0]+x[1]*x[1]-x[2]*x[2]-3])

def f9(x):
    return x**4 - 8*x**3 + 24*x**2 - 32*x + 17

def f10(x):
    return 2 - np.exp(-2*x**2 + 8*x - 8)