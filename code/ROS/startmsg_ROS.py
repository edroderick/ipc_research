#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from datetime import datetime
import serial
import time
import random

rospy.init_node('startmsg', anonymous=True)
pub = rospy.Publisher('link1', String, queue_size=None)
rate = rospy.Rate(100)

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=2) #USB Serial for response
ser.flushInput()
ser.flushOutput()

def talker():
    lastID = 0

    #test message code
    testID = 'X'
    while(lastID != testID):
	#print 'sending testid'
	pub.publish(testID)
	lastID = ser.read(1)



    for i in range (1, 10001):
	uID = str(random.randint(0,9))
	while(uID == lastID):
		uID = str(random.randint(0,9))

	tick = datetime.now()
	pub.publish(uID)
	msg = ser.read(1)
	tock = datetime.now()
	if (msg == uID):
		dT = tock-tick
	else:
		dT = 'missed'

	lastID = uID
	print i, '\t', tick, '\t', tock, '\t', uID, '\t', dT
	rate.sleep()
	
if __name__ == '__main__':
    #output file header
    print 'Run', '\t', 'T Sent', '\t', 'T Received', '\t', 'Message ID', '\t', 'dT'

    try:
        talker()
    except rospy.ROSInterruptException:
        pass
