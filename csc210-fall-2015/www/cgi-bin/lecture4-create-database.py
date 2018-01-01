#!C:\Python27\python.exe

# Above line is for windows
# For Unix/Linux:
# #!/usr/bin/env python
import sqlite3

conn = sqlite3.connect('people.db')
c = conn.cursor()

c.execute('create table users(name varchar(100) primary key, age integer, image varchar(100));')

conn.commit()
conn.close()
