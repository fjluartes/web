#!"C:\Python27\python.exe"

# the above line is for Windows. For Mac OS, use the path to your Python,
# which is usually:
#!/usr/bin/env python

# Lecture 3 - CSC210 Fall 2015
# Philip Guo

# To run, start AMPSS and visit:
#
# http://localhost/cgi-bin/lecture3.py?my_name=Philip&my_age=32&my_image=../cat.jpg

# useful for debugging
import cgitb
cgitb.enable()
import datetime
import cgi
form = cgi.FieldStorage()

print 'Content-type:text/html'
print # don't forget the extra new line
# extra blank line separates http header from body

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

      p#myLine {
        color: red;
      }
    </style>
  </head> '''
print ''
print '  <body>'
print '    <h1>My heading</h1>'
print ''
print '    <h2>'
print str(datetime.datetime.now())
#print '    My sub-heading'
print '    </h2>'
print ''
print '    <h2>Your name is: ' + form['my_name'].value + '</h2>'
print '    <h2>Your age is: ' + form['my_age'].value + '</h2>'
print '    <img src="' + form['my_image'].value + '"/>'
print ''
print '    <p>Hello</p>'
print ''
print '    <h2>'
print '      My other sub-heading'
print '    </h2>'
print ''
print '    <p id="myLine">a new line</p>'
print ''
print '    <p>another one</p>'
print ''
print '  </body>'
print '</html>'

