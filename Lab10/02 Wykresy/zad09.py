# Narysuj funkcję cos(2*pi*x) oraz cos(2*pi*x)*exp(x) na jednym wykresie
# dla x z zakresu <0, 2*pi>

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import CheckButtons

x = np.arange(0.0, 2.0 * np.pi, 0.01)
y1 = np.sin(2 * np.pi * x)
y2 = np.cos(2 * np.pi * x) * np.exp(x)

fig, ax = plt.subplots()
p1, = ax.plot(x, y1, lw=2, color='y', label='sin')
p2, = ax.plot(x, y2, lw=2, color='r', label='cos')

ax.legend()
plt.subplots_adjust(left=.25)
plt.grid(True)

lines = [p1, p2]

rax = plt.axes([0.0, 0.8, 0.175, 0.15])
labels = [str(line.get_label()) for line in lines]
visibility = [line.get_visible() for line in lines]
check = CheckButtons(rax, labels, visibility)

def func(label):
    index = labels.index(label)
    lines[index].set_visible(not lines[index].get_visible())
    plt.draw()

check.on_clicked(func)

plt.show()