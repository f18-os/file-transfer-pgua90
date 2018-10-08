#! /usr/bin/env python3


#Write a fileClient.py & fileServer.py, that transfers a file ("put") from client to server. 
#You program should
#1. Work with/without a proxy
#2. Support multiple clients simeoultaneously using fork();
#3. Deal with scenarios such as:
#    * Zero length files
#    * user attempts to submit a file that does not exist.
#    * file already exists in server
#    * the client or server unexpectedly disconnects


# Echo client program
import socket, sys, re
sys.path.append("../lib")       # for params
import params

from framedSock import framedSend, framedReceive


switchesVarDefaults = (
    (('-s', '--server'), 'server', "127.0.0.1:50001"),
    (('-d', '--debug'), "debug", False), # boolean (set if present)
    (('-?', '--usage'), "usage", False), # boolean (set if present)
    )

progname = "framedClient"
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
        print("creating sock: af = %d, type = %d, proto = %d" % (af, socktype, proto))
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


try:    
    with open("declaration.txt", rb) as inputTxtFile: #open file as binary file, as rb
        while True:
            data = inputTxtFile.read(100)
            print('file opened')
except FileNotFoundError as error:
    print("File not found...")
    sys.exit(0)
   
if not data:
    print("file is empty... ")
    sys.exit(0)

else:
    print("sending... ")
    framedSend(s, b':' + data, debug)
    print("recieved: ", framedReceive(s, debug))
             
s.close()