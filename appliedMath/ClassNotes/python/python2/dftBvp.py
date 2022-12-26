# File: dftBvp.py
# Author: Ian May
# Purpose: Define a brief spectral collocation method for the
#          shifted Poisson equation. Written primarily to
#          showcase basic numpy usage

import numpy as np
import matplotlib.pyplot as plt

# Define spatial grid
def grid(N):
    return np.linspace(0, 2 * np.pi, N, endpoint=False)


# Define wavenumbers and forward transform
def transMat(x):
    N = len(x)
    dx = x[1] - x[0]
    om = 2 * np.pi / (N * dx)
    # Set wavenumbers and transformation matrix
    k = np.zeros(N)
    T = np.zeros([N, N])
    T[0, :] = 1.0 / N
    for i in np.arange(1, N, 2):
        k[i] = (i + 1) * om / 2
        T[i, :] = 2 * np.cos(k[i] * x) / N
        if i + 1 < N:
            k[i + 1] = k[i]
            T[i + 1, :] = 2 * np.sin(k[i] * x) / N
    if N % 2 == 0:
        T[N - 1, :] /= 2
    return (k, T)


# Define inverse transformation
def invTransMat(x, k):
    N = len(x)
    Tinv = np.zeros([N, N])
    Tinv[:, 0] = 1.0
    for j in np.arange(1, N, 2):
        Tinv[:, j] = np.cos(k[j] * x)
    for j in np.arange(2, N, 2):
        Tinv[:, j] = np.sin(k[j] * x)
    return Tinv


# Define forcing function and exact solution
def forcing(x):
    es = np.exp(np.sin(x)) * (1 + np.sin(x) - np.cos(x) ** 2)
    ec = 9 * np.exp(np.cos(3 * x)) * (-1.0 / 9.0 + np.sin(3 * x) ** 2 - np.cos(3 * x))
    return es + ec


def exact(x):
    return np.exp(np.sin(x)) - np.exp(np.cos(3 * x))


def solve(force, N):

    print("Solving with %d grid points" % N)
    # We should wrap this into its own function shouldn't we?
    x = grid(N)
    k, T = transMat(x)
    Tinv = invTransMat(x, k)
    f = force(x)
    ft = np.matmul(T, f)
    ft = ft / (1 + k**2)
    u = np.matmul(Tinv, ft)
    return u, x


# Define default behavior when calling from the command line
if __name__ == "__main__":

    # Code to loop quickly through values:
    # for N in range(21, 102, 10):
    #     u, x = solve(forcing, N)
    #     print("Max error: ", np.max(np.abs(u - exact(x))))

    N = 101
    u, x = solve(forcing, N)
    print("Max error: ", np.max(np.abs(u - exact(x))))

    plt.plot(x, u, "-o", x, forcing(x), "-b")
    plt.savefig("soln.png")
