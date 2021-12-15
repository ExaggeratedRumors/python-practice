# Na podstawie pliku dane.dat (z poprzednich zajęć) narysować wykres
# przedstwiający drogę w funkcji (czasu) s = f(t),
# gdzie s jest drogą przejechaną od początku jazdy
# i czas, także jest czasem od początku rozpoczęcia ruchu.


import numpy as np
import matplotlib.pyplot as plt

with open("dane.dat", 'r') as file:
    result = np.array([[float(val) for val in line.split()] for line in file if line[0] != '#'])

t = result[:, 0]
s = result[:, 1]

plt.plot(t, s)
plt.legend(loc='upper left')
plt.grid()
plt.show()

print(result)
