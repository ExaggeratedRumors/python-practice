# 10. Rzucamy dwoma kośćmi, aż wyrzucimy dokładnie sumą 100.
# Jeśli suma wyrzucona w jednym rzucie jest za duża w stosunku
# do aktualnej sumy to odejmujemy dany rzut, a jak wynik jest < 100
# to dodajemy do sumy. Rejestrujemy wszystkie wyrzucone wartości i sumę.
# Na końcu podajemy ile rzutów wykonaliśmy aby osiągnąć wartość 100.
import random


def fun(n=100):
    throw_sum = 0
    iterator = 0
    while True:
        iterator += 1
        first_dice = random.randint(1, 6)
        second_dice = random.randint(1, 6)
        temp = first_dice + second_dice
        if (throw_sum + temp) == n:
            break
        elif (throw_sum + temp) > n:
            throw_sum -= temp
        else:
            throw_sum += temp
    return iterator


print(fun())
