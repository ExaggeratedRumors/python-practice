# 2. Utworzyć i nawiązać połączenie do bazy test.db:
# (można także skopiowac bazę danych test.db wcześniej utworzoną katalogu Lab11)

# >>> sqlite connect & close - tworzenie bazy danych

import sqlite3
conn = sqlite3.connect('test.db')
print ("Połączenie z bazą danych - nawiązane");
conn.close()
print ("Połączenie z bazą danych - zakończone ");