import scipy
import numpy as np
import scipy.linalg


def eigen_decomposition(A):
    """
    Compute diagonalized matrix of A
    A = P D P_inv

    Args:
        A (np.array): Matrix A that will be diagonalized

    Returns:
        tuple of 3 np.array: P, D, P_inv (P inversed)
    """
    eigen_values, eigen_vectors = scipy.linalg.eig(A)
    P = eigen_vectors
    D = np.diag(eigen_values)
    P_inv = np.linalg.inv(P)
    
    return P, D, P_inv

def spectral(A):
    """
    Compute diagonalized matrix of A in spectral theorem when A is symetric
    A = U D U.T

    Args:
        A (np.array): Matrix A that will be diagonalized (must be symetric)

    Returns:
        tuple of 3 np.array: U, D, U.T (U transpose)
    """
    eigen_values, eigen_vectors = scipy.linalg.eig(A)
    U = eigen_vectors
    D = np.diag(eigen_values)
    return U, D, U.T


if __name__ == "__main__":
    A = np.array([[0, -1], [1, 0]])
    