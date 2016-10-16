Random Email
Language: Python
Author: Andrew McGillivary
Date: 10/16/16


This is a script designed to generate a random email address using the website www.10minutemail.com.
It uses the requests, lxml, and time modules.  The lxml module saves the html from the website as an
html tree, then the script uses xpath to find the email address that has been generated.  It then 
prints the email address and the time at which it was created, with a reminder that it will last
for 10 minutes.