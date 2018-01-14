#!C:\Python27\python.exe
# #!/usr/bin/env python
# edit product
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
email = c['current_email'].value

form = cgi.FieldStorage()
my_pid = form['my_pid'].value

for r in cur.execute('select * from products where p_id=? and email=?;', [my_pid, email]):
    my_name = str(r[1])
    my_price = str(r[3])
    my_qty = str(r[4])

print 'Content-type: text/html'
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
    '''
print '  <form method="post" action="edit-product-submit.py?my_pid=' + my_pid + '">'
print '''      
      <h2>Edit Product</h2>
        <div class="form-group">
          <label for="my_pid">Product ID:</label>
'''
print '          <input type="text" class="form-control" name="my_pid" value="' + my_pid + '" disabled>'
print '''
        </div>
        <div class="form-group">
          <label for="my_name">Product Name:</label>
'''

print '          <input type="text" class="form-control" name="my_name" value="' + my_name + '">'
print '''
        </div>
        <div class="form-group">
          <label for="my_price">Price:</label>
'''
print '          <input type="text" class="form-control" name="my_price" value="' + my_price + '">'
print '''
        </div>
        <div class="form-group">
          <label for="my_qty">Quantity:</label>
'''
print '          <input type="text" class="form-control" name="my_qty" value="' + my_qty + '">'
print '''
        </div>
        <button type="submit" class="btn btn-primary">Submit</button>
        <a href="homepage.py" class="btn btn-default">Back</a>
      </form>
    </div>

    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
    <script>window.jQuery || document.write('<script src="../assets/js/vendor/jquery.min.js"><\/script>')</script>
    <script src="../dist/js/bootstrap.min.js"></script>
    <script src="../assets/js/ie10-viewport-bug-workaround.js"></script>
  </body>
</html>
'''
