#!/usr/bin/env python

import rospy
from std_msgs.msg import String
import serial

#ser = serial.Serial('/dev/ttyAMA0', 9600)
rospy.init_node('tocm', anonymous=True)

def callback(data):
    #ser.write(data)
    rospy.loginfo(data.data)

if __name__ == '__main__':
    rospy.Subscriber("link2", String, callback)
    rospy.spin()
