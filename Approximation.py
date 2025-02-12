import numpy as np

with open(mode='r', file='data.csv') as f:
    data = f.read().splitlines()
    data = data[1:]
    x = np.array([float(data[i].split(',')[0]) for i in range(len(data))])
    y = np.array([float(data[i].split(',')[1]) for i in range(len(data))])
    print(np.sum(x * y) / sum(x ** 2))
