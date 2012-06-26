#!/usr/local/bin/python
#
# Echo client program
import datetime
import socket
import urllib
import urllib2
import commands

hostname=socket.gethostname()
(a,username) = commands.getstatusoutput('whoami')
#username=os.system("whoami")
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


def sendPostRequestToServer(username,hostname,date,evaluation,feedback):
    
    query_args = { 'username':str(username), 'hostname':str(hostname), 'date':str(date), 'evaluation':str(evaluation), 'feedback':str(feedback) }
    encoded_args = urllib.urlencode(query_args)
    url = 'http://posttestserver.com/post.php'
    print urllib2.urlopen(url, encoded_args).read()    


sendPostRequestToServer(username,hostname,date,evaluation,feedback)
