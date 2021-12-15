# Rysowanie funkcji sinx, cosx, sin2x, cos2x na czterech wykresach
# w jednym oknie w dowolnej konfiguracji

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import CheckButtons

x = np.arange(0.0, 2 * np.pi, 0.01)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.sin(2 * x)
y4 = np.cos(2 * x)

fig = plt.figure()
gs = fig.add_gridspec(4, hspace=0.5)
axs = gs.subplots(sharex=True, sharey=False)

axs[0].plot(x, y1, lw=2, color='y', label='sin')
axs[0].set_title('sinx')
axs[1].plot(x, y2, lw=2, color='r', label='cos')
axs[1].set_title('cosx')
axs[2].plot(x, y3, lw=2, color='b', label='2cos')
axs[2].set_title('sin2x')
axs[3].plot(x, y4, lw=2, color='g', label='cos(x+pi/4')
axs[3].set_title('cos2x')

plt.show()
