# File: finiteDiff.py
# Author: Ian May
# Purpose: Demonstrate numpy array functionality by
#          computing a few finite differences

import numpy as np
import matplotlib.pyplot as plt

# First derivative using forward difference
def fwdFirstDiff(f, x):
    dx = x[1] - x[0]
    df = (f[1:] - f[:-1]) / dx
    return df, x[:-1]


# First derivative using centered difference
def ctrFirstDiff(f, x):
    dx = x[1] - x[0]
    df = (f[2:] - f[:-2]) / (2.0 * dx)
    return df, x[1:-1]


# Second derivative using centered difference
def ctrSecondDiff(f, x):
    dx = x[1] - x[0]
    ddf = (f[2:] - 2.0 * f[1:-1] + f[:-2]) / dx**2
    return ddf, x[1:-1]


# Function to approximate and its exact derivatives
def fun(x):
    return np.sin(x**2)


def exactFirstDiff(x):
    return 2.0 * x * np.cos(x**2)


def exactSecondDiff(x):
    return 2.0 * (np.cos(x**2) - 2.0 * x**2 * np.sin(x**2))


if __name__ == "__main__":
    # Grid and discrete function
    N = 200
    x = np.linspace(0, np.pi, N)
    f = fun(x)
    # Forward first difference
    fFD, xf = fwdFirstDiff(f, x)
    # centered first difference
    cFD, xc = ctrFirstDiff(f, x)
    # centered second difference
    cSD, xc = ctrSecondDiff(f, x)
    # Evaluate error using known exact derivatives
    ex_fFD = exactFirstDiff(xf)
    ex_cFD = exactFirstDiff(xc)
    ex_cSD = exactSecondDiff(xc)
    print("Errors, but not relative erros:")
    print("Max error fwd first diff:", np.max(np.abs(fFD - ex_fFD)))
    print("Max error ctr first diff:", np.max(np.abs(cFD - ex_cFD)))
    print("Max error ctr second diff:", np.max(np.abs(cSD - ex_cSD)))
    print("\nRelative Errors - by taking the max value:")
    print("Max error fwd first diff:", np.max(np.abs(fFD - ex_fFD) / np.abs(ex_fFD)))
    print("Max error ctr first diff:", np.max(np.abs(cFD - ex_cFD) / np.abs(ex_cFD)))
    print("Max error ctr second diff:", np.max(np.abs(cSD - ex_cSD) / np.abs(ex_cSD)))
    print("\nAverage the Relative Errors:")
    print("Max error fwd first diff:", np.max(np.abs(fFD - ex_fFD) / np.abs(ex_fFD)))
    print("Max error ctr first diff:", np.mean(np.abs(cFD - ex_cFD) / np.abs(ex_cFD)))
    print("Max error ctr second diff:", np.mean(np.abs(cSD - ex_cSD) / np.abs(ex_cSD)))
