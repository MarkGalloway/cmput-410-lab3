#!/usr/bin/env python
 
print """Content-type: text/html

<!DOCTYPE html>
<html><head><title>Test URL Encoding</title></head><body>
<form method="post" action="test_form.py">
<textarea name="comments" cols="40" rows="5">
Enter comments here...
</textarea>
<br/>
<input type="submit" value="Submit">
</form>
</body>
</html>"""



