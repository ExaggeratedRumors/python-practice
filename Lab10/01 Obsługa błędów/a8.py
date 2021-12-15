# Obsługa przy podawaniu błędnej daty z klawiatury.

import datetime

try:
    input_date = input("podaj datę w formacie RRRR-MM-DD: ")
    array = input_date.split("-")
    array = list(map(int, array))
    date = datetime.date(array[0], array[1], array[2])
    print(f"Podałeś datę: {date.day}.{date.month}.{date.year}")
except:
    print("Podałeś zły format daty")

