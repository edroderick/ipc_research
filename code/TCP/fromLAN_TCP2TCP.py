import socket
 
REC_IP = "192.168.1.245"
#REC_IP = "127.0.0.1"
REC_PORT = 5005
SEND_IP = "127.0.0.1"
SEND_PORT = 5006

send = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #TCP SEND
send.connect((SEND_IP, SEND_PORT))

receive = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #TCP Receive
receive.bind((REC_IP, REC_PORT))    
receive.listen(10)
print 'listening'
conn, addr = receive.accept()
print 'Connected with ' + addr[0] + ':' + str(addr[1])

while True:
    data = conn.recv(1024)
    send.send(data)
    print data

