#!/usr/bin/env python
 
import cgi
 
form = cgi.FieldStorage()
 
name = form.getvalue('name')
fname = form.getvalue('fname')
pwd = form.getvalue('pwd')

print """Content-type: text/html

<!DOCTYPE html>
<html>
<head>
  <title>Name and Family Page</title>
</head>
<body>
  <div>Received from page 1...</br>First Name: 
"""

print name

print "</br>Last Name:"

print fname

print "</br>"

print "That password isn't very secure...<br/>"

print """<br/>
  <form method="post" action="page1.py">
    Birthdate <input name="bday"/></br>
    Main Hobby <input name="hobby"/></br>
    Do you like chocolate? <input name="choc_box" type="checkbox" checked/><br/>
    <input type="submit" value="Submit">
  </form>
</body>
</html>"""