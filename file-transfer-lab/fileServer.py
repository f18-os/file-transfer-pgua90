#! /usr/bin/env python3

import sys
sys.path.append("../lib")       # for params

import os, re, socket, params
os.chdir("Server")

switchesVarDefaults = (
                    (('-l', '--listenPort') ,'listenPort', 50001),
                    (('-d', '--debug'), "debug", False), # boolean (set if present)
                    (('-?', '--usage'), "usage", False), # boolean (set if present)
                    )

progname = "fileServer"
paramMap = params.parseParams(switchesVarDefaults)

debug, listenPort = paramMap['debug'], paramMap['listenPort']

if paramMap['usage']:
    params.usage()

lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # listener socket
bindAddr = ("127.0.0.1", listenPort)
lsock.bind(bindAddr)
lsock.listen(5)
print("listening on:", bindAddr)

sock, addr = lsock.accept()

print("connection rec'd from", addr)



from framedSock import framedSend, framedReceive

while True:
    payload = framedReceive(sock, debug)
    if debug: print("rec'd: ", payload)
    if not payload:
        break
    
   print("recieved...")
   
   while len(sendMsg):
       bytesSent = framedSend(sock, payload, debug)
       file  = open("rcv.txt", 'w') #attempted to put output results into textfile
       file.write(bytesSent)
       file.close()
       sendMsg = sendMsq[bytesSent: 0]
       
sock.shutdown(socket.SHUT_WR)
sock.close()

    
    

