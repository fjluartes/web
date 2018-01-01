#!C:\Python27\python.exe

# Above line is for windows
# For Unix/Linux:
# #!/usr/bin/env python
import cgitb
cgitb.enable()

import cgi
form = cgi.FieldStorage()

my_name = form['my_name'].value
my_age = form['my_age'].value
my_image = form['my_image'].value

# insert into database
import sqlite3

conn = sqlite3.connect('people.db')
c = conn.cursor()

c.execute('insert into users values(?, ?, ?);', (my_name, my_age, my_image))
conn.commit()

import datetime

print 'Content-type:text/html'
print ''

print '<html>'
print '''  <head>
    <title>
      My first webpage
    </title>

    <style type="text/css">
      h1 {
        font-size: 100px;
        font-family: arial;
      }

      img {
        width: 300px;
      }
  </style>
  </head> '''
print ''
print '  <body>'
print '    <h1>My heading</h1>'
print ''
print '    <h2>'
print str(datetime.datetime.now())
print '    </h2>'
print ''
for r in c.execute('select * from users;'):
    name = r[0]
    age = r[1]
    image = r[2]
    
    print '    <h2>Your name is: ' + name + '</h2>'
    print '    <h2>Your age is: ' + str(age) + '</h2>'
    print '    <img src="' + image + '"/>'
    print '<hr/>'
conn.close()

print '  </body>'
print '</html>'

