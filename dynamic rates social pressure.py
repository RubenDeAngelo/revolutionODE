import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

time_end = 10

alpha_r1 = lambda r1, N1: 5 * r1 / (N1 - r1)
alpha_n1 = lambda r1, N1: 3 * (N1 - r1)/r1

alpha_r2 = lambda r2, N2: 4 * r2/(N2 - r2)
alpha_n2 = lambda r2, N2: 2 * (N2 - r2)/r2

N1 = 100
N2 = 500
lambda12 = 5
lambda21 = 1

def system_time(t, y):
    r1, r2 = y
    dr1dt = 1/N1 * alpha_r1(r1,N1) * r1 * (N1-r1) - alpha_n1(r1,N1)*r1 + lambda12*r2*(N1-r1) * 1/N1
    dr2dt = 1/N2 * alpha_r2(r2,N2) * r2 * (N2-r2) - alpha_n2(r2,N2)*r2 + lambda21*r1*(N2-r2) * 1/N2
    return [dr1dt, dr2dt]

r1_0 = 0.5 * N1
r2_0 = 0.2 * N2

t_span = (0, time_end)
t_eval = np.linspace(t_span[0], t_span[1], 1000)

solution_time = solve_ivp(system_time, t_span, [r1_0, r2_0], t_eval=t_eval)

plt.plot(solution_time.t, solution_time.y[0], label='r1(t) - time-dependent rates', linestyle='-')
plt.plot(solution_time.t, solution_time.y[1], label='r2(t) - time-dependent rates', linestyle='-')
plt.xlabel('Zeit t')
plt.ylabel('Lösungen r1 und r2')
plt.legend()
plt.show()
