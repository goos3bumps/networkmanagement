#!/usr/bin/env python

import paramiko
import time
#import getpass

host = "192.168.122.169"
user = "root"
password = "password"

client  = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=host,username=user,password=password)

#Send commands to execute
client.exec_command('touch newfilebyexeccommand.txt')
client.exec_command('date >> newfilebyexeccommand.txt')
#client.exec_command('ifconfig lo down')

#invoking shell to run command and print capture output
remote_shell = client.invoke_shell()
remote_shell.send('ls -alh\n')
remote_shell.send('date\n')
remote_shell.send('cat newfilebyexeccommand.txt\n')
#remote_shell.send('ifconfig\n')
time.sleep(1)
output = remote_shell.recv(65535)
print(output)
#time.sleep(0.5)
#remote_shell.send('ifconfig lo up\n')
time.sleep(1)
#remote_shell.send('ifconfig\n')
#time.sleep(0.5)
#output = remote_shell.recv(65535)
#print(output)

#closing ssh client
client.close()
