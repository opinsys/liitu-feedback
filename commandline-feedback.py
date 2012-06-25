#!/usr/local/bin/python
#
# Echo client program
import datetime
import os
import socket

hostname=socket.gethostname()
username=os.system("whoami")
date = datetime.datetime.now()

print "How do you feel after using the system"
print "4 - Great, 3 - Ok, 2 - Could be better, 1 - Sucks"

evaluation=raw_input('Enter your evaluation by  value: ')

print ""
print "Please Give us some written feedback"
feedback=raw_input('Write your feedback here: ')


print "hostname: " + hostname
print "username: " + str(username)
print "date:" + str(date)
print "evaluation: " + evaluation
print "feedback: " + feedback
    
