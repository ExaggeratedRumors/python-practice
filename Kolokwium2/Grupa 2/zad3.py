import matplotlib.pyplot as plt
import numpy

MIN_VAL = -500
MAX_VAL = 500
krok = 0.1

# Komentarz:
# Przy kroku 0.1 nie zaobserwujemy dokładnie
# krzywizny funkcji w pobliżu asymptoty x=3
# Żeby funkcja oddawała rzeczywisty przebieg należy odpowiednio
# zmniejszyć krok np: krok = 0.001

x = numpy.arange(-10, 10, krok)
y = x ** 3 + 2 / (x - 3)
y1 = []
for i in y:
    if MIN_VAL < i < MAX_VAL:
        y1.append(i)
    else:
        y1.append(numpy.NaN)
y = y1[:]

plt.plot(x, y, 'b-', markersize=5)
plt.title("y = x^3 + 2/(x-3)")
plt.grid()
ax = plt.gca()
ax.set_ylim([MIN_VAL, MAX_VAL])
ax.set_xlim([-10, 10])
plt.show()
