import time
from socket import *

#Create UDP server
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)

#time for response
clientSocket.settimeout(1)
#Take in user input
message = raw_input('Input lowercase sentence: ')
#inital time
#i_time = time.time()
address = (serverName, serverPort)

#Used to calculate max,min and average RTT
temp = []
#used to calculate the average of all RTT's
counter = 0.0
#Used to calculate packet loss percantage
counter2 = 0
for i in range(10):
    i_time = time.time()
    sendTime = time.time()
    clientSocket.sendto(message, address)

    try:
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
        f_time = time.time()
        rtt = f_time - i_time
        print modifiedMessage
        print 'Round Trip Time: ' +str(rtt) + ' s'
        temp.append(rtt)
        counter += rtt
    except timeout:
        counter2 += 1
        print 'Request Times out'

counter = counter/len(temp)
print 'Max RTT: ' + str(max(temp)) + ' s'
print 'Min RTT: ' + str(min(temp)) + ' s'
print 'Avgerage RTT: ' + str(counter) + ' s'
print 'Packet loss percentage: ' + str(counter2*10) + '%'
