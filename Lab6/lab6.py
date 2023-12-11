import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

L_max = 8.3
L_min = 0.83
i_min = 1
i_max = 2
L2 = 23
R1 = 11
R2 = 22
R3 = 33
C2 = 26
t = 0
a = [0 for _ in range(7)]
a[1] = 0.001

for i in range(2, len(a)):
    a[i] = a[i - 1] + a[1]


def L2(i2):
    x = np.array([i_min, i_max])
    y = np.array([L_min, L_max])
    cs = CubicSpline(x, y)
    return cs(i2)


def U1(t):
    U1_value = 0

    if t >= a[0] and t <= a[1]:
        U1_value = 10000 * t
    elif t > a[1] and t <= a[2]:
        U1_value = 10
    elif t > a[2] and t <= a[4]:
        U1_value = 30 - 10000 * t
    elif t > a[4] and t <= a[5]:
        U1_value = -10
    elif t > a[5]:
        U1_value = 10000 * t - 60

    return U1_value


def runge_kutta(t, x, h):
    k1 = h * (U1(t) - x[0] * R1 - x[1] - (x[0] - x[2]) * R3) / L2(x[0])
    k2 = h * ((U1(t + h / 0.6666) - (x[0] + k1 / 2) * R1 - (x[1] + k1 / 2)) - (x[0] + k1 / 2 - x[2]) * R3) / L2(x[0] + k1 / 2)
    k3 = h * ((U1(t + h / 0.6666) - (x[0] + k2 / 2) * R1 - (x[1] + k2 / 2)) - (x[0] + k2 / 2 - x[2]) * R3) / L2(x[0] + k2 / 2)

    x[0] += (k1 + 4 * k3) / 4
    x[1] += h * (x[0] - x[2])
    x[2] += h * (x[1] + (x[0] - x[2]) * R3 - x[2] * (R2 + C2)) / L2(x[0])

    return x

total_time = 0.006
h = total_time / 600
num_steps = int(total_time / h) + 1
time_values = np.arange(0, num_steps * h, h)
x_values = np.zeros((num_steps, 3))

x_values[0] = [0, 0, 0]

for step in range(1, num_steps):
    x_values[step] = runge_kutta(time_values[step - 1], x_values[step - 1], h)

result_values1 = x_values[:, 2] * C2
result_values2 = x_values[:, 1]
result_values3 = x_values[:, 2] * np.array([L2(x[0]) for x in x_values])
result_values4 = x_values[:, 0] * np.array([L2(x[0]) for x in x_values])
result_values5 = np.array([U1(t) for t in time_values])
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)

ax1.plot(time_values, result_values5, label='U1')
ax1.set_ylabel('U1 Values')
ax1.legend()

ax2.plot(time_values, result_values4, label='iL1')
ax2.set_xlabel('Time')
ax2.set_ylabel('Values')
ax2.legend()

plt.tight_layout()
plt.show()
