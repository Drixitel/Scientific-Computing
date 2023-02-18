#%%from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

# from matplotlib import animation
import math

# This is an example of using Python to calculate and plot the motion of a driven damped pendulum.
# This program can reproduce plots shows in Chapter 12 and also animate the pendulum motion.
# R.P. Johnson, August 2018
# See Section 12.2 of Taylor for the an explanation of the equation of motion
# The motion is calculated by integration of a set of first-order differential equations.
# Order of variables in each vector of the list u[]:
#    0: phi        angle of the pendulum
#    1: dphi/dt    angular velocity of the pendulum
#    2: theta      phase of the harmonic driving term


# Parameters describing the pendulum system
# L = 0.1103275111
# g = 9.8
omega = 2.0 * math.pi
omega0 = 1.5 * omega
print("Enter a value for gamma:")
gamma = float(input())
print("Enter the number of driving periods to simulate: (10)")
M = 10
inp = input()
if inp != "":
    M = int(inp)
print("Enter the first starting angle in degrees (0)")
phi0 = 0.0
inp = input()
if inp != "":
    phi0 = float(inp) * math.pi / 180.0
print("Enter the second starting angle in degrees (0)")
phi1 = 0.0
inp1 = input()
if inp1 != "":
    phi1 = float(inp1) * math.pi / 180.0

beta = omega0 / 4.0
print("Simulation of a driven, damped pendulum")
# print("Pendulum length= "+str(L)+", and acceleration of gravity g= "+str(g))
print(
    "Natural frequency= " + str(omega0) + ", and the driving frequency= " + str(omega)
)
print("The ratio of the natural frequency to the driving frequency is ", omega0 / omega)
print("The driving period is ", 2.0 * math.pi / omega)
print("The angles are " + str(phi0) + ", and " + str(phi1))
print(
    "The damping factor is b= "
    + str(beta)
    + ", and the driving amplitude is gamma= "
    + str(gamma)
)
print("A total of ", M, " driving periods will be simulated")

# The drive period
tau = 2.0 * math.pi / omega
print("The driving period is tau= " + str(tau))

# Assign initial conditions to the motion.
phiDot0 = 0.0
theta0 = 0.0
phiDot1 = 0.0
theta1 = 0.0

u0 = [phi0, phiDot0, theta0]  # initial conditions for all 3 variables
u1 = [phi1, phiDot1, theta1]

# This function gives the time derivative of each of the 3 variables. It corresponds to the differential equation 12.11 in Taylor
def dudt(u, t):
    r = [0.0, 0.0, 0.0]
    r[0] = u[1]
    r[1] = (
        omega0 * omega0 * (gamma * math.cos(u[2]) - math.sin(u[0])) - 2.0 * beta * u[1]
    )
    r[2] = omega
    return r


# Use the scipy odeint routine to carry out the numerical integration of the system of equations.
t0 = 0.0  # start time
N0 = 100
dt = tau / N0  # time step
N = M * N0  # number of time steps
t1 = t0 + N * dt  # end time
print("The number of time steps per driving period is N0=" + str(N0))
print("The total number of time steps is N=" + str(N))

# Choose a set of time values at which to evaluate the solution y(t)
t = np.arange(t0, t1, dt)

# Call the routing from scipy that does the integration
# The returned "u" is a list of 3D vectors. The angle Phi is the 0th element of each vector
# See the detailed description of u above.
uu0 = odeint(dudt, u0, t)
uu1 = odeint(dudt, u1, t)
uu2 = uu1 - uu0
for row in uu2:
    for b in row:
        b = np.log(b) if b != 0 else b

# Print the results out to a text file
f = open("drivenPendulumOutput.txt", "w")
for time, phi in zip(t, uu0[..., 0]):
    strOut = "{}, {}, \n".format(time, phi)
    f.write(strOut)
f.close()

# Change the default font size in Python Matplotlib
font = {"size": 18}
plt.rc("font", **font)

# Use pyplot from matplotlib to plot the motion phi1(t)
fig, ax = plt.subplots(figsize=(8, 8))
plt.xlim(t0, t1)
plt.suptitle("Pendulum Position versus Time")
ax.set_xlabel("t (s)")
ax.set_ylabel("phi1 (degrees)")
ax.plot(t, uu0[..., 0] * 180.0 / math.pi)


fig, ax = plt.subplots(figsize=(8, 8))
plt.xlim(t0, t1)
plt.suptitle("Pendulum Position versus Time")
ax.set_xlabel("t (s)")
ax.set_ylabel("phi2 (degrees)")
ax.plot(t, uu1[..., 0] * 180.0 / math.pi)


fig, ax = plt.subplots(figsize=(8, 8))
plt.xlim(t0, t1)
plt.suptitle("Pendulum Logarithm of Absolute Difference versus Time")
ax.set_xlabel("t (s)")
ax.set_ylabel("log |delta phi| (degrees)")
ax.plot(t, uu2[..., 0] * 180.0 / math.pi)

plt.show()

# # You can delete everything that follows if you don't want the animation
# # In that case you may also delete "from matplotlib import animation" near the file beginning

# # Calculate the 2D trajectories of the mass
# X1 = np.zeros(N)
# Y1 = np.zeros(N)
# for i in range(N):
#     X1[i] = L*math.sin(u[i,0])
#     Y1[i] = -L*math.cos(u[i,0])

# # Now use matplotlib to make an animation of the motion
# fig = plt.figure(figsize=(8,8))
# ax = plt.axes(xlim=(-1.2*L,1.2*L), ylim=(-1.2*L,1.2*L))
# plt.suptitle('Driven Damped Pendulum')
# ax.set_aspect('equal')
# line, = ax.plot([],[],lw=2)
# time_text = ax.text(0.02, 0.95, '', transform=ax.transAxes)
# time_step = 1000.*(t1-t0)/N
# ax.set_xlabel('x (m)')
# ax.set_ylabel('y (m)')

# def init():
#     line.set_data([],[])
#     time_text.set_text('')
#     return line, time_text

# def animate(i):
#     XP = [0.,X1[i]]
#     YP = [0.,Y1[i]]
#     line.set_data(XP,YP)
#     time = i*time_step
#     time_text.set_text('time=%.1f ms' % time)
#     return line, time_text

# # The animation is created here
# anim = animation.FuncAnimation(fig, animate, init_func=init,frames=N, interval=time_step, blit=True)

# # Save the animation to an mpeg file. This requires ffmpeg to be installed,
# # with the executable in the PATH
# #anim.save('doublePendulum.mp4', fps=30, extra_args=['-vcodec', 'libx264'])

# # Display the animation
# plt.show()
# %%
