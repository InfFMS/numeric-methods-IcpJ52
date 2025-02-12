import numpy as np

n1 = float(input())
n2 = float(input())
y1 = float(input())  # Горизонтальная прямая, на которой расположена точка старта
y2 = float(input())  # Горизонтальная прямая, на которой расположена точка финиша


def find_min_distance(x, n1=n1, n2=n2, y1=y1, y2=y2):
    return y1 * n1 / np.sin(x) + y2 * n2 / np.sqrt(1 - n1 ** 2 / n2 ** 2 * np.cos(x) ** 2)


def find_min(a, b, f, eps):
    while b - a > 2 * eps:
        mid1 = a + (b - a) / 3
        mid2 = b - (b - a) / 3
        if f(mid1) < f(mid2):
            b = mid2
        else:
            a = mid1
    return (a + b) / 2


print(find_min(0, np.pi / 2, find_min_distance, 0.01))
