import numpy as np
import matplotlib.pyplot as plt

Umax = 100
f = 50
R1 = 5
R2 = 4
L1 = 0.01
C1 = 300e-6
C2 = 150e-6
t_int = 0.2
h = 0.00001
R3 = 7
L3 = 0.015
C3 = 200e-6


def model(i1, i2, i3, u1, u2, u3, t):
    U1 = Umax * np.sin(2 * np.pi * f * t)
    di1dt = (U1 - u1 - R1*i1) / C2
    di2dt = (u1 - u2 - L1*i2) / R2
    di3dt = (u2 - R3*i3) / L3
    du1dt = i1 / C1 - i2 / C2
    du2dt = i2 / C2 - i3 / C3
    du3dt = i3 / C3
    return di1dt, di2dt, di3dt, du1dt, du2dt, du3dt

i1, i2, i3, u1, u2, u3 = 0, 0, 0, 0, 0, 0

t = np.arange(0, t_int, h)

results = []
for time in t:
    di1dt, di2dt, di3dt, du1dt, du2dt, du3dt = model(i1, i2, i3, u1, u2, u3, time)
    i1 += h * di1dt
    i2 += h * di2dt
    i3 += h * di3dt
    u1 += h * du1dt
    u2 += h * du2dt
    u3 += h * du3dt
    results.append(u2)

input = []
for time in t:
    di1dt, di2dt, di3dt, du1dt, du2dt, du3dt = model(i1, i2, i3, u1, u2, u3, time)
    i1 += h * di1dt
    i2 += h * di2dt
    i3 += h * di3dt
    u1 += h * du1dt
    u2 += h * du2dt
    u3 += h * du3dt
    input.append(u1)
print(i1)
print(i2)
print(i3)
print(i4)
print(i5)

plt.plot(t, results)
plt.plot(t, input)

plt.xlabel('Час (C)')
plt.ylabel('Напруга U2 (B)')
plt.title('Перехідний процес вихідної напруги U2 (Метод Ейлера)')
plt.grid(True)
plt.show()


