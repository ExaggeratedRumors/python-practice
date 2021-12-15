# wygeneruj pary liczb całkowitych x i y losowo z zakresu x (0,100) y (0,100)
# i przedstaw w postaci punktów rozkład tych punktów na płaszczyźnie x,y.

from pylab import *
import random
import matplotlib.pyplot as plt

x = []
y = []
for i in range(0, 10):
    x.append(random.randint(0,100))
    y.append(random.randint(0,100))

fig = plt.figure()
ax = fig.add_subplot(111)

scatter(x, y, s=100, marker='o')

[plot([dot_x, dot_x], [0, dot_y], '-', linewidth=1) for dot_x, dot_y in zip(x, y)]
[plot([0, dot_x], [dot_y, dot_y], '-', linewidth=1) for dot_x, dot_y in zip(x, y)]

left, right = ax.get_xlim()
low, high = ax.get_ylim()
arrow(left, 0, right - left, 0, length_includes_head=True, head_width=0.15)
arrow(0, low, 0, high - low, length_includes_head=True, head_width=0.15)

grid()
show()
