import socket
import serial
import zmq

REC_IP = "127.0.0.1"
REC_PORT = 5006

#ser = serial.Serial('/dev/ttyAMA0', 57600)
ser = serial.Serial('/dev/ttyACM0', 9600)

#receive = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP from process 1st internal process
#receive.bind((REC_IP, REC_PORT))

context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.bind('tcp://%s:%s' % (REC_IP, REC_PORT))

while True:
	#data, addr = receive.recvfrom(1024) # buffer size is 1024 bytes
	data = socket.recv()
	ser.write(data)
	print 'write ', data




