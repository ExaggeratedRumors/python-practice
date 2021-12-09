# 3. Zapisywanie trzech najlepszych wyników gry (np. rzucanie dwoma kostkami aż wyrzucimy 6,6) 
# do pliku score.txt i przechowujemy ilości rzutów w danej sesji, datę i czas w postaci YYYY-MM-DD HH24:MIN:SEC. 
# Jeżeli wynik jest taki sam a data jest starsza to nie zastępujemy jej.

import datetime
import random


def add_result(score, scores):
    new_score = [str(score), str(datetime.datetime.today())]
    if not scores:
        scores.append(new_score)
    else:
        for i in range(0, len(scores)):
            if score < int(scores[i][0]):
                if len(scores) > 2:
                    scores.pop()
                scores.insert(i, new_score)
                break


def save_score(score):
    with open("score.txt", "r") as file:
        scores = [[val for val in line.split()] for line in file]
    with open("score.txt", "w") as file:
        add_result(score, scores)
        for s in scores:
            separator = " "
            output = separator.join(s)
            file.write(output + "\n")


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

print("Wynik:", counter)
save_score(counter)
