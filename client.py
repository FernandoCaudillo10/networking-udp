import socket

import sys

import threading

port = int(sys.argv[1])

# Client passed in as commandline argument (X/Y)

client = sys.argv[2]

# Name of client (Alice/Bob)

name = sys.argv[3]

# connect with server at port in commandline argument

def getConnection(port, ip):

s = socket.socket()

while True:

try:

s.connect((ip, port))

break

except:

pass

return s

# method to send message to server

def sendMessages(s):

global msgsent

msgsent = "%s: %s"%(client,name)

s.send(msgsent)

# receive message from server

def receiveMessages(s):

msg = s.recv(1024)

print(msgsent)

print(msg)

def main():

ip = '127.0.0.1'

s = getConnection(port,ip)

t = threading.Thread(target=receiveMessages, args=[s])

t.start()

sendMessages(s)

main()