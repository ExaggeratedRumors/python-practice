# Od punktu 3 tworzymy osobny plik o nazwie lab11_03.py itd.,
# gdzie wstawiamy opis i rozwiązanie (można wykorzystać już istniejący kod z poprzednich zadań)

# 2. Utworzyć i nawiązać połączenie do bazy test.db:
# (można także skopiowac bazę danych test.db wcześniej utworzoną katalogu Lab11)
import sqlite3
conn = sqlite3.connect('test.db')
print ("Połączenie z bazą danych - nawiązane");
conn.close()
print ("Połączenie z bazą danych - zakończone ");