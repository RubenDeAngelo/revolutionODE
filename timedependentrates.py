import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Parameter
# =============================================================================
# alpha_r1 = 5   
# alpha_n1 = 2
# alpha_r2 = 9
# alpha_n2 = 1
# =============================================================================

# =============================================================================
# alpha_r1 = lambda r1: r1/(1-r1)   
# alpha_n1 = lambda r1: (1-r1)/r1
# alpha_r2 = lambda r2: r2/(1-r2)
# alpha_n2 = lambda r2: (1-r2)/r2
# =============================================================================

time_end = 20

#alpha_r1 = lambda t: 5 + (3/time_end)*t
#alpha_n1 = lambda t: 2 - (1/time_end)*t
#alpha_r2 = lambda t: 3 - (2/time_end)*t
#alpha_n2 = lambda t: 1 - (0.5/time_end)*t
np.sin(time_end)
alpha_r1 = lambda t: 5 + 3 *np.sin(t)
alpha_n1 = lambda t: 2 - 1 *np.sin(t)
alpha_r2 = lambda t: 3 - 2*np.sin(t)
alpha_n2 = lambda t: 1 - 0.5*np.sin(t)


N1 = 100
N2 = 500
lambda12 = 5
lambda21 = 1

# =============================================================================
# gamma1 = alpha_n1/alpha_r1  
# gamma2 = alpha_n2/alpha_r2  
# beta12 = lambda12/alpha_r1 * N1/N2  
# beta21 = lambda21/alpha_r2 * N2/N1  
# =============================================================================

# ODE-System

# Not working
# =============================================================================
# # =============================================================================
# # def system(t, y):
# #     r1, r2 = y
# #     dr1dt = 1/N1 * alpha_r1 * r1**2 - alpha_n1*(1-r1) + lambda12*r2*(1-r1) * 1/N1
# #     dr2dt = 1/N2 * alpha_r2 * r2**2 - alpha_n2*(1-r2) + lambda21*r1*(1-r2) * 1/N2
# #     return [dr1dt, dr2dt]
# # =============================================================================
# 
# # =============================================================================
# # def system(t, y):
# #     r1, r2 = y
# #     dr1dt = r1**2 - gamma1*(1-r1) + beta12*r2*(1-r1)
# #     dr2dt = r2**2 - gamma2*(1-r2) + beta21*r1*(1-r2)
# #     return [dr1dt, dr2dt]
# # =============================================================================
# =============================================================================
t_values = np.linspace(0, time_end, 1000)

plt.plot(t_values, alpha_r1(t_values), label=r'$\alpha_{r1}(t)$', linestyle='-', linewidth=4)
plt.plot(t_values, alpha_n1(t_values), label=r'$\alpha_{n1}(t)$', linestyle='--', linewidth=4)
plt.plot(t_values, alpha_r2(t_values), label=r'$\alpha_{r2}(t)$', linestyle=':', linewidth=4)
plt.plot(t_values, alpha_n2(t_values), label=r'$\alpha_{n2}(t)$', linestyle='-.', linewidth=4)

plt.xlabel('Time t', fontsize=30)  # Adjust font size
plt.ylabel(r'$\alpha(t)$ values', fontsize=30)  # Adjust font size
plt.xticks(fontsize=30)
plt.yticks(fontsize=30)
plt.legend(fontsize=25)  # Adjust font size
plt.grid(True)
plt.show()
# Time-dependent rates
def system_time(t, y):
    r1, r2 = y
    a = alpha_r1(t)
    b=alpha_n1(t)
    dr1dt = 1/N1 * alpha_r1(t) * r1 * (N1-r1) - alpha_n1(t)*r1 + lambda12*r2*(N1-r1) * 1/N1
    dr2dt = 1/N2 * alpha_r2(t) * r2 * (N2-r2) - alpha_n2(t)*r2 + lambda21*r1*(N2-r2) * 1/N2
    return [dr1dt, dr2dt]
# Rate constant = starting value of time-dependent
def system(t, y):
    r1, r2 = y
    dr1dt = 1/N1 * alpha_r1(0) * r1 * (N1-r1) - alpha_n1(0)*r1 + lambda12*r2*(N1-r1) * 1/N1
    dr2dt = 1/N2 * alpha_r2(0) * r2 * (N2-r2) - alpha_n2(0)*r2 + lambda21*r1*(N2-r2) * 1/N2
    return [dr1dt, dr2dt]

# =============================================================================
# def system(t, y):
#     r1, r2 = y
#     dr1dt = 1/N1 * alpha_r1 * r1 * (N1-r1) - alpha_n1*r1 + lambda12*r2*(N1-r1) * 1/N1
#     dr2dt = 1/N2 * alpha_r2 * r2 * (N2-r2) - alpha_n2*r2 + lambda21*r1*(N2-r2) * 1/N2
#     return [dr1dt, dr2dt]
# =============================================================================

# =============================================================================
# def system(t, y):
#     r1, r2 = y
#     dr1dt = r1 * (1-r1) - gamma1*r1 + beta12*r2*(1-r1)
#     dr2dt = r2 * (1-r2) - gamma2*r2 + beta21*r1*(1-r2)
#     return [dr1dt, dr2dt]
# =============================================================================

# Anfangsbedingungen
# =============================================================================
# r1_0 = 0.5  # Anpassbar
# r2_0 = 0.2  # Anpassbar
# =============================================================================

r1_0 = 0.5 * N1  # Anpassbar
r2_0 = 0.2 * N2 # Anpassbar

# Zeitbereich für die Simulation
t_span = (0, time_end)  # Von t=0 bis t=10
t_eval = np.linspace(t_span[0], t_span[1], 1000)  # Zeitpunkte für die Lösung

# Lösen des ODE-Systems
solution_time = solve_ivp(system_time, t_span, [r1_0, r2_0], t_eval=t_eval)
solution = solve_ivp(system, t_span, [r1_0, r2_0], t_eval=t_eval)

# Plotten der Lösung
plt.plot(solution.t, solution_time.y[0], label='r1(t) - dynamic rates', linestyle='-', linewidth=4)
plt.plot(solution.t, solution_time.y[1], label='r2(t) - dynamic rates', linestyle='-', linewidth=4)
plt.plot(solution.t, solution.y[0], label='r1(t)', color='C0', linestyle='--', linewidth=4)
plt.plot(solution.t, solution.y[1], label='r2(t)', color='C1', linestyle='--', linewidth=4)

plt.xlabel('Time t', fontsize=30)
plt.ylabel('r1 and r2 (People)', fontsize=30)
plt.xticks(fontsize=30)
plt.yticks(fontsize=30)
plt.legend(fontsize=25)
plt.grid(True)
plt.show()
