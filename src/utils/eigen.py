import scipy
import numpy as np
import scipy.linalg


def eigen_decomposition(A):
    """
    Compute diagonalizable matrices of A
    A = PDP^(-1)
    """
    eigen_values, eigen_vectors = scipy.linalg.eig(A)
    P = eigen_vectors
    D = np.diag(eigen_values)
    P_inv = np.linalg.inv(P)
    
    return P, D, P_inv

def spectral(A):
    eigen_values, eigen_vectors = scipy.linalg.eig(A)
    U = eigen_vectors
    D = np.diag(eigen_values)
    return U, D, U.T


if __name__ == "__main__":
    A = np.array([[0, -1], [1, 0]])
    