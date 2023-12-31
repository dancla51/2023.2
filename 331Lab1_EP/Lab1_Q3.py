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
        plt.plot([tol]*10, founds[1], 'b.')
    plt.plot(0, 0, 'b+', label="Calculated Values")

    # Plot real values (with horizontal lines)
    for ele in real:
        plt.plot([1e-8, 1e-2], [ele]*2, 'r--')
    plt.plot(0, 0, 'r-', label="True Values")

    plt.xlabel("Tolerance")
    plt.ylabel("Frequency (Hz)")
    plt.legend(bbox_to_anchor=(0.5, 1.15), loc='upper center')
    plt.semilogx()
    #plt.savefig("Freq_by_tolerance")
    #plt.show()

def print_results(real, tols, founds):
    # Print all frequencies with progression
    for ev_num in range(len(real)):
        print("\nFor the %ith frequency, I calculated:" % (ev_num+1))
        for i in range(len(founds)):
            print("%5.6f Hz from a tolerance of %1.1e" % (founds[i][ev_num], tols[i]))
        print("%5.6f Hz is the true value" % real[ev_num])

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
    print_results(real_freq, tols, freqs_from_tols)

def solve_simple(N,K):
    # Solve for default tolerance
    A_mat = construct_system(N, K)
    all_eigenpairs = Lab1.power_w_deflate(A_mat) # Use default tolerance
    # Print results
    for i,pair in enumerate(all_eigenpairs):
        print("The %ith frequency is %f" % (i+1, np.sqrt(pair[0]) / (2*np.pi) ))
        print("The %ith eigenvector is" % (i+1), pair[1].reshape([1, len(pair[1])]), "\n")

if __name__ == "__main__":
    # Test with spring constants of
    #solve_freq_modes(10, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
    solve_simple(10, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1])




