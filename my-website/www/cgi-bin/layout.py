#!C:\Python27\python.exe
import cgitb
cgitb.enable()
import datetime
import cgi
form = cgi.FieldStorage()

print 'Content-type:text/html'
print ''
print '''
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Fred's Site</title>
    <link rel="stylesheet" href="../styles/style.css">
  </head>

  <body>
    <nav>
      <ul>
        <li><a href="index.html">Fred's Site</a></li>
        <li><a href="archives.html">Archives</a></li>
        <li><a href="works.html">Works</a></li>
      </ul>

      <form>
        <input type="search" name="q" placeholder="Search query">
        <input type="submit" value="Go!">
      </form>
    </nav>

    <main>
      <article>
        <p>Blog post here</p>
      </article>

      <aside>
        <h2>About</h2>

        <p>I'm Fred Luartes. I'm a developer, MS Computer Science student, and music enthusiast. </p>

        <p>This website is for my personal projects, notes, and thoughts. </p>
        
        <h2>Archives</h2>
        <ul>
          <li><a href="#">December 2017</a></li>
          <li><a href="#">November 2017</a></li>
          <li><a href="#">September 2017</a></li>
          <li><a href="#">November 2016</a></li>  
          <li><a href="#">July 2016</a></li>
        </ul>

        <h2 id="title">Contact me:</h2>
        <ul>
          <li><a href="mailto:fjluartes@gmail.com" target="_blank">fjluartes@gmail.com</a></li>
          <li><a href="https://twitter.com/fjluartes" target="_blank">Twitter</a></li>
          <li><a href="https://github.com/fjluartes" target="_blank">Github</a></li>
        </ul>
      </aside>
    </main>

    <footer>
      <p>&copy;2017 Fred Luartes</p>
    </footer>
  </body>
</html>
'''
