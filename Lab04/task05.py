# 5. Losujemy liczby od 1-100 i po ilu losowaniach
# wartość będzie większa od 10000 ale tylko liczb parzystych.

import random


def sum_of_even_randoms(limit=10000):
    sum_of_numbers = iterator = 0
    while sum_of_numbers < limit:
        random_number = random.randint(1, 100)
        if random_number % 2 == 0:
            sum_of_numbers += random_number
        iterator += 1
    return iterator
