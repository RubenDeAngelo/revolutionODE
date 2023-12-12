import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Define the ODE function dr/dt = r(1 - r) - gamma * r
def model(r, t, gamma):
    return r * (1 - r) - gamma * r

# Define the initial condition
r0 = 0.1  # Initial value of r
alpha = 1
beta = 2
gamma = 0.1  # Gamma value
if gamma is None:
    gamma = beta / alpha

# Create an array of time values
t = np.linspace(0, 10, 100)  # Start at 0, end at 10, 100 points in between

# Solve the ODE
r = odeint(model, r0, t, args=(gamma,))

# Calculate n = 1 - r
n = 1 - r

# Plot both r and n in the same plot
plt.figure(figsize=(8, 6))

plt.plot(t, r, label='r(t)', color='blue')
plt.plot(t, n, label='n(t) (1 - r(t))', color='red', linestyle='--')  # Plotting n = 1 - r
plt.xlabel('Time')
plt.ylabel('Value')
plt.title(r'$\gamma = $' + f'{gamma}')  # Display gamma as a Greek symbol
plt.legend()
plt.grid(True)
plt.ylim(0, 1)  # Set y-axis range from 0 to 1

plt.show()
