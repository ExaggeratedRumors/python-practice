# 3. Wylosować 5000 liczb całkowitych z przedziału od 1 do 9
# i sprawdzić ile razy wystąpiła liczba 3 oraz 7.
import random

estimate = 5000
n_min = 1
n_max = 9
counter_three = 0
counter_seven = 7

for i in range(0, estimate):
    n = random.randint(n_min, n_max)
    if n == 3:
        counter_three += 1
    elif n == 7:
        counter_seven += 1

print(f"Liczba wystąpień liczby 3: {counter_three}\n"
      f"Liczba wystąpień liczby 7: {counter_seven}")