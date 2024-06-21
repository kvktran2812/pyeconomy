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


def worker_dynamic(alpha, beta):
    eigen_values = np.array([1, 1 - alpha - beta])
    eigen_vectors = np.array([
        [1, 1], 
        [-alpha, beta]
    ])
    return eigen_values, eigen_vectors


def worker_dynamic_decomposition(alpha, beta):
    D = np.array([
        [1, 0],
        [0, 1 - alpha - beta]
    ])
    E = np.array([
        [1, -alpha],
        [1, beta],
    ])
    return E, D, np.linalg.inv(E)


def worker_dynamic_power_matrix(alpha, beta, m):
    factor = 1 / (alpha + beta)
    lambda_2 = 1 - alpha - beta
    power = np.array([
        [beta + alpha * lambda_2 ^ m, alpha * lambda_2 ^ m],
        [beta * (1 - lambda_2)^m, alpha + beta * (lambda_2) ^ m]
    ])

    return factor * power


def spectral_radius(A):
    """
    Function to calculate spectral radius of a matrix

    Args:
        A (np.array): Matrix A to calculate spectral radius from

    Returns:
        int: Spectral radius of matrix A (scalar value)
    """
    return np.max(np.abs(np.linalg.eigvals(A)))

if __name__ == "__main__":
    A = np.array([[0, -1], [1, 0]])
    