#!C:\Python27\python.exe

# Above line is for windows
# For Unix/Linux:
# #!/usr/bin/env python
import cgi

import cgitb
cgitb.enable()

import datetime
t = str(datetime.datetime.now())

import Cookie
import os

stored_cookie_string = os.environ.get('HTTP_COOKIE')

# my first time visiting site
if not stored_cookie_string:
    c = Cookie.SimpleCookie()
    c["current_time"] = t
    
    # HTTP header
    print "Content-type: text/html"
    print c
    print 
    print '<html>'
    print '  <body>'
    print '    <h2>Hello! The current time is: ' + t + '</h2>'
    print "    <h2>I'm sending you a cookie!</h2>"
    print '  </body>'
    print '</html>'

else:
    # parse the cookie string
    c = Cookie.SimpleCookie(stored_cookie_string)

    # HTTP header
    print "Content-type: text/html"
    print c
    print 
    print '<html>'
    print '  <body>'
    print '  stored_cookie_string: ', stored_cookie_string
    print '    <h2>The server received your cookie!</h2>'
    print "    <h2>Your cookie's current time is: " + c["current_time"].value + "</h2>"
    print '  </body>'
    print '</html>'

