#!/usr/bin/env python

import socket
import time
import random
import serial
from datetime import datetime
import zmq

#Set IP addresses
SEND_IP = "192.168.1.245"	#static IP of raspberry pi
#SEND_IP = "127.0.0.1"		#for testing purposes on same computer
SEND_PORT = 5005

BUFFER_SIZE = 1024
lastID = 0

#UDP
#send = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#ZMQ
context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.connect('tcp://%s:%s' % (SEND_IP, SEND_PORT))

#TCP
#send = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
#send.connect(SEND_IP, SEND_PORT))

#Initialize USB serial from OpenCM
ser = serial.Serial('/dev/ttyACM1', 9600, timeout=2) #USB Serial for response
ser.flushInput()
ser.flushOutput()

#send test message, resend until correct id received
testID = 'X'
while(lastID != testID):
	#send.sendto(testID, (SEND_IP, SEND_PORT)) #UDP send
	#send.send(testID) #TCP send
	socket.send(testID) #ZMQ send
	lastID = ser.read(1)

#print header for output file
print 'Run', '\t', 'T Sent', '\t', 'T Received', '\t', 'Message ID', '\t', 'dT'	

for i in range(1,10001):

	#create random 1 byte id, ensure differs from last id
	uID = str(random.randint(0,9))
	while(uID == lastID):
		uID = str(random.randint(0,9))

	tick = datetime.now()
	#send.sendto(uID, (SEND_IP, SEND_PORT)) #UDP send
	#send.send(uID) #TCP send
	socket.send(uID) #ZMQ send
        msg = ser.read(1)
	tock = datetime.now()
	if (msg == uID):
		dT = tock-tick
	else:
		dT = 'missed'
	
	lastID = uID
	print i, '\t', tick, '\t', tock, '\t', uID, '\t', dT	

	time.sleep(.01)
