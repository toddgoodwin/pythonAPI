#!/usr/bin/python3

import sqlite3

conn =sqlite3.connect("test.db")
print('Opened db successfully')

try:
   conn.execute('''CREATE TABLE COMPANY
           (ID INT PRIMARY KEY NOT NULL,
           NAME TEXT NOT NULL,
           AGE INT NOT NULL,
           ADDRESS CHAR(50),
           SALARY REAL);''')
   print('Table create')
except:
    print('table exists')
else:
    conn.close()
