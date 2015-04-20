#!/usr/bin/env python

import rospy
from std_msgs.msg import String
   
rospy.init_node('fromlan', anonymous=True)
pub = rospy.Publisher('link2', String, queue_size=1000)

def callback(data):
    pub.publish(data.data)
    rospy.loginfo(data.data)

if __name__ == '__main__':
    rospy.Subscriber("link1", String, callback)
    rospy.spin()
