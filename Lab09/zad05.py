# 4. Wykorzystanie modułu shelve do zapisania rzutów dwoma kostkami,
# aż do wyrzucenia wartości 12 (zapisujemy kolejne sumy).
# Powtarzamy tą operację jeszcze 100 razy i każdą z serii zapisujemy do nowego zestawu danych.
# Następnie czytamy dane z danego pliku i podajemy ile rzutów potrzebujemy, w każdej serii
# do wyrzucenia sumy równej 12. Następnie liczymy jedną wartość średnią z wszystkich serii.

import shelve
import random


def dice_blackjack():
    throw = 0
    history = []
    while True:
        throw = random.randint(1, 6) + random.randint(1, 6)
        history.append(str(throw))
        if throw == 12:
            break
    return history


data = shelve.open("zad5")
for i in range(0, 100):
    data[str(i + 1)] = dice_blackjack()
data.sync()
data.close()

data = shelve.open("zad5")
throws_sum = 0
for i in data.keys():
    print(f"Seria {i}: {len(data.get(i))} rzutów")
    throws_sum += len(data.get(i))
avg = throws_sum / len(data.keys())
print(f"Średnia rzutów: {avg}")
data.close()
