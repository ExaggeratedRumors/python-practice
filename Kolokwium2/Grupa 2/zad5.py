import re

# Komentarz:
# akceptowalny jest jedynie
# prawidłowy format zapisu liczb dziesiętnych
# np: 042 nie jest akceptowalne

while True:
    x = input("Podaj liczbę: ")
    if re.match('^[1-9][0-9]*$', x):
        try:
            conversion = int(x)
            print(f"Wprowadzono liczbę: {x}")
            break
        except ValueError as e:
            print("Podana wartość jest stringiem")
