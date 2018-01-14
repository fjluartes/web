#!C:\Python27\python.exe
# #!/usr/bin/env python
# edit product submit
import cgitb
cgitb.enable()

import cgi

import sqlite3
conn = sqlite3.connect('product.db')
cur = conn.cursor()

import Cookie
import os

stored_cookie_string = os.environ.get('HTTP_COOKIE')
c = Cookie.SimpleCookie(stored_cookie_string)
my_email = c['current_email'].value

form = cgi.FieldStorage()
my_pid = form['my_pid'].value
my_name = form['my_name'].value
my_price = form['my_price'].value
my_qty = form['my_qty'].value

cur.execute("update products set name=?, price=?, quantity=? where p_id=? and email=?", (my_name, my_price, my_qty, my_pid, my_email))
conn.commit()
conn.close()

print 'Content-Type: text/html'
print ''
print '''
<html>
<head>
<meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="">
<meta name="author" content="">

<title>ProductHub</title>

<link href="../dist/css/bootstrap.min.css" rel="stylesheet">
<link href="../assets/css/ie10-viewport-bug-workaround.css" rel="stylesheet">
<link href="../styles/template.css" rel="stylesheet">
<link href="../styles/signin.css" rel="stylesheet">
<script src="../assets/js/ie-emulation-modes-warning.js"></script>
</head>

<body>
<nav class="navbar navbar-inverse navbar-fixed-top">
<div class="container">
<div class="navbar-header">
<button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
<span class="sr-only">Toggle navigation</span>
<span class="icon-bar"></span>
<span class="icon-bar"></span>
<span class="icon-bar"></span>
</button>
<a class="navbar-brand" href="#">ProductHub</a>
</div>
<div id="navbar" class="collapse navbar-collapse">
<ul class="nav navbar-nav">
<li class="active"><a href="#">Home</a></li>
<li><a href="contact.html">Contact</a></li>
<li><a href="/">Logout</a></li>
</ul>
</div>
</div>
</nav>
<div class="container">
<h2>Edit Product</h2>
<h3>Success!</h3>
<p><a href="homepage.py">Back to Home</a></p>
</div>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
<script>window.jQuery || document.write('<script src="../assets/js/vendor/jquery.min.js"><\/script>')</script>
<script src="../dist/js/bootstrap.min.js"></script>
<script src="../assets/js/ie10-viewport-bug-workaround.js"></script>
</body>
</html>
'''
