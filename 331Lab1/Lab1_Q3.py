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
    print(A)








if __name__ == "__main__":
    # Test matrix
    construct_system(4, [1,2,3,4])




