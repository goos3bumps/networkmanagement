import paramiko
import time
import array

#Defining Username, Password and retriving current time

username = "ankuj"
password = "juniper123"
timestr = time.strftime("%d%m%Y-%H%M%S")

#Opening the file name myfirewall(should be localy created in the folder as this script) having the ip address

fo = open("myfirewall", "r")
ip_address = fo.read()
fo.close()

#Formating the above read data and reading the IP address

ip_address = ip_address.replace("\n", " ")
ip_address = ip_address.split(" ")

#Defining a file name Error_log to write the error encountered while the script is running

file = open("Error_log", "a")
file.write(timestr)
file.write("\n")
file.close()

# Below module to run the commands in a loop until the ip address in the list are over 

for count in range(0,len(ip_address)):
    ip_addr = ip_address[count]

    try:
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=ip_addr,username=username,password=password)


        #print "Successful connection", ip_addr

        remote_connection = ssh_client.invoke_shell()

        
        filename = "backup" + "-" +str(ip_addr) + "-" + timestr

        #remote_connection.send("terminal length 0\n")
        #remote_connection.send("show running-config\n")
        #remote_connection.send("show version\n")
        #remote_connection.send("exit\n")
        
        #remote_connection.send("\n")
        #remote_connection.send("show configuration | display set| no-more | save " + filename + "\n")
        #remote_connection.send("file copy "+ filename + " ftp://ankuj:welcome123@1.1.1.3"+"\n")
        #remote_connection.send("file delete " + filename + "\n")
        #remote_connection.send("exit\n")

        remote_connection.send("\n")
        remote_connection.send("show configuration | display set| no-more\n")
        remote_connection.send("show chassis routing-engine | no-more\n")
        remote_connection.send("show chassis hardware | no-more\n")
        remote_connection.send("exit\n")

        time.sleep(1)
        output = remote_connection.recv(65535)

        file = open(filename , "w")
        file.write(output)
        file.close()
        
    except Exception as e:
        #pass
        #print e
        file = open("Error_log", "a")
        file.write(str(e))
        file.write("\n")
        file.close()