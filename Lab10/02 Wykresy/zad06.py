# Rysujemy funkcję f(x) = 1/(x+1) z wybranego zakresu,
# który przynajmniej obejmuję zakres x (-5,5) oraz y (-10,10). Uwaga na wartość x = -1.

import numpy as np
import matplotlib.pyplot as plt


def f(d):
    return 1 / d


np.seterr(divide='ignore', invalid='ignore')

x = np.linspace(-5, 5, 101)
y = f(x)

fx_name = r'$f(x)=\frac{1}{x}$'
plt.plot(x, y, label=fx_name)
plt.legend(loc='upper left')
plt.grid()
ax = plt.gca()
ax.set_ylim([-10, 10])
plt.show()
