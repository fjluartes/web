#!C:\Python27\python.exe
# #!/usr/bin/env python
import sqlite3

conn = sqlite3.connect('product.db')
cur = conn.cursor()

for r in cur.execute('select * from users;'):
    print r
print

for r2 in cur.execute('select * from products;'):
    print r2
print

for r3 in cur.execute('select name, price, quantity from products where email=\'fred@fred.com\';'):
    print r3
print

conn.commit()
conn.close()
