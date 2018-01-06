#!C:\Python27\python.exe

# Above line is for windows
# For Unix/Linux:
# #!/usr/bin/env python
import cgi

import cgitb
cgitb.enable()

import sqlite3
conn = sqlite3.connect('people.db')
cur = conn.cursor()

import Cookie
import os

form = cgi.FieldStorage()
if 'my_name' in form:
    name = form['my_name'].value 

    c = Cookie.SimpleCookie()
    c['current_name'] = name

    # HTTP header
    print "Content-type: text/html"
    print c
    print 
    print '<html>'
    print '  <head>'
    print '  <style>'
    print '    img {'
    print '      width: 300px;'
    print '    }'
    print '  </style>'
    print '  </head>'
    print '  <body>'
    
    for r in cur.execute('select * from users where name=?', [name]):
        print '    <h2>Hello ' + name + '</h2>'
        print '    <p>Age: ' + str(r[1]) + '</p>'
        print '    <p>Photo: </p>'
        print '    <img src="' + r[2] + '"/>'

    print '  </body>'
    print '</html>'

else:
    # do we have a cookie?
    stored_cookie_string = os.environ.get('HTTP_COOKIE')

    # HTTP header
    print "Content-type: text/html"
    print 
    print '<html>'
    print '  <head>'
    print '  <style>'
    print '    img {'
    print '      width: 300px;'
    print '    }'
    print '  </style>'
    print '  </head>'
    print '  <body>'

    if not stored_cookie_string:
        print "    <h2>Sorry, no username and you're not logged in<h2>"
    else:
        c = Cookie.SimpleCookie(stored_cookie_string)
        name = c['current_name'].value

        print "    <h2>You are logged in as: " + name + "</h2>"
        print '<hr/>'
        for r in cur.execute('select * from users where name=?', [name]):
            print '    <h2>Hello ' + name + '</h2>'
            print '    <p>Age: ' + str(r[1]) + '</p>'
            print '    <p>Photo: </p>'
            print '    <img src="' + r[2] + '"/>'

    print '  </body>'
    print '</html>'
