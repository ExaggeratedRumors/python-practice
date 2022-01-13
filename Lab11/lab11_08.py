
# 8. Obsługa błędu np. przy tworzeniu tabeli, która już istnieje
#	(bez IF NOT EXISTS w polecniu CREATE TABLE)

import sqlite3

sql_create_table = """
                    CREATE TABLE EMPLOYEES
                    (ID INT PRIMARY KEY NOT NULL,
                    NAME TEXT NOT NULL,
                    AGE INT NOT NULL,
                    ADDRESS CHAR(50),
                    SALARY REAL);
                    """
conn = None

try:
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    c.execute(sql_create_table)
    conn.close()
except sqlite3.Error as e:
    print(e)


    # Typ wyjątku Opis
    # Warning Zgłaszany w przypadku ważnych ostrzeżeń, tj. obcinanie danych
    # podczas wstawiania, itp. Musi to być podklasa StandardError.
    # Error Klasa podstawowa dla wszystkich innych wyjątków.
    # InterfaceError Zgłaszany w przypadku błędów związanych z interfejsem bd.
    # DatabaseError Zgłaszany dla błędów związanych z bazą danych.
    # DataError Zgłaszany dla błędów, które są spowodowane problemami z
    # przetworzonymi danymi.
    # OperationalError Zgłaszany dla błędów związanych z działaniem bazy danych.
    # IntegrityError Zgłaszany gdy naruszona jest integralność bazy danyc
    # InternalError Zgłaszany baza danych napotka błąd wewnętrzny, np. Kursor
    # nie jest już ważny, transakcja nie jest zsynchronizowana.
    # ProgrammingError Zgłaszany w przypadku błędów programowania, np. Tabela nie
    # została znaleziona lub już istnieje, błąd składni SQL.
    # NotSupportedError Zgłaszany w przypadku użycia metody lub interfejsu API bazy
    # danych, który nie jest obsługiwany przez bazę danych.