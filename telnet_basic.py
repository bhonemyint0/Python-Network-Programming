import getpass
import sys
import telnetlib

HOST = "192.168.1.1"
user = raw_input("Enter your telnet username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until("Username: ")
tn.write(user + "\n")
if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")

tn.write("enable \n")
tn.read_until("Password: ")
enable_passwd = getpass.getpass("Enter your Enable password ")
tn.write(enable_passwd + "\n")
tn.write("conf t\n")
tn.write("host R1\n")
tn.write("end\n")
tn.write("exit\n")
#tn.close()
output =tn.read_all()
print output