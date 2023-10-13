import numpy as np
import matplotlib.pyplot as plt

# Function to find the root of ln(x) + x = 0
def equation(x):
    return np.log(x) + x

# Bisection method
def bisection_method(a, b, tol=1e-6, max_iter=100):
    if equation(a) * equation(b) >= 0:
        print("Bisection method may not converge.")
        return None

    iterations = 0
    while (b - a) / 2.0 > tol and iterations < max_iter:
        midpoint = (a + b) / 2.0
        if equation(midpoint) == 0.0:
            return midpoint
        elif equation(a) * equation(midpoint) < 0.0:
            b = midpoint
        else:
            a = midpoint
        iterations += 1

    return (a + b) / 2.0

# Define the interval [a, b]
a = 0.01
b = 16

# Perform the bisection method
root = bisection_method(a, b)

# Print the result
if root is not None:
    print(f"Approximate root: {root}")
else:
    print("Bisection method did not converge.")

# Create a plot to visualize the function and root
x = np.linspace(0.01, 16, 100)
y = equation(x)

plt.figure(figsize=(8, 6))
plt.plot(x, y, label="ln(x) + x")
if root is not None:
    plt.scatter([root], [equation(root)], color='red', label='Root')
plt.axhline(0, color='black', linestyle='--', linewidth=0.7)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.title('Bisection Method for ln(x) + x = 0')
plt.grid(True)
plt.show()
