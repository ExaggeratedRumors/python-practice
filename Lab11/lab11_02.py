# Od punktu 3 tworzymy osobny plik o nazwie lab11_03.py itd.,
# gdzie wstawiamy opis i rozwiązanie (można wykorzystać już istniejący kod z poprzednich zadań)

# 2. Utworzyć i nawiązać połączenie do bazy test.db:
# (można także skopiowac bazę danych test.db wcześniej utworzoną katalogu Lab11)
import sqlite3
conn = sqlite3.connect('c:/temp/test.db')
print ("Połączenie z bazą danych - nawiązane");
conn.close()
print ("Połączenie z bazą danych - zakończone ");

# 3. W bazie danych test.db założyć tabelę (na podstawie materiałów z wykladów):
#   EMPLOYEES z kolumnami:
#   - ID
# 	- NAME
# 	- AGE
# 	- ADDRESS
# 	- SALARY
#   Zaproponować właściwe typy danych w każdej z kolumn.

# 4. Do tabeli: EMPLOYEES wprowadzić 3-4 krotki (rekordy).

# 5. Napisać skrypt, który pobierze i wyświetli wszystkie krotki z tabeli EMPLOYEES.

# 6. Napisać skrypt, który zmodyfikuje składowane w tabeli EMPLOYEES dane (polecenie UPDATE) zwiększajć o 10% wartość SALARY

# 7. Napisać skrypt, który usunie z tabeli EMPLOYEES rekordy o ID <=2 (polecenie DELETE)

# 8. Obsługa błędu np. przy tworzeniu tabeli, która już istnieje
#	(bez IF NOT EXISTS w polecniu CREATE TABLE)

# 9. Utworzyć w pamięci RAM tabelę z autonumeracją pola ID.
# conn = sqlite3.connect(':memory:')
# Zrealizować wstawianie danych na podstawie listy (tuple).
# Dodatkowo wstawianie i prezentacja danych powinna być zrealizowana na podstawie opracowanej do tego funkcji.
# Opracowane funkcje mają przyjmować określone atrybuty w zależności od ich przeznaczenia.
# Zaprezentować prawidłowe działanie tych funkcji
    # import sqlite3
    # def czytaj_dane():
    #     """Funkcja pobiera i wyświetla dane z bazy."""
    # def utworz_tabele(): #gotowa funkcja
    #     """Tworzenie tabeli bez parametrów"""
    #     conn.execute('''CREATE TABLE IF NOT EXISTS EMPLOYEES
    #     (ID INTEGER PRIMARY KEY ASC,
    #     NAME TEXT NOT NULL,
    #     AGE INT NOT NULL,
    #     ADDRESS CHAR(50),
    #     SALARY REAL);''')
    # def wstaw_dane(lista):
    #     """Wstawiamy wiele rekordów na podstawie listy tuple"""

# 10. Ostatni przykład, wstawić powyższe 3 funkcje do oddzielnego modułu modul_db.py
#   oraz wykonać powyższe funkcje (pamiętajmy, iż zmienna conn jest dostępna w ramach jedengo skryptu.
#   Jednak gdy przeniesiemy je do oddzielnego modułu to parametrem wejściowym powinna być zmienna conn)
    # modul_db.py
    # def czytaj_dane(connection):
    #     """Funkcja pobiera i wyświetla dane z bazy."""
    # def utworz_tabele(connection): #gotowa funkcja
    #     """Tworzenie tabeli bez parametrów"""
    #     connection.execute('''CREATE TABLE IF NOT EXISTS EMPLOYEES
    #     (ID INTEGER PRIMARY KEY ASC,
    #     NAME TEXT NOT NULL,
    #     AGE INT NOT NULL,
    #     ADDRESS CHAR(50),
    #     SALARY REAL);''')
    # def wstaw_dane(lista,connection):
    #     """Wstawiamy wiele rekordów na podstawie listy tuple"""


