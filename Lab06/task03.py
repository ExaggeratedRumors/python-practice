# 3. Dana jest lista:
# lista = [7, 49, 3, 9, 18, 6, 5, 25, 24, 4, 4, 5, 3, 19, 71, 21]
# Wykorzystaj moduł statistics (from statistics import *) i
# oblicz wartość średnią(mean), medianę (median),
# modę (mode), odchylenie standardowe (stdev),
# wariancję (variance)

from statistics import *

lista = [7, 49, 3, 9, 18, 6, 5, 25, 24, 4, 4, 5, 3, 19, 71, 21]

print(mean(lista),
      median(lista),
      mode(lista),
      stdev(lista),
      variance(lista)
      )
