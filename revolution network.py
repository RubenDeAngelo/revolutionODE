import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Define the ODE system for r1 and r2
def model(z, t, gamma, w12, w21):
    r1, r2 = z
    dr1dt = r1 * (1 - r1) - gamma * r1 + w12 * r2 * (1 - r1)
    dr2dt = r2 * (1 - r2) - gamma * r2 + w21 * r1 * (1 - r2)
    return [dr1dt, dr2dt]

# Define the initial conditions and parameters
N1 = 1.5
N2 = 0.5
r1_0 = 0.1
r2_0 = 0.1
gamma = 0.2
w12 = 0.2 * N2
w21 = 5 * N1

# Create an array of time values
t = np.linspace(0, 20, 1000)

# Solve the ODE system
z0 = [r1_0, r2_0]
z = odeint(model, z0, t, args=(gamma, w12, w21))
r1, r2 = z[:, 0], z[:, 1]

# Calculate n1 = 1 - r1 and n2 = 1 - r2
n1 = 1 - r1
n2 = 1 - r2

# Plot r1 with n1 and r2 with n2 in subplots
plt.figure(figsize=(10, 8))

plt.subplot(2, 1, 1)
plt.plot(t, r1, label='r1(t)', color='blue')
plt.plot(t, n1, label='n1(t) (1 - r1(t))', color='red', linestyle='--')
plt.xlabel('Time')
plt.ylabel('Value')
plt.title('Solution for $r_1(t)$ and $n_1(t) = 1 - r_1(t)$')
plt.text(0.5, 0.85, r'$\gamma = {}$'.format(gamma), fontsize=12)
plt.text(0.5, 0.75, r"$w_{12}$ = " + str(w12), fontsize=12)
plt.text(0.5, 0.65, r'$N_{1}$ = '+ str(N1), fontsize=12)
plt.legend()
plt.grid(True)
plt.ylim(0, 1)

plt.subplot(2, 1, 2)
plt.plot(t, r2, label='r2(t)', color='green')
plt.plot(t, n2, label='n2(t) (1 - r2(t))', color='orange', linestyle='--')
plt.xlabel('Time')
plt.ylabel('Value')
plt.title('Solution for $r_2(t)$ and $n_2(t) = 1 - r_2(t)$')
plt.text(0.5, 0.85, r'$\gamma = {}$'.format(gamma), fontsize=12)
plt.text(0.5, 0.75, r"$w_{21}$ = " + str(w21), fontsize=12)
plt.text(0.5, 0.65, r'$N_{2}$ = '+ str(N2), fontsize=12)
plt.legend()
plt.grid(True)
plt.ylim(0, 1)

plt.tight_layout()
plt.show()
