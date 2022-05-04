#!/bin/python

import cgitb

cgitb.enable()

print("Content-type: text/html\n\n")
print("<html><body>")
print("<h1> Welcome to the test page </h1>")

for i in range(5):
	print("<h2> Hello World !!" + str(i) + "</h2>")

print("</body></html>")
