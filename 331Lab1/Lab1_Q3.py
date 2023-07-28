import numpy as np
import Lab1


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

def solve_freq_modes(N,K):
    A_mat = construct_system(N, K)
    all_eigenpairs = Lab1.power_w_deflate(A_mat, 10**-2)
    found_eig = []
    for pair in range(N):
        found_eig.append(all_eigenpairs[pair][0])
    found_freq = np.sqrt(found_eig) / (2*np.pi)

    real_eig = np.sort(np.linalg.eig(A_mat)[0])[::-1]
    real_freq = np.sqrt(real_eig) / (2*np.pi)
    print(real_freq)
    print(found_freq)


if __name__ == "__main__":
    # Test with spring constants of
    solve_freq_modes(10, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1])




