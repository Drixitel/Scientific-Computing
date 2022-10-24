# %%
import numpy as np
import matplotlib.pyplot as plt
import sys
import re


def readData(dFiles, nPlot):
    # Make room for q and a
    q = np.zeros(len(dFiles))
    a = np.zeros([nPlot, len(dFiles)])
    # Read output file
    for idx, d in enumerate(dFiles):
        data = np.loadtxt(d)
        # Keep only the smallest eigenvalues
        a[:, idx] = np.sort(data[:, 1])[0:nPlot]
        # Extract q from filename
        q[idx] = float(re.split("_|\.", d)[2])

    return (q, a)


# Usage: python plotEVals.py <data file list/glob> <number of evals to follow>
if __name__ == "__main__":
    # Extract data files from argv list
    dFiles = sys.argv[1:-1]
    # Number of evals to follow
    nPlot = int(sys.argv[-1])
    q, a = readData(dFiles, nPlot)
    # Plot all simultaneously
    for n in range(0, nPlot):
        plt.plot(q, a[n, :], "-k")
    plt.gca().grid(which="both")
    plt.title(r"Mathieu eigenvalues parametrized by $q$", fontsize=14)
    plt.xlabel(r"$q$", fontsize=14)
    plt.ylabel(r"$a$", fontsize=14)
    plt.show()

# %%
