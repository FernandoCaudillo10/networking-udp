## Nicholas Cerda
## Fernando Caudillo

import time
import random
from socket import *

clientSocket = socket(AF_INET, SOCK_DGRAM)

clientSocket.settimeout(1)
message = raw_input('Input lowercase sentence: ')
address = ('localhost', 12000)

rttStack = []
packetLostCounter = 0

for i in range(10):
	print '*************************'
	start = time.time()
	print 'Ping ' + str(i) + ' ' + str(time.strftime("%H:%M:%S"))
	clientSocket.sendto(message, address)

	try:
		response, serverAddress = clientSocket.recvfrom(2048)
		done = time.time()
		rtt = done - start
		rttStack.append(rtt)
		print response
		print 'Round Trip Time: ' + str(rtt) + ' s'

	except timeout:
		packetLostCounter += 1
		print 'Request Timed out'
	print '*************************'
	print '\n'

EstimatedRTT=0.0
DevRTT=0.0
alpha=0.125
beta=.25
for x in range(len(rttStack)):
	SampleRTT=random.choice(rttStack)
	EstimatedRTT=(1-alpha)*EstimatedRTT+alpha*SampleRTT
	DevRTT=(1-beta)*DevRTT+beta*abs(SampleRTT-EstimatedRTT)

print '\n'
print 'Max. RTT: ' + str(max(rttStack)) + ' s'
print 'Min. RTT: ' + str(min(rttStack)) + ' s'
print 'Avgerage RTT: ' + str(sum(rttStack) / len(rttStack)) + ' s'
print 'Packets lost: ' + str(packetLostCounter*10) + '%'
print 'Estimated RTT: ' + str(EstimatedRTT) + ' s'
print 'DevRTT: ' + str(DevRTT) + ' s'
print '\n\n'
