# %%
import numpy as np
import matplotlib.pyplot as plt
import sys


def readData(dataFile):
    # Read output file
    data = np.loadtxt(dataFile)
    # Extract grid positions
    x = data[:, 0]
    # Extract real part of eigenvalues
    w = data[:, 1]
    # Extract eigenfunctions
    V = data[:, 3:]
    return (x, w, V)


def trimData(thresh, w, V):
    wtrim = w[np.where(w < thresh)]
    Vtrim = np.zeros([V.shape[0], wtrim.shape[0]])
    # Loop over just the smallest entries of w and copy out
    for dst, src in enumerate(np.nditer(np.where(w < thresh))):
        Vtrim[:, dst] = V[:, src]
    return (wtrim, Vtrim)


# Usage: python plotEFuncs.py <data file> <Threshold for a>
if __name__ == "__main__":
    x, wFull, VFull = readData(sys.argv[1])
    w, V = trimData(float(sys.argv[2]), wFull, VFull)
    # Plot all simultaneously
    for idx in range(0, V.shape[1]):
        plt.plot(x, V[:, idx])
    plt.gca().grid(which="both")
    plt.title(r"All Mathieu functions with $a<" + sys.argv[2] + r"$")
    plt.xlabel(r"$x$")
    plt.ylabel(r"$y$")
    plt.show()

# %%
# x,w,V = readData('Mathieu_201_40.dat')
# trimData(x,w,V)
# %%
