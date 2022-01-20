import random

THROWS = 4
ATTEMPTS = 100


def play():
    return sum([sum([random.randint(1, 6) for _ in range(0, THROWS)]) for _ in range(0, ATTEMPTS)])


player_name = input("Podaj nazwę gracza: ")
score = play()

with open("stores.txt", 'a') as file:
    file.write(f"{player_name} {score}\n")

with open("stores.txt", 'r') as file:
    data = [[val for val in line.split()] for line in file]

print(f"{player_name} otrzymał/a: {score} punktów")
print(f"Najlepszy wynik: {max([int(score[1]) for score in data])}")
