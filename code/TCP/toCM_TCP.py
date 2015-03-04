import socket
import serial

REC_IP = "127.0.0.1"
REC_PORT = 5006

ser = serial.Serial('/dev/ttyAMA0', 9600)
#ser = serial.Serial('/dev/ttyACM0', 9600)

receive = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # UDP from process 1st internal process
receive.bind((REC_IP, REC_PORT))
receive.listen(10)
print 'listening'
conn, addr = receive.accept()
print 'Connected with ' + addr[0] + ':' + str(addr[1])

while True:
	data = conn.recv(1024)
	ser.write(data)
	print 'write ', data




