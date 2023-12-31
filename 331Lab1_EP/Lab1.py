import numpy as np


def power(Mat, tolerance=10 ** -18):
    # Initialise
    n = len(Mat)
    rel_change = 1
    # Generate Random Eigenvector
    x = np.random.rand(n)
    x = np.reshape(x / np.linalg.norm(x), [n, 1])
    gamma = 0
    # Loop until meets tolerance levels
    while rel_change > tolerance:
        # Calc new vector
        x = np.matmul(Mat, x) / np.linalg.norm(np.matmul(Mat, x))
        # Calc gamma
        gamma_new = np.matmul(x.T, np.matmul(Mat, x))
        # Calc relative change
        rel_change = (gamma_new - gamma) / gamma_new
        gamma = gamma_new

    return gamma[0, 0], x


def power_w_deflate(Mat, tolerance=10 ** -18):
    n = len(Mat)
    eigenpairs = []
    for i in range(n):
        eigenpair = power(Mat, tolerance)
        eigenpairs.append(eigenpair)
        # Find value of deflation and deflate the matrix
        deflation = eigenpairs[i][0] * np.matmul(eigenpairs[i][1], eigenpairs[i][1].T)
        Mat = Mat - deflation

    return (eigenpairs)


if __name__ == "__main__":
    # Test matrix
    Mat1 = np.matrix([[2, -1], [-1, 2]])
    Mat2 = np.matrix([[2, -1, 0], [-1, 2, -1], [0, -1, 2]])

    # Find all eigenpairs using power method with deflation
    all_eigenpairs = power_w_deflate(Mat1, tolerance=10 ** -18)
    # Print results
    for e in range(len(all_eigenpairs)):
        prints1 = (e + 1, all_eigenpairs[e][0])
        prints2 = ['%5.3f' % all_eigenpairs[e][1][i, 0] for i in range(len(all_eigenpairs))]
        print("For pair %i, eigenvalue is: %5.3f & eigenvector is: " % prints1, prints2)

    print("\n")
    # Find all eigenpairs using power method with deflation
    all_eigenpairs = power_w_deflate(Mat2, tolerance=10 ** -18)
    # Print results
    for e in range(len(all_eigenpairs)):
        prints1 = (e + 1, all_eigenpairs[e][0])
        prints2 = ['%5.3f' % all_eigenpairs[e][1][i, 0] for i in range(len(all_eigenpairs))]
        print("For pair %i, eigenvalue is: %5.3f & eigenvector is: " % prints1, prints2)
