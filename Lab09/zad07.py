# 5. Liczenie wartości funkcji podanej z klawiatury np. (x*x+2x+4 lub 1/(x+1))
# (wykorzystać funkcję eval())
# oraz zapisanie do pliku binarnego wartości x oraz y od 0 do 50 o kroku 0.1.
# Następnie czytamy dane z pliku binarnego.


import numpy as np
import codecs
import re

x = np.arange(.0, 50., 0.1)
fun = input("Podaj funkcję: ")
result = eval(fun)
data = np.column_stack((x, result))
data = [np.array2string(line) for line in data]
with codecs.open("zad7.txt", 'wb', 'utf-8') as file:
    for i in data:
        file.write(i + '\n')

with codecs.open("zad7.txt", 'rb', 'utf-8') as file:
    result = [re.sub('[\n]', '', line) for line in file]

for i in result:
    print(i)
