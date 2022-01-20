import matplotlib.pyplot as plt
import numpy

N = 100
x = numpy.arange(1, 11, 1)
print(x)
labels = [f"Próbka {i}" for i in x]

y = [[i for i in range(1, N + 1)] for sample in x]

plt.plot(x, y, 'b.', markersize=1)
plt.title("Lab13")
plt.xticks(x, labels, fontsize=6, rotation=45)
plt.show()
