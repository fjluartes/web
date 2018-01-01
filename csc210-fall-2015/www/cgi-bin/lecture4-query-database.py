#!C:\Python27\python.exe

# Above line is for windows
# For Unix/Linux:
# #!/usr/bin/env python
import sqlite3

conn = sqlite3.connect('people.db')
c = conn.cursor()

for r in c.execute('select * from users;'):
    print r
print

conn.commit()
conn.close()
