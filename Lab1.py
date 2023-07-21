import numpy as np


def power(Mat, tolerance = 10**-12):
    # Initialise
    n = len(Mat)
    rel_change=1
    # Generate Random Eigenvector
    x = np.random.rand(n)
    x = np.reshape(x/np.linalg.norm(x), [n,1])
    gamma = 0
    # Loop until meets tolerance levels
    while rel_change>tolerance:
        # Calc new vector
        x = np.matmul(Mat,x)/np.linalg.norm(np.matmul(Mat,x))
        # Calc gamma
        gamma_new = np.matmul(x.T,np.matmul(Mat,x))
        # Calc relative change
        rel_change = (gamma_new-gamma)/gamma_new
        gamma=gamma_new

    return gamma,x

if __name__ == "__main__":
    # Test with given matrix
    Mat = np.matrix([[2, -1],[ -1, 2]])

    l, v = power(Mat)
    print("The eigenvalue is: %2f , and the eigenvector is: (%5.3f, %5.3f)" % (1,v[0,0], v[1,0]))