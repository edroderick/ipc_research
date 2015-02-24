#!/usr/bin/env python

import curses
import socket
import time

#initialize UDP Socket
UDP_IP = "192.168.1.245"	#static IP of raspberry pi
#UDP_IP = "127.0.0.1"		#for testing purposes on same computer
UDP_PORT = 5005
print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP

#intialize curses module
stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(True)
curses.halfdelay(1)


lastmessage = "0"

# Get the current feed-forward (state) 
while (True):
 	#clear buffer to prevent overwhelming RasPI with UDP messages when directional keys held down
	curses.flushinp()
	inputKey = stdscr.getch()
	if inputKey == ord('x'): #exit on X key and close curses module and ach channel
		curses.nocbreak()
		stdscr.keypad(False)
		curses.echo()
		curses.endwin()
		break
	elif inputKey == curses.KEY_RIGHT:
		MESSAGE = "R"
	elif inputKey == curses.KEY_LEFT:
		MESSAGE = "L"		
	elif inputKey == curses.KEY_UP:
		MESSAGE = "F"		
	elif inputKey == curses.KEY_DOWN:
		MESSAGE = "B"	
	else:
		MESSAGE = "S"

	#tick = time.clock()
	if (lastmessage != MESSAGE):
		sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
	#wait for usb serial response
	#dT = tock - tick
	lastmessage = MESSAGE
	time.sleep(.01)
