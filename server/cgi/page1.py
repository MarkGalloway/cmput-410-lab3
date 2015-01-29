#!/usr/bin/env python
 
import cgi
 
form = cgi.FieldStorage()
 
bday = form.getvalue('bday')
hobby = form.getvalue('hobby')
choc = form.getvalue('choc_box')

print """Content-type: text/html

<!DOCTYPE html>
<html>
<head>
  <title>Name and Family Page</title>
</head>
<body>

  <div>Received from page 2...</br>Birthdate: 
"""

print bday

print "</br>Main Hobby:"

print hobby

print "</br>"

if choc:
  print "I like chocolate too!<br/>"
else:
  print "That's too bad. Chocolate is great.<br/>"

print """</br>
  <form method="post" action="page2.py">
    First Name <input name="name"/></br>
    Family Name <input name="fname"/></br>
    Password <input type="password" name="pwd"/></br>
    Which is a better pet?  
    Cats: <input name="pets" value="cats" type="radio"/> 
    Dogs: <input name="pets" value="dogs" type="radio"/><br/>
    <input type="submit"/>
  </form>
</body>
</html>"""