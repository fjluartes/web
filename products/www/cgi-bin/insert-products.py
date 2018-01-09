#!C:\Python27\python.exe

# Above line is for windows
# For Unix/Linux:
# #!/usr/bin/env python
import sqlite3

conn = sqlite3.connect('product.db')
c = conn.cursor()

c.execute("insert into products values(1, 'Samsung Note 8', 'fred@fred.com', '1299', '9');")
c.execute("insert into products values(2, 'iPhone X', 'maan@maan.com', '1099', '10');")

conn.commit()
conn.close()
