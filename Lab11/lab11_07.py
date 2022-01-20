# 7. Napisać skrypt, który usunie z tabeli
# EMPLOYEES rekordy o ID <=2 (polecenie DELETE)

# >>> execute DELETE - usuwanie rekordu

import sqlite3

conn = None

table_name = "EMPLOYEES"

try:
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    for i in range(0, 2):
        cursor.execute(f"DELETE from {table_name} WHERE ID={i+1}")
    conn.commit()
    cursor.execute("SELECT id, name, address, salary from EMPLOYEES")
    for row in cursor:
        for i in range(0, 4):
            print(row[i], end=" ")
        print("\n")
    conn.close()
except sqlite3.Error as e:
    print(e)