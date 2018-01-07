#!C:\Python27\python.exe
# #!/usr/bin/env python
import sqlite3

conn = sqlite3.connect('product.db')
c = conn.cursor()

c.execute('create table users(email varchar(100) primary key, password varchar(100));')
c.execute('create table products(name varchar(100) primary key, price integer, quantity integer)')

conn.commit()
conn.close()
