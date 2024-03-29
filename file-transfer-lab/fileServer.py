#! /usr/bin/env python3

import sys, os, re, socket, params
#os.chdir("..")
os.chdir("Server")

switchesVarDefaults = (
    (('-l', '--listenPort') ,'listenPort', 50001),
    (('-d', '--debug'), "debug", False), # boolean (set if present)
    (('-?', '--usage'), "usage", False), # boolean (set if present)
    )

progname = "echoserver"
paramMap = params.parseParams(switchesVarDefaults)

debug, listenPort = paramMap['debug'], paramMap['listenPort']

if paramMap['usage']:
    params.usage()

lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # listener socket
bindAddr = ("127.0.0.1", listenPort)
lsock.bind(bindAddr)
lsock.listen(5)
print("listening on:", bindAddr)

while True:

    sock, addr = lsock.accept() #once it accepts it needs to fork, you want to do everything inside the child, and exit child
    #make sure the server let the server know the child is done with some sort of feature.
    print("connection rec'd from", addr)

    from framedSock import framedSend, framedReceive

    if not os.fork():
        print("new child process handling connection from", addr)
        while True:
            payload = framedReceive(sock, debug)
            if debug: print("rec'd: ", payload)
            if not payload:
                if debug: print("child exiting")
                sys.exit(0)
            
            print("recieved...")
            framedSend(s, b':' + payload, debug)
            sys.exit(0)

sock.close()