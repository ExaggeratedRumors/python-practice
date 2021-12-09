# Narysuj trzy funkcje na jednym wykresie
import matplotlib.pyplot as plt
import numpy as np

# evenly sampled time at 200ms intervals
t = np.arange(-5., 5., 0.2)

# red dashes, blue squares and green triangles
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3/100, 'g^')
plt.grid(True)
plt.axhline(0, color='#F00')
plt.axvline(0, color='#F00')
plt.show()
