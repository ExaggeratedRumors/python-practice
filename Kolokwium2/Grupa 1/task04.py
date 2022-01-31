import re

while True:
    number = input("Podaj liczbę:")
    if re.match('^[1-9][0-9]*$', number):
        print(f"Wprowadzona liczba: {number}")
        break
