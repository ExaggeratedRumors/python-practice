# 10. Ostatni przykład, wstawić powyższe 3 funkcje do oddzielnego modułu modul_db.py
#   oraz wykonać powyższe funkcje (pamiętajmy, iż zmienna conn jest dostępna w ramach jedengo skryptu.
#   Jednak gdy przeniesiemy je do oddzielnego modułu to parametrem wejściowym powinna być zmienna conn)
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


def utworz_tabele(con):  # gotowa funkcja
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
        con.commit()
    except sqlite3.Error as e:
        print(e)


