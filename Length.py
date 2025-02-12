import numpy as np


def calc_length(a, b, f):
    h = 0.001
    x = a
    y = f(x)
    length = 0
    while x < b:
        x += h
        y_next = f(x)
        length += np.sqrt(h ** 2 + (y_next - y) ** 2)
        y = y_next
    return length


def f1(x):
    return np.cos(x)


def f2(x):
    return np.cos(x) + 0.1 * x ** 2


def f3(x):
    return -np.tanh(x - np.pi / 2)


def f4(x):
    return -0.2 * (x - np.pi) ** 3 + 0.5 * (x - np.pi) ** 2 + 1


print(calc_length(0, np.pi, f1))
print(calc_length(0, np.pi, f2))
print(calc_length(0, np.pi, f3))
print(calc_length(0, np.pi, f4))
