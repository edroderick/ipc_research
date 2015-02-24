import socket
 
REC_IP = "127.0.0.1"
REC_PORT = 5005
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))    
s.listen(10)
conn, addr = s.accept()
print 'Connected with ' + addr[0] + ':' + str(addr[1])

while True:
    data = conn.recv(1024)
    print data
 

