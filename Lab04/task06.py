# 6. Jaka to liczba? Komputer wybiera losowo liczbę z zakresu od 1 do 100.
# Gracz próbuje ją odgadnąć, a komputer go informuje,
# czy podana przez niego liczba jest: za duża, za mała,
# prawidłowa (na końcu podajemy ile liczb podaliśmy aby
# zgadnąć wylosowaną liczbę

import random


def init_number(min_val=1, max_val=100):
    return random.randint(min_val, max_val)


def guess_number(number):
    guessed_number = None
    counter = 0
    while guessed_number != number:
        guessed_number = int(input("podaj liczbę: "))
        if guessed_number < number:
            print("za mała")
        elif guessed_number > number:
            print("za duża")
        else:
            print("zgadłeś!")
        counter += 1
    return counter


guess_number(init_number())
