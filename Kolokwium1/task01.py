# 1. Podaj listę o dowolnej liczbie elementów
# typu int na stałe w programie
# (np. lista=[2,452,35,49,4,3,6,4,2,4,45,23,12,23,2,24,8,4,7,14])
# i oblicz sumę i wartość średnią tylko liczb podzielnych przez 4 lub 7.

lista=[2,452,35,49,4,3,6,4,2,4,45,23,12,23,2,24,8,4,7,14]

suma = 0
for i in lista:
    if i % 4 == 0 or i % 7 == 0:
        suma += i

avg = suma/len(lista)

print(f"Suma wybranych elementów listy: {suma}\n"
      f"Wartość średnia wybranych elementów listy: {avg}")