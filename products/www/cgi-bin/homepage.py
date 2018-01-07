#!C:\Python27\python.exe
# #!/usr/bin/env python
import cgi

import cgitb
cgitb.enable()

import sqlite3
conn = sqlite3.connect('product.db')
cur = conn.cursor()

import Cookie
import os

form = cgi.FieldStorage()

if ('my_email' in form):
    email = form['my_email'].value

    cur.execute('select email from users where email=?', [email])
    if cur.fetchone() is not None:
        c = Cookie.SimpleCookie()
        c['current_email'] = email
    else:
        c = ''

    print 'Content-Type: text/html'
    print c
    print ''
    print '''
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
        <li><a href="../contact.html">Contact</a></li>
        <li><a href="../">Logout</a></li>
        </ul>
        </div>
        </div>
        </nav>
            
        <div class="container">
        <div class="account">
        '''
    cur.execute('select email from users where email=?', [email])
    if cur.fetchone() is None:
        print '<h2>Invalid user! Please login.</h2>'
    else:
        for r in cur.execute('select email from users where email=?', [email]):
            print '<h1>Hello, ' + email + '</h2>'
            print '''
            <p class="lead">Your products:</p>
            </div>
    
            <table class="table table-bordered table-striped">
            <thead>
            <tr>
            <th>Product Name</th>
            <th>Price</th>
            <th>Quantity</th>
            </tr>
            </thead>
            <tbody>
            <tr>
            <td>iPhone X</td>
            <td>$1,099.99</td>
            <td>10</td>
            </tr>
            <tr>
            <td>Samsung Note 8</td>
            <td>$899.99</td>
            <td>8</td>
            </tr>
            <tr>
            <td>Macbook Pro 2016</td>
            <td>$1,299.99</td>
            <td>9</td>
            </tr>
            </tbody>
            </table> 
            </div>
            </div>
            '''

    print '''
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
        <script>window.jQuery || document.write(\'<script src="../assets/js/vendor/jquery.min.js"><\/script>\')</script>
        <script src="../dist/js/bootstrap.min.js"></script>
        <script src="../assets/js/ie10-viewport-bug-workaround.js"></script>
        </body>
        </html>
        '''
else:
    stored_cookie_string = os.environ.get('HTTP_COOKIE')
    
    print 'Content-Type: text/html'
    print ''
    print '''
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
        <li><a href="../contact.html">Contact</a></li>
        <li><a href="../">Logout</a></li>
        </ul>
        </div>
        </div>
        </nav>
    
        <div class="container">
        <div class="account">
        '''
    #cur.execute('select email from users where email=?', [stored_cookie_string])
    #cur.fetchone() is None
    if not stored_cookie_string:
        print '''
        <h2>Invalid user. Please login.</h2>
        </div>
        </div>
        '''
    else:
        c = Cookie.SimpleCookie(stored_cookie_string)
        email = c['current_email'].value

        for r in cur.execute('select email from users where email=?', [email]):
            print '<h1>Hello, ' + email + '</h1>'
            print '''
            <p class="lead">Your products:</p>
            </div>
    
            <table class="table table-bordered table-striped">
            <thead>
            <tr>
            <th>Product Name</th>
            <th>Price</th>
            <th>Quantity</th>
            </tr>
            </thead>
            <tbody>
            <tr>
            <td>iPhone X</td>
            <td>$1,099.99</td>
            <td>10</td>
            </tr>
            <tr>
            <td>Samsung Note 8</td>
            <td>$899.99</td>
            <td>8</td>
            </tr>
            <tr>
            <td>Macbook Pro 2016</td>
            <td>$1,299.99</td>
            <td>9</td>
            </tr>
            </tbody>
            </table> 
            </div>
            </div>
                '''
    print '''
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
        <script>window.jQuery || document.write(\'<script src="../assets/js/vendor/jquery.min.js"><\/script>\')</script>
        <script src="../dist/js/bootstrap.min.js"></script>
        <script src="../assets/js/ie10-viewport-bug-workaround.js"></script>
        </body>
        </html>
    '''
