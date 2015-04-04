import socket
import ach
import ipc_include as ipc

REC_IP = "192.168.1.245"
#REC_IP = "127.0.0.1"
REC_PORT = 5005

receive = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP from process over lan
receive.bind((REC_IP, REC_PORT))

chan = ach.Channel(ipc.CONTROLLER_REF_NAME)
chan.flush()
message = ipc.CONTROLLER_REF()


while True:
	data, addr = receive.recvfrom(1024) # buffer size is 1024 bytes
	message.msg = data
	chan.put(message)
	print data




