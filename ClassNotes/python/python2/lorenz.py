# File: lorenz.py
# Author: Ian May
# Purpose: Demonstrate SciPy by solving the Lorenz equations

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Define right hand side of ODE
# Note calling signature must look like this
def lorenz(t, y):  # time is not used, but required as a parameter
    # Parameters for the system
    rho = 28
    sigma = 10
    beta = 8 / 3
    # Return RHS
    f = np.zeros(y.shape)
    f[0] = sigma * (y[1] - y[0])
    f[1] = y[0] * (rho - y[2]) - y[1]
    f[2] = y[0] * y[1] - beta * y[2]
    return f


if __name__ == "__main__":
    # Set initial condition and solve
    t0, tf = 0.0, 100.0
    dt_max = 0.02
    y0 = np.ones(3)
    sol = solve_ivp(
        lorenz, (t0, tf), y0, max_step=dt_max
    )  # max step limited for pretty plots
    # sol = solve_ivp(lorenz, (t0, tf), y0) to see what happens
    # sol = solve_ivp(lorenz, (t0, tf), y0,t_eval =np.linspace(t0,tf,10_000)) specifc evaluation times

    # Plot time series of each component
    fig, axs = plt.subplots(3, 1)

    axs[0].plot(sol.t, sol.y[0, :])
    axs[0].set_ylabel("x", fontsize=14)
    axs[0].set_title("Evolution of Lorenz equations", fontsize=16)

    axs[1].plot(sol.t, sol.y[1, :])
    axs[1].set_ylabel("y", fontsize=14)

    axs[2].plot(sol.t, sol.y[2, :])
    axs[2].set_xlabel("t", fontsize=14)
    axs[2].set_ylabel("z", fontsize=14)

    # fig.tight_layout()

    plt.savefig("Evolution.png")

    plt.show()

    # Plot phase space trajectory
    ax = plt.figure().add_subplot(projection="3d")

    ax.plot(sol.y[0, :], sol.y[1, :], sol.y[2, :])

    ax.set_xlabel("x", fontsize=15)
    ax.set_ylabel("y", fontsize=15)
    ax.set_zlabel("z", fontsize=15)
    ax.set_title("Lorenz phase space trajectory", fontsize=18)

    # plt.savefig("Phasespace.png")

    plt.show()
