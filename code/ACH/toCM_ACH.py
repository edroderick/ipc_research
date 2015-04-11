import ach
import serial
import ipc_include as ipc

ser = serial.Serial('/dev/ttyAMA0', 9600)
#ser = serial.Serial('/dev/ttyACM0', 9600)

chan = ach.Channel(ipc.CONTROLLER_REF_NAME)
chan.flush()
message = ipc.CONTROLLER_REF()

while True:
	[status, framesize] = chan.get(message, wait=True, last=True)	
	#print message.msg
	ser.write(message.msg)
	print 'write ', message.msg

