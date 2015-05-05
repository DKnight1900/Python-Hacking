#!/usr/bin/env python
#0x01 Port Scanner

import socket
ports = [21, 22, 53, 445, 80, 443, 3389, 8080]
hosts = ['127.0.0.1', '10.10.10.10', '192.168.1.1']
for host in hosts:
    for port in ports:
        try:
            s = socket.socket()
            print "[+] Attempting to connect to " + host + ":" + str(port)
            s.connect((host, port))
            s.send('hello bird! /n')
            banner = s.recv(1024)
            if banner:
                print "[+] " + host + ":" + str(port) + " open: \n" + banner
            s.close()
        except:
            pass
