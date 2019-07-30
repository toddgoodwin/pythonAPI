#!/usr/bin/python3

import sqlite3

conn =sqlite3.connect("test.db")
print('Opened db successfully')

try:
   rs = conn.execute('SELECT *  FROM COMPANY')
   
   
   for col in rs:
       #print(dir(col))
       print(col)
       print(col[0]) 
       #print(col[1].name)
except:
    print('NO DATA')
else:
    conn.close()
