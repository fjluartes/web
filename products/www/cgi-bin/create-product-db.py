#!C:\Python27\python.exe
# #!/usr/bin/env python
import sqlite3

conn = sqlite3.connect('product.db')
c = conn.cursor()

c.execute('create table users(u_id integer primary key, email varchar(100), password varchar(100));')
c.execute('create table products(p_id integer primary key, name varchar(100), email varchar(100), price integer, quantity integer)')

conn.commit()
conn.close()
