# 9. Utworzyć w pamięci RAM tabelę z autonumeracją pola ID.
# conn = sqlite3.connect(':memory:')
# Zrealizować wstawianie danych na podstawie listy (tuple).
# Dodatkowo wstawianie i prezentacja danych powinna być zrealizowana na podstawie opracowanej do tego funkcji.
# Opracowane funkcje mają przyjmować określone atrybuty w zależności od ich przeznaczenia.
# Zaprezentować prawidłowe działanie tych funkcji

# >>> wprowadzanie danych do bazy z tupli

import sqlite3

table_name = "EMPLOYEES"


def czytaj_dane(conn):
    """Funkcja pobiera i wyświetla dane z bazy."""
    try:
        cursor = conn.cursor()
        cursor.execute(f"SELECT id, name, address, salary from {table_name}")
        output = [[value for value in row] for row in cursor]
        return output
    except sqlite3.Error as e:
        print(e)


def utworz_tabele(con):
    """Tworzenie tabeli bez parametrów"""
    con.execute(f'''CREATE TABLE IF NOT EXISTS {table_name}
    (ID INTEGER PRIMARY KEY ASC,
    NAME TEXT NOT NULL,
    AGE INT NOT NULL,
    ADDRESS CHAR(50),
    SALARY REAL);''')


def wstaw_dane(con, lista):
    """Wstawiamy wiele rekordów na podstawie listy tuple"""
    try:
        con.execute(f"INSERT OR IGNORE INTO {table_name} VALUES {lista}")
        conn.commit()
    except sqlite3.Error as e:
        print(e)


conn = sqlite3.connect(':memory:')
utworz_tabele(conn)
wstaw_dane(conn, (1, "Dominik", 20, "Warszawa", 20000))
data = czytaj_dane(conn)
conn.close()
print(data)
