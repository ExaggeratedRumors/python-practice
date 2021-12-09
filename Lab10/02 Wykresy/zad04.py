# 1. Rysowanie funkcji sin, cos, 2 cos, cos ( .. + 45) na jednym wykresie (2 okresy)

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import CheckButtons

x = np.arange(0.0, 2 * np.pi, 0.01)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = 2 * np.cos(x)
y4 = np.cos(x + np.pi*45/180)

fig, ax = plt.subplots()
p1, = ax.plot(x, y1, lw=2, color='y', label='sin')
p2, = ax.plot(x, y2, lw=2, color='r', label='cos')
p3, = ax.plot(x, y3, lw=2, color='b', label='2cos')
p4, = ax.plot(x, y4, lw=2, color='g', label='cos(x+pi/4')
ax.legend()
plt.subplots_adjust(left=.25)
plt.grid(True)

lines = [p1, p2, p3, p4]

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
