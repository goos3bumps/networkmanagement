#!/usr/bin/env python

import getpass
import sys
import telnetlib

readfile = open('routerlist', "r")
HOST = readfile.read()
readfile.close()
HOST = HOST.split()

#HOST = ["192.168.122.16" , "192.168.122.79"]
user = raw_input("Enter your telnet username: ")
password = getpass.getpass()

for line in HOST:
#for count in range(0,len(HOST)):
#       tn = telnetlib.Telnet(HOST[count])
        print(line)
        tn = telnetlib.Telnet(line)
        tn.read_until("Username: ")
        tn.write(user + "\n")
        if password:
                tn.read_until("Password: ")
                tn.write(password + "\n")
                tn.write("conf t\n")
                for i in range(0,11):
                        tn.write("no int loop " + str(i) + "\n")
#                       tn.write("int loop " + str(i) + "\n")
#                       tn.write("desc pythonscript loopback int " + str(i) + "\n")
                tn.write("end\n")
                tn.write("wr mem\n")
                tn.write("\n")
                tn.write("exit\n")

                print tn.read_all()
