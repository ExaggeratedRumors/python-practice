# 3. Wykorzystanie modułu pickle do zapisania
# wygenerowanych 10000 liczb całkowitych o wartości od 0 do 100.
# Następnie czytamy dane z danego pliku i szukamy, które z wygenerowanych liczb jest najwięcej.

import pickle
import random
import statistics

array = [random.randint(0, 100) for i in range(0, 10000)]

with open('zad4.pickle', 'wb') as handle:
    pickle.dump(array, handle, protocol=pickle.HIGHEST_PROTOCOL)

with open('zad4.pickle', 'rb') as handle:
    result = pickle.load(handle)

print(f"Najwięcej pojawień liczby: {statistics.mode(result)}")