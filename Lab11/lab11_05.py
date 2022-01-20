# 5. Napisać skrypt, który pobierze i wyświetli wszystkie krotki z tabeli EMPLOYEES.

# >>> wyświetlanie rekordów

import sqlite3

conn = None

table_name = "EMPLOYEES"

try:
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, address, salary from EMPLOYEES")
    for row in cursor:
        for i in range(0, 4):
            print(row[i], end=" ")
        print("\n")
    conn.close()
except sqlite3.Error as e:
    print(e)
