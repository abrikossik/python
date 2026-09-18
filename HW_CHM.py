from IPython.display import HTML
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import glob
from collections import defaultdict
from draw import *

import pickle
with open('LipsArrayHalfTime.np' , 'rb') as f:
    LipsData = pickle.load(f)


def lagrange(t_nodes, y_nodes, t):
    """
    t_nodes - известные значения времени
    y_nodes - известные значения координаты
    t       - момент времени, в котором нужно найти значение
    """

    result = 0.0

    for i in range(len(t_nodes)):
        basis = 1.0

        for j in range(len(t_nodes)):
            if i != j:
                basis *= (t - t_nodes[j]) / (t_nodes[i] - t_nodes[j])

        result += y_nodes[i] * basis

    return result

Task1LispPoints = {}

for letter, data in LipsData.items():

    n = data.shape[0]

    t_nodes = np.arange(n, dtype=float)
    new_times = np.arange(0, n - 0.5 + 0.001, 0.5)

    result = np.zeros((len(new_times), 40, 2), dtype=float)

    for k, t in enumerate(new_times):
        for point in range(40):
            x_values = data[:, point, 0]
            y_values = data[:, point, 1]

            new_x = lagrange(t_nodes, x_values, t)
            new_y = lagrange(t_nodes, y_values, t)

            result[k, point, 0] = new_x
            result[k, point, 1] = new_y

    Task1LispPoints[letter] = result


for letter, data in Task1LispPoints.items():
    print(f"Буква {letter}: {data.shape}")

animate_lips(Task1LispPoints['В'], interval=100)