import numpy as np

n1 = float(input())
n2 = float(input())
y1 = float(input())
y2 = float(input())
x1 = float(input())
x2 = float(input())


def f1(x, n1=n1, n2=n2, y1=y1, y2=y2, x1=x1, x2=x2):
    return n1 * (x - x1) / np.sqrt(y1 ** 2 + (x - x1) ** 2) - n2 * (x2 - x) / np.sqrt(y2 ** 2 + (x2 - x) ** 2)


def f2(x, n1=n1, n2=n2, y1=y1, y2=y2, x1=x1, x2=x2):
    return n1 * np.sqrt(y1 ** 2 + (x - x1) ** 2) + n2 * np.sqrt(y2 ** 2 + (x2 - x) ** 2)


def find_min(a, b, f, eps):
    while b - a > 2 * eps:
        mid1 = a + (b - a) / 3
        mid2 = b - (b - a) / 3
        if f(mid1) < f(mid2):
            b = mid2
        else:
            a = mid1
    return (a + b) / 2


def solve_equation(a, b, f, eps):
    while b - a >= 2 * eps:
        c = (a + b) / 2
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c
    return c


print(find_min(x1, x2, f2, 0.01))
print(solve_equation(x1, x2, f1, 0.01))
