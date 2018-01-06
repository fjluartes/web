#!C:\Python27\python.exe
# #!/usr/bin/env python
import sqlite3

conn = sqlite3.connect('product.db')
c = conn.cursor()

for r in c.execute('select * from users;'):
    print r
print

conn.commit()
conn.close()
