# 9. Z wykładu definiujemy funkcję silnia(a) i
# porównujemy wyniki z funkcją math.factorial().
# Śledzimy za pomocą debugera wykonanie rekurencyjne
# naszej funkcji silnia. Dodatkowo wykorzystujemy funkcję
# time() z biblioteki time do sprawdzenia,
# która z obliczeń działa szybciej (sprawdzić dla dość duzych liczb)
import math
import time


def silnia(n):
    if n > 1:
        return n * silnia(n - 1)
    else:
        return 1


val = 575
estimate = 1000

t1 = time.time()
for i in range(1, estimate):
    silnia(val)
t2 = time.time()
print('Funkcja silnia: ', t2 - t1)

t1 = time.time()
for i in range(1, estimate):
    math.factorial(val)
t2 = time.time()
print('Funkcja factorial: ', t2 - t1)
