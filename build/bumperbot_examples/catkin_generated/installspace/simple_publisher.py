#!/usr/bin/env python3

import rospy
from std_msgs.msg import String







if __name__== '__main__':
    
    rospy.init_node('simple_publisher_py', anonymous= True)
    pub =rospy.Publisher('chatter', String, queue_size=10)
    r = rospy.Rate(10)
    counter = 0
    while not rospy.is_shutdown():
        hello_msg= "hello world from python: %d"%counter
        pub.publish(hello_msg)
        r.sleep()
        counter += 1
