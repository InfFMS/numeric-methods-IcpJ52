import numpy as np


def square(a, b, f):
    h = 0.001
    x = a
    y = f(x)
    area = 0
    while x < b:
        x += h
        y_next = f(x)
        area += 0.5 * (y + y_next) * h
        y = y_next
    return area


def f11(x):
    return np.sin(2 * x) + 1


def f12(x):
    return -0.2 * x ** 2 + 0.5


def f21(x):
    return np.cos(x) + 1.2


def f22(x):
    return -0.5 * x ** 2 + 0.7


def f31(x):
    return np.exp(-x ** 2) + 1


def f32(x):
    return -0.3 * x ** 3 + 0.5


def f41(x):
    return np.exp(-x ** 2) + 0.5


def f42(x):
    return 0.2 * np.sin(3 * x) - 0.5


def f51(x):
    return np.exp(-(x + 1) ** 2) + np.exp(-(x - 1) ** 2) + 0.5


def f52(x):
    return -0.3 * x ** 2


print(abs(square(0, np.pi, f11) - square(0, np.pi, f12)))
print(abs(square(-np.pi / 2, np.pi / 2, f21) - square(-np.pi / 2, np.pi / 2, f22)))
print(abs(square(-2, 2, f31) - square(-2, 2, f32)))
print(abs(square(-2, 2, f41) - square(-2, 2, f42)))
print(abs(square(-2, 2, f51) - square(-2, 2, f52)))
