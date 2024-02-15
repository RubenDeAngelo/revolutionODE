import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

time_end = 100


alpha_r1 = lambda r1, N1: 5 * r1 / (N1 - r1) if r1 <N1 else 0
alpha_n1 = lambda r1, N1: 3 * (N1 - r1) / r1 if r1 < N1 else np.inf

alpha_r2 = lambda r2, N2: 4 * r2 / (N2 - r2) if r2 < N2 else 0
alpha_n2 = lambda r2, N2: 2 * (N2 - r2) / r2 if r2 < N2 else np.inf

N1 = 100
N2 = 500
lambda12 = 5
lambda21 = 4


def system_time(t, y):
    r1, r2 = y
    a = alpha_r1(r1, N1)
    b = alpha_n1(r1, N1)
    dr1dt = max(0,
                1 / N1 * alpha_r1(r1, N1) * r1 * (N1 - r1) - alpha_n1(r1, N1) * r1 + lambda12 * r2 * (N1 - r1) * 1 / N1)
    dr2dt = max(0,
                1 / N2 * alpha_r2(r2, N2) * r2 * (N2 - r2) - alpha_n2(r2, N2) * r2 + lambda21 * r1 * (N2 - r2) * 1 / N2)
    return [dr1dt, dr2dt]


r1_0 = 0.5 * N1
r2_0 = 0.2 * N2

t_span = (0, time_end)
t_eval = np.linspace(t_span[0], t_span[1], 1000)

solution_time = solve_ivp(system_time, t_span, [r1_0, r2_0], t_eval=t_eval)

plt.plot(solution_time.t, solution_time.y[0], label='r1(t) - social pressure rates', linestyle='-')
plt.plot(solution_time.t, solution_time.y[1], label='r2(t) - social pressure rates', linestyle='-')
plt.xlabel('Zeit t')
plt.ylabel('Lösungen r1 und r2')
plt.legend()
plt.grid(True)
plt.show()
