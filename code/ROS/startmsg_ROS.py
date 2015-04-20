#!/usr/bin/env python

import rospy
from std_msgs.msg import String

rospy.init_node('startmsg', anonymous=True)
pub = rospy.Publisher('link1', String, queue_size=10)

def talker():
    while not rospy.is_shutdown():
        pub.publish('x')
        rospy.loginfo('x')

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
