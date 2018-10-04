#! /usr/bin/env python3

import sys

sys.path.append(".../lib") #for params
import re, socket, params

from framedSock import framedSend, framedReceive

switchesVarDefaults = (
    (('-s', '--server'), 'server', "127.0.0.1:50001"),
    (('-d', '--debug'), "debug", False), # boolean (set if present)
    (('-?', '--usage'), "usage", False), # boolean (set if present)
    )

progname = "fileClient"
paramMap = params.parseParams(switchesVarDefaults)

server, usage, debug  = paramMap["server"], paramMap["usage"], paramMap["debug"]

if usage:
    params.usage()

try:
    serverHost, serverPort = re.split(":", server)
    serverPort = int(serverPort)
except:
    print("Can't parse server:port from '%s'" % server)
    sys.exit(1)

s = None

for res in socket.getaddrinfo(serverHost, serverPort, socket.AF_UNSPEC, socket.SOCK_STREAM):
    af, socktype, proto, canonname, sa = res
    try:
        print("creating sock: af=%d, type=%d, proto=%d" % (af, socktype, proto))
        s = socket.socket(af, socktype, proto)
    except socket.error as msg:
        print(" error: %s" % msg)
        s = None
        continue
    try:
        print(" attempting to connect to %s" % repr(sa))
        s.connect(sa)
    except socket.error as msg:
        print(" error: %s" % msg)
        s.close()
        s = None
        continue
    break

if s is None:
    print('could not open socket')
    sys.exit(1)
#Want to create a file so that each line is read line by line but by 100 bytes at a time.

inputTxtFile = input("Enter file name declaration.txt \n")

try:
    with open(inputTxtFile.strip(), 'rb') as file:
        content = file.read()
        
except FileNotFoundError:
    print("File not found")
    sys.exit(0)

framedSend(s,b':' + inputTxtFile.strip().encode('utf-8'))

data = data.replace(b"\n", b"\'e\'")
        
while len(data) >= 100:
    line = data[:100]
    framedSend(s,b":" + line, debug)

                
if len(data) > 0:
    framedSend(s,b":"+data,debug)
    framedSend(s,b":\'end\'")
    print("recieved:", framedReceive(s, debug))

socket.close()
quit()
