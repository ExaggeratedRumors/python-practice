# 6. Napisać skrypt, który zmodyfikuje składowane w tabeli EMPLOYEES dane (polecenie UPDATE) zwiększajć o 10% wartość SALARY

# >>> update - zmiana rekordu

import sqlite3

conn = None

table_name = "EMPLOYEES"

try:
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT salary from EMPLOYEES")
    salaries = [float(record[0]) for record in cursor.fetchall()]
    for i in range(0, len(salaries)):
        cursor.execute(f"UPDATE {table_name} set SALARY = {salaries[i] * 1.1} WHERE ID={i+1}")
    cursor.execute("SELECT id, name, address, salary from EMPLOYEES")
    conn.commit()
    for row in cursor:
        for i in range(0, 4):
            print(row[i], end=" ")
        print("\n")
    conn.close()
except sqlite3.Error as e:
    print(e)