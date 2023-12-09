import numpy as np

m = 2
q = 2
p = 10
n = 2 * q + 1
x0 = np.array([0.5, 0])
epsilon = 1e-5

def f1(x):
    return x[0] ** 2 + x[1] ** 2 + 0.1 - x[0]

def f2(x):
    return 2 * x[0] * x[1] - 0.1 - x[1]

def OR(cond1, cond2):
    return cond1 or cond2

for _ in range(p):
    S = np.zeros((n, m))
    Sn = np.zeros((n, m))
    cond = True

    for k in range(-1, n - 1):
        for i in range(m):
            if k == -1:
                Sn[k + 1, i] = x0[i]
            else:
                Sn[k + 1, i] = Sn[k, i] + (1 / (2 ** k)) * S[k, i]

        S[k + 1, 0] = f1(Sn[k + 1, :])
        S[k + 1, 1] = f2(Sn[k + 1, :])

        if k >= 1:
            cond = cond and OR(abs(S[k, 0]) < abs(S[k - 1, 0]), abs(S[k, 1]) < abs(S[k - 1, 1]))

    if not cond:
        break

    if p == 1:
        break

result = Sn[n - 1, :]

print("Result:")
print(f"x1 = {result[0]}, x2 = {result[1]}")

print("\nCheck if result right:")
print(f"f1 = {f1(result)}, f2 = {f2(result)}")
