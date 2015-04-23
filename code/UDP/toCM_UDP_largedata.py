import socket
import serial

REC_IP = "127.0.0.1"
REC_PORT = 5006

#ser = serial.Serial('/dev/ttyAMA0', 9600)
#ser = serial.Serial('/dev/ttyACM0', 9600)

receive = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP from process 1st internal process
receive.bind((REC_IP, REC_PORT))

while True:
	data, addr = receive.recvfrom(65010) # buffer size is 1024 bytes
	ser.write(data[-1:])
	print 'write ', data[-1:]




