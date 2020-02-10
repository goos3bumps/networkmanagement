#!/usr/bin/env python

import getpass
import sys
import telnetlib

#Open the file called myswitch, copy it to variable HOST, strip of the whitespaces:
readfile = open('myswitch', "r")
HOST = readfile.read()
readfile.close()
HOST = HOST.split()

#Ask for username and password:
user = raw_input("Enter your telnet username: ")
password = getpass.getpass()

#loop through each line of the HOST variable and execute the commands:
for line in HOST:
        print "Get running config from " + (line)
        tn = telnetlib.Telnet(line)
        tn.read_until("Username: ")
        tn.write(user + "\n")
        if password:
                tn.read_until("Password: ")
                tn.write(password + "\n")
                tn.write("terminal len 0\n")
                tn.write("show run\n")
                tn.write("exit\n")
                readoutput = tn.read_all()
                saveoutput = open("switch-" + line, "w")
                saveoutput.write(readoutput)
                saveoutput.close()
