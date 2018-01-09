#!C:\Python27\python.exe
# #!/usr/bin/env python
# register
import cgitb
cgitb.enable()

import cgi

import sqlite3
conn = sqlite3.connect('product.db')
c = conn.cursor()

form = cgi.FieldStorage()
my_uid = form['my_uid'].value
my_email = form['my_email'].value
my_pwd = form['my_pwd'].value

c.execute('insert into users values(?, ?, ?);', (my_uid, my_email, my_pwd))
conn.commit()
conn.close()

print 'Content-Type: text/html'
print ''
print '''
<!DOCTYPE html>
<html lang="en">
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
<li><a href="/">Login</a></li>
</ul>
</div>
</div>
</nav>
<div class="container">
<h2>Register</h2>
<h3>Success!</h3>
</div>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
<script>window.jQuery || document.write('<script src="../assets/js/vendor/jquery.min.js"><\/script>')</script>
<script src="../dist/js/bootstrap.min.js"></script>
<script src="../assets/js/ie10-viewport-bug-workaround.js"></script>
</body>
</html>
'''
