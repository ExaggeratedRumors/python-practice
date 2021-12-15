# Obsługa błędu przy otwieraniu pliku do odczytu, który nie istnieje.

try:
    data = open("nieistniejacy_plik.txt", "r")
except FileNotFoundError:
    print("plik nie istnieje")