# 3. W bazie danych test.db założyć tabelę (na podstawie materiałów z wykladów):
#   EMPLOYEES z kolumnami:
#   - ID
# 	- NAME
# 	- AGE
# 	- ADDRESS
# 	- SALARY
#   Zaproponować właściwe typy danych w każdej z kolumn.

import sqlite3

sql_create_table = """
                    CREATE TABLE IF NOT EXISTS EMPLOYEES
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

