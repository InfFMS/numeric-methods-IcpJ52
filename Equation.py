import numpy as np


def solve_equation(a, b, f, eps):
    while b - a >= 2 * eps:
        c = (a + b) / 2
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c
    return c


# Есть 1 корень на отрезке от -2 до -1
def f1(x):
    return x ** 3 - x + 1


# Есть 3 корня на отрезке от -4 до -2, от -2 до 2, от 2 до 4
def f2(x):
    return x ** 3 - x ** 2 - 9 * x + 9


# Есть 1 корень на отрезке от -2 до 2
def f3(x):
    return x ** 2 - np.exp(x)


# Есть 2 корня на отрезке от 0 до 2, от 2 до 4
def f4(x):
    return 5 * x - 6 * np.log(x) - 7


# Есть 1 корень на отрезке от 1 до 1.5
def f5(x):
    return np.cos(x) + 2 * x - 3


print(solve_equation(-2, -1, f1, 0.01))
print('\n')
print(solve_equation(-4, -2, f2, 0.01), solve_equation(-2, 2, f2, 0.01), solve_equation(2, 4, f2, 0.01), sep='\n')
print('\n')
print(solve_equation(-2, 2, f3, 0.01))
print('\n')
print(solve_equation(0.0001, 2, f4, 0.01), solve_equation(2, 4, f4, 0.01), sep='\n')
print('\n')
print(solve_equation(1, 1.5, f5, 0.01))
