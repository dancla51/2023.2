import numpy as np
import Lab1
import matplotlib.pyplot as plt

def construct_system(N, K):
    # K should be a list
    K.append(0) #K sub n+1 = 0
    A = np.zeros([N,N])

    for i in range(N):
        for j in range(N):
            if i==j:
                A[i,j] = K[i]+K[i+1]
            elif i==j+1:
                    A[i,j] = -1 * K[i]
            elif j==i+1:
                    A[i,j] = -1 * K[j]
    return(A)


def plot_results(real, tols, founds):

    # Plot found values
    for i, tol in enumerate(tols):
        plt.plot([tol]*10, founds[1], 'b^')
    # Plot real values (with horizontal lines)
    for ele in real:
        plt.plot([1e-8, 1e-2], [ele]*2, 'r-')

    plt.xlabel("Tolerance")
    plt.ylabel("Frequency (Hz)")
    plt.semilogx()
    plt.show()


def solve_freq_modes(N,K):
    A_mat = construct_system(N, K)
    tols = [1e-2, 1e-4, 1e-6, 1e-8]
    freqs_from_tols = []

    for num, tol in enumerate(tols):
        all_eigenpairs = Lab1.power_w_deflate(A_mat, tol)
        found_eig = []
        for pair in range(N):
            found_eig.append(all_eigenpairs[pair][0])
        found_freq = np.sqrt(found_eig) / (2*np.pi)
        freqs_from_tols.append(found_freq)

    real_eig = np.sort(np.linalg.eig(A_mat)[0])[::-1]
    real_freq = np.sqrt(real_eig) / (2*np.pi)
    plot_results(real_freq, tols, freqs_from_tols)


if __name__ == "__main__":
    # Test with spring constants of
    solve_freq_modes(10, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1])




