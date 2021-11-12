# 2. Dana jest lista:
# lista = [7, 49, 3, 9, 18, 6, 5, 25, 24, 4, 4, 5, 3, 19, 71, 21]
# Oblicz sumę, wartość średnią, wartość minimalną
# i maksymalną z wykorzstaniem i bez korzystania z
# funkcji wbudowanych sum, min, max, count.
import math

lista = [7, 49, 3, 9, 18, 6, 5, 25, 24, 4, 4, 5, 3, 19, 71, 21]

array_sum = sum(lista)
array_avg = array_sum / len(lista)
array_min = min(lista)
array_max = max(lista)

array_sum2 = 0
array_min2 = math.inf
array_max2 = -math.inf
for i in range(0, len(lista)):
    array_sum2 += lista[i]
    if lista[i] < array_min2:
        array_min2 = lista[i]
    if lista[i] > array_max2:
        array_max2 = lista[i]
array_avg2 = array_sum2 / len(lista)

print(array_sum, " : ", array_sum2)
print(array_avg, " : ", array_avg2)
print(array_min, " : ", array_min2)
print(array_max, " : ", array_max2)