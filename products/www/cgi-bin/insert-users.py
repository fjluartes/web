#!C:\Python27\python.exe

# Above line is for windows
# For Unix/Linux:
# #!/usr/bin/env python
import sqlite3

conn = sqlite3.connect('product.db')
c = conn.cursor()

c.execute("insert into users values('fred@fred.com', 'password');")
c.execute("insert into users values('maan@maan.com', 'password');")

conn.commit()
conn.close()
