# 5. Liczenie wartości funkcji podanej z klawiatury np. (x*x+2*x+4 lub 1/(x+1))
# (wykorzystać funkcję eval())
# oraz zapisanie do pliku wzoru oraz obliczenie 500 elementów od 0 do 50 o kroku 0.1

import numpy as np

x = np.arange(.0, 50., 0.1)
fun = input("Podaj funkcję:")
with open("zad6.txt", 'w') as file:
    file.write(fun)

with open("zad6.txt", 'r') as file:
    read_fun = file.readline()
result = eval(read_fun)
print(result)