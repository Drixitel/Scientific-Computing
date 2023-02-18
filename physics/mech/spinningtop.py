#%%
import mpl_toolkits.mplot3d.axes3d as p3
from scipy.integrate import odeint
from scipy.optimize import root
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
import math

# This is an example of using Python calculate and plot the motion of a symmetric top
# Order of variables in the array u[]:
#    0: theta
#    1: theta-dot
#    2: phi
#    3: psi

print()
print("Numerical solution of the symmetric top.  R. Johnson  5/23/2021")

# Parameters describing the system.
L = 0.5  # distance to the c.m. in meters
M = 5.0  # mass in kg
g = 9.8  # gravitational acceleration in m/s^2
beta = 2.0  # parameter that sets the moments of inertia (see I1 below)
I1 = 2.0 * M * g * L / beta  # first principal moment of inertia
I3 = 0.25 * I1  # moment of inertia about the symmetry axis
print("Parameters: beta=", beta)
print("            L=", L, " meters,  M=", M, " kg,   g=", g, " m/s^2")
print("            I1=", I1, "    I3=", I3)

# Initial conditions
phi0 = 0.0  # initial azimuthal angle
psi0 = 0.0  # initial rotation angle of the top (this has no consequence, due to the symmetry)
theta0 = 45.0 * math.pi / 180.0  # initial tip angle of the top
psiDot0 = 10.0  # initial spin rate of the top about its symmetry axis
phiDot0 = 1.0  # initial precession rate
thetaDot0 = 0.5  # initial angular velocity in the tipping direction

print("Initial tipping angle is theta0=", theta0 * 180.0 / math.pi, " degrees")
print("    cos(theta0)=", math.cos(theta0))
print("Initial phi-dot=", phiDot0, " radians/s")
print("Initial psi-dot=", psiDot0, " radians/s")
print("Initial theta-dot=", thetaDot0, " radians/s")

# The conserved angular velocity about the spin axis (I3 times this is the conserved momentum conjugate to psi)
omega3 = psiDot0 + phiDot0 * math.cos(theta0)
pphi = I1 * phiDot0 * math.pow(math.sin(theta0), 2) + I3 * omega3 * math.cos(theta0)
ppsi = I3 * omega3
print("Conserved z component of angular momentum, p-phi=", pphi, " kg m^2/s^2")
print("Conserved angular momentum about the symmetry axis, p-psi=", ppsi, " kg m^2/s^2")
print("p-phi over p-psi=", pphi / ppsi)

Omega = M * g * L / ppsi
print("Precession speed for constant precession is approximately ", Omega, " radians/s")


def phidot(theta):
    return (pphi - ppsi * math.cos(theta)) / (I1 * math.pow(math.sin(theta), 2))


def psidot(theta):
    return ppsi / I3 - math.cos(theta) * phidot(theta)


def thetaDotDot(theta):
    q1 = math.pow(phidot(theta), 2) * math.sin(theta) * math.cos(theta)
    q2 = (
        (psidot(theta) + phidot(theta) * math.cos(theta))
        * phidot(theta)
        * math.sin(theta)
    )
    q3 = M * g * L * math.sin(theta)
    return q1 - I3 * q2 / I1 + q3 / I1


phiDot0c = phidot(theta0)
psiDot0c = psidot(theta0)
# print("Check: initial psi-dot=",psiDot0c," radians/s")
# print("Check: initial phi-dot=",phiDot0c," radians/s")

# Energy and effective potential
def Ueff(theta):
    Ue = (
        math.pow((pphi - ppsi * math.cos(theta)), 2)
        / (2.0 * I1 * math.pow(math.sin(theta), 2))
        + ppsi * ppsi / 2.0 / I3
        + M * g * L * math.cos(theta)
    )
    return Ue


Energy = 0.5 * I1 * thetaDot0 * thetaDot0 + Ueff(theta0)


def func(theta):
    return Ueff(theta) - Energy


sol = root(func, math.pi / 20.0)
t1 = sol.x[0]
sol = root(func, math.pi / 2.0)
t2 = sol.x[0]
print("The conserved energy is E=", Energy, " Joules")
print(
    "First root of the potential function= ",
    t1 * 180.0 / math.pi,
    " degrees;   cos(theta)=",
    math.cos(t1),
)
print(
    "Second root of the potential function=",
    t2 * 180.0 / math.pi,
    " degrees;   cos(theta)=",
    math.cos(t2),
)
print("Ratio of pphi/psi is u0=", pphi / ppsi)

Nt = 65
tmin = 20.0
tmax = 85.0
theta = np.arange(tmin, tmax, (tmax - tmin) / Nt)
U = np.zeros(Nt)
E = np.zeros(Nt)
for i in range(Nt):
    U[i] = Ueff(theta[i] * math.pi / 180.0)
    E[i] = Energy
fig = plt.figure(figsize=(8, 8))
ax = plt.subplot()
ax.plot(theta, U)
ax.plot(theta, E)
ax.set_xlabel("theta (degrees)")
ax.set_ylabel("Ueff (J)")
plt.title("Effective Potential")
plt.show()

# This function gives the time derivative of each of the 4 variables. These follow from the Lagrange equations of motion
def dudt(u, t):
    r = [0.0, 0.0, 0.0, 0.0]
    r[0] = u[1]
    r[1] = thetaDotDot(u[0])
    r[2] = phidot(u[0])
    r[3] = psidot(u[0])
    return r


# Use the scipy odeint routine to carry out the numerical integration of the system of equations.
t0 = 0.0  # start time
t1 = 20.0  # end time
N = 800  # number of time steps

# Choose a set of time values at which to evaluate the solution y(t)
t = np.arange(t0, t1, (t1 - t0) / N)

u0 = [theta0, thetaDot0, phi0, psi0]

# Call the routing from scipy that does the integration
u = odeint(dudt, u0, t)

# Check that the energy really was conserved:
Efinal = 0.5 * I1 * math.pow(u[N - 1, 1], 2) + Ueff(u[N - 1, 0])
print("The final energy is " + str(Efinal))

font = {"size": 18}
plt.rc("font", **font)

# Use pyplot from matplotlib to plot the theta motion (nutation)
fig = plt.figure(figsize=(8, 8))
ax = plt.subplot()
ax.plot(t, u[..., 0] * 180.0 / math.pi)
ax.set_xlabel("t (s)")
ax.set_ylabel("theta (degrees)")
ax.set_ylim(0.0, 110.0)
plt.title("Nutation")
plt.show()

# Plot the phi motion (precession)
fig = plt.figure(figsize=(8, 8))
ax = plt.subplot()
ax.set_xlabel("t (s)")
ax.set_ylabel("phi (degrees)")
ax.plot(t, u[..., 2] * 180.0 / math.pi)
plt.title("Precession")
plt.show()

# Calculate and plot the 3D trajectory of the center of mass
X = np.zeros(N)
Y = np.zeros(N)
Z = np.zeros(N)
for i in range(N):
    X[i] = L * math.cos(u[i, 2]) * math.sin(u[i, 0])
    Y[i] = L * math.sin(u[i, 2]) * math.sin(u[i, 0])
    Z[i] = L * math.cos(u[i, 0])

fig = plt.figure(figsize=(8, 8))
ax = plt.axes(projection="3d")
ax.set_xlim3d(-1.1 * L, 1.1 * L)
ax.set_ylim3d(-1.1 * L, 1.1 * L)
ax.set_zlim3d(-1.1 * L, 1.1 * L)
ax.set_xlabel("x (m)")
ax.set_ylabel("y (m)")
ax.set_zlabel("z (m)")
ax.set_aspect("auto")
plt.title("Trajectory of the Symmetric Top CM")
ax.plot3D(X, Y, Z)
plt.show()

# Now use matplotlib to make an animation of the motion


def update_line(num, data, line, type):
    line.set_data(data[0:2, :num])
    line.set_3d_properties(data[2, :num])
    return line


time_step = math.floor(500.0 * (t1 - t0) / N)
print("Time step = ", time_step)
fig = plt.figure(figsize=(8, 8))
ax = plt.axes(projection="3d")
ax.set_xlim3d(-1.2 * L, 1.2 * L)
ax.set_ylim3d(-1.2 * L, 1.2 * L)
ax.set_zlim3d(-1.2 * L, 1.2 * L)
ax.set_xlabel("x (m)")
ax.set_ylabel("y (m)")
ax.set_zlabel("z (m)")
ax.set_title("Symmetric Top Animation")
data = np.empty((3, N))
for i in range(N):
    data[0, i] = X[i]
    data[1, i] = Y[i]
    data[2, i] = Z[i]
line = ax.plot3D(data[0, 0:1], data[1, 0:1], data[2, 0:1])[0]

# The animation is created here
line_ani = animation.FuncAnimation(
    fig, update_line, N, fargs=(data, line, type), interval=time_step, blit=False
)

# Save the animation to an mpeg file. This requires ffmpeg to be installed,
# with the executable in the PATH
# line_ani.save('symmetricTop.mp4', fps=30, extra_args=['-vcodec', 'libx264'])

# Display the animation
plt.show()

# %%
