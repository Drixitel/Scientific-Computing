# File: randEigH.py
# Author: Ian May
# Purpose: Generates many random symmetric matrices
#          and creates several histograms from their
#          spectra
# Notes: See Wigner's semicircle distribution for more info

import numpy as np
from numpy.random import default_rng
import matplotlib.pyplot as plt

# Initialize default generator
rng = default_rng()

# Generate lots of random symmetric matrices
# returns *scaled* eigenvalues
def randHermEvals(N=10, numSamples=100):
    ew = np.zeros((N, numSamples))
    for i in range(0, numSamples):
        # Note: eigvalsh looks only at lower triangle by default
        #       don't need to symmetrize A
        A = rng.standard_normal((N, N))  # does become symmetric
        # Get eigenvalues and scale out by sqrt(N)
        ew[:, i] = np.linalg.eigvalsh(A) / np.sqrt(N)  # will assume A is symmetric
    # print("Matix A:")
    # print(A)
    return ew


# Evaluate Wigner's semicircle distribution--needs probability theory and lin.alg
# Note: assumes unit variance of matrix entries
def wignerDist(x):
    return np.sqrt(4 - x**2) / (2 * np.pi)


if __name__ == "__main__":
    N = 40  # increasing this value gets us closer to theoretical results but costly
    numSamples = 20000  # same many needed but costly

    # Generate lots of matrices, get their e-vals and spectral gaps
    ewSamples = randHermEvals(N, numSamples)

    # Generate the jump in energy (gaps) eignenvalue gas
    ewGaps = ewSamples[1:, :] - ewSamples[:-1, :]

    # Evaluate Wigner distribution
    x = np.linspace(-2, 2, 200)
    wd = wignerDist(x)

    # Set up two panel plot for e-vals
    fig, axs = plt.subplots(2, 1)

    # Plot histogram of all e-vals
    axs[0].hist(ewSamples.flatten(), bins=100, density=True)
    axs[0].plot(x, wd, "-k")
    axs[0].set_title("All eigenvalues")

    # Plot separate histograms for minimum, central, and largest e-vals
    axs[1].hist(ewSamples[0, :], bins=75, density=True)
    axs[1].hist(ewSamples[N // 2 - 1, :], bins=75, density=True)
    axs[1].hist(ewSamples[-1, :], bins=75, density=True)
    axs[1].set_title("Eigenvalues %d, %d, and %d" % (1, N // 2, N))
    plt.savefig("RandomMarticies.png")
    plt.show()

    # Semicircle Wtf
    # semi-normal dist.

    # Set up two panel plot for e-vals ------------------------gaps
    fig, axs = plt.subplots(2, 1)

    # Plot histogram of all e-vals
    axs[0].hist(ewGaps.flatten(), bins=100, density=True)
    # axs[0].plot(x, wd, "-k")
    axs[0].set_title("All eigenvalues gaps")

    # Plot separate histograms for minimum, central, and largest e-vals
    axs[1].hist(ewGaps[0, :], bins=75, density=True)
    axs[1].hist(ewGaps[N // 2 - 1, :], bins=75, density=True)
    axs[1].hist(ewGaps[-1, :], bins=75, density=True)
    axs[1].set_title("Eigenvalue gaps %d, %d, and %d" % (1, N // 2, N - 1))
    plt.savefig("EignenGaps.png")
    plt.show()
