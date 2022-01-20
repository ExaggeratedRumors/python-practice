# 4. Do tabeli: EMPLOYEES wprowadzić 3-4 krotki (rekordy).

# >>> commit - wprowadzanie rekordów

import sqlite3

conn = None

table_name = "EMPLOYEES"

try:
    conn = sqlite3.connect('test.db')
    conn.execute(f"INSERT OR IGNORE INTO {table_name} VALUES (1, 'Jan', 32, 'Warszawa', 20000.00 )")
    conn.execute(f"INSERT OR IGNORE INTO {table_name} VALUES (2, 'Piotr', 25, 'Kraków', 15000.00 )")
    conn.execute(f"INSERT OR IGNORE INTO {table_name} VALUES (3, 'Adam', 23, 'Rzeszów', 32000.00 )")
    conn.commit()

    #wyświetlanie tabeli
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    print(cursor.fetchall())
    conn.close()
except sqlite3.Error as e:
    print(e)