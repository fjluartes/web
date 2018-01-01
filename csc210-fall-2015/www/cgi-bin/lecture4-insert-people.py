#!C:\Python27\python.exe

# Above line is for windows
# For Unix/Linux:
# #!/usr/bin/env python
import sqlite3

conn = sqlite3.connect('people.db')
c = conn.cursor()

c.execute("insert into users values('Philip', '30', '../cat.jpg');")
c.execute("insert into users values('John', '25', '../dog.jpg');")
c.execute("insert into users values('Jane', '40', '../bear.jpg');")

conn.commit()
conn.close()
