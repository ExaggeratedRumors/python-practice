# 1. Zapisywanie sesji gry (np. rzucanie dwoma kostkami aż wyrzucimy 6,6)
# do pliku dla danej osoby, ilości rzutów w danej sesji, daty

import random
import datetime
import codecs


def dice_throw(number_of_throws):
    output = []
    for i in range(0, number_of_throws):
        output.append(random.randint(1, 6))
    return output


counter = 0
while True:
    result = dice_throw(2)
    if result == [6, 6]:
        break
    counter += 1

name = "Dominik"
date = datetime.datetime.today()

with codecs.open("results.txt", 'w', 'utf-8') as file:
    file.write(f"{name}\n")
    file.write(f"{date}\n")
    file.write(f"liczba rzutów: {counter}\n")



