import math
import numpy as np

def f(x):
    return math.sqrt(x ** 2 + 3) / x ** 2

def trapezoidal_method(a, b, n):
    h = (b - a) / n
    integral = 0.5 * (f(a) + f(b))

    for i in range(1, n):
        x_i = a + i * h
        integral += f(x_i)
    
    integral *= h
    return integral

a = 1
b = 2
n = 30

integral_trapezoidal = trapezoidal_method(a, b, n)

def true_solution(x):
    return -1 * (math.sqrt(x ** 2 + 3) / x) + np.log(x + math.sqrt(x ** 2 + 3))

true_integral = true_solution(b) - true_solution(a)
print("The exact value of the integral:\n", true_integral)

error_trapezoidal = abs(true_integral - integral_trapezoidal)
print("Solution using the trapezium method:\n", integral_trapezoidal)
print("Calculation error with trapezium method:\n", error_trapezoidal)
