# %%
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
import math

# This is an example of using Python calculate and plot the motion of a a mass
# orbiting another in a central force field.
# Order of variables in the array u[]:
#    0: r
#    1: v_r
#    2: phi
# Written by Robert P. Johnson

# Parameters describing the system.
k = 1.0  # force constant
Mass = 2.0  # first mass
mass = 1.0  # second mass
mu = Mass * mass / (Mass + mass)  # reduced mass
alpha = -0.1

# Define the central force function
def F(r):
    return -(1.0 + alpha) * k / pow(r, 2.0 + alpha)


def U(r):
    return -k / pow(r, 1.0 + alpha)


# Assign initial conditions to the motion.
r0 = 4.0
rdot0 = 0.0
phi0 = 0.0
Lc = math.sqrt(
    mu * pow(r0, 1.0 - alpha) * (1.0 + alpha) * k
)  # Angular momentum for a circular orbit
L = 0.5 * Lc  # Conserved angular momentum
u0 = [r0, rdot0, phi0]  # initial conditions for all 3 variables

# This function gives the time derivative of each of the 3 variables. These follow from the Lagrange equations of motion,
# taking into account the fact that phi is ignorable, so that pphi=L is constant.
def dudt(u, t):
    r = [0.0, 0.0, 0.0]
    r[0] = u[1]
    r[1] = L * L / (mu * mu * pow(u[0], 3)) + F(u[0]) / mu
    r[2] = L / (mu * u[0] * u[0])
    return r


def h(u):
    return 0.5 * mu * u[1] * u[1] + L * L / (2.0 * mu * u[0] * u[0]) + U(u[0])


# Use the scipy odeint routine to carry out the numerical integration of the system of equations.
t0 = 0.0  # start time
t1 = 100.0  # end time
N = 1600  # number of time steps

# Choose a set of time values at which to evaluate the solution y(t)
t = np.arange(t0, t1, (t1 - t0) / N)

# Call the routing from scipy that does the integration
u = odeint(dudt, u0, t)

Einitial = h(u0)
Efinal = h(u[N - 1, ...])
print("Integration of two-body central force orbits.")
print("The potential goes as -1/r^n with n= " + str(1 + alpha))
print("The masses are " + str(Mass) + " and " + str(mass))
print("The initial radius is " + str(r0))
print("The initial radial velocity is " + str(rdot0))
print("The initial phi angle is " + str(phi0))
print("The conserved angular momentum is " + str(L))
print("The angular momentum for a circular orbit would be " + str(Lc))
print(str(N) + " time steps will be taken from time " + str(t0) + " to time " + str(t1))
print("The initial energy is " + str(Einitial))
print("The final energy is " + str(Efinal))

font = {"size": 18}
plt.rc("font", **font)

# Use pyplot from matplotlib to plot the relative trajectory
fig = plt.figure(figsize=(8, 8))
ax = plt.subplot(111, projection="polar")
ax.set_rlabel_position(-22.5)
ax.plot(u[..., 2], u[..., 0])
ax.set_rmax(1.1 * r0)
plt.tight_layout()
plt.title("Relative Trajectory")
plt.show()

# Plot the individual orbits
fig = plt.figure(figsize=(8, 8))
ax = plt.subplot(111, projection="polar")
ax.plot(u[..., 2], (Mass / (Mass + mass)) * u[..., 0])
ax.plot(u[..., 2] + math.pi, (mass / (Mass + mass)) * u[..., 0])
ax.set_rmax(1.1 * r0)
plt.title("Individual Orbits")
plt.show()

# Now use matplotlib to make an animation of the motion
fig = plt.figure(figsize=(8, 8))
ax = plt.subplot(111, projection="polar")
(pnt1,) = ax.plot([], [], "bo", markersize=12)
(pnt2,) = ax.plot([], [], "ro", markersize=12)
ax.set_rmax(1.1 * r0)
plt.title("Orbit Animation")
time_text = ax.text(0.01, 0.98, "", transform=ax.transAxes)
time_step = 40.0 * (t1 - t0) / N


def init():
    pnt1.set_data([], [])
    pnt2.set_data([], [])
    time_text.set_text("")
    return pnt1, pnt2, time_text


def animate(i):
    pnt1.set_data(u[i, 2], (Mass / (Mass + mass)) * u[i, 0])
    pnt2.set_data(u[i, 2] + math.pi, (mass / (Mass + mass)) * u[i, 0])
    time = i * time_step
    time_text.set_text("time=%.1f ms" % time)
    return pnt1, pnt2, time_text


# The animation is created here
anim = animation.FuncAnimation(
    fig, animate, init_func=init, frames=N, interval=time_step, blit=False
)

# Save the animation to an mpeg file. This requires ffmpeg to be installed,
# with the executable in the PATH
# This takes a lot of CPU time, so don't do it when it is not needed.
# anim.save('TimeOrbit.mp4', fps=30, extra_args=['-vcodec', 'libx264'])

# Display the animation
plt.show()
# %%
