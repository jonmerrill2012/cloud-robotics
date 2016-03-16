#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

if __name__=="__main__":
    rospy.init_node('interrupt_move')
    #pub = rospy.Publisher('~cmd_vel', Twist, queue_size=5)
    pub = rospy.Publisher('cmd_vel_mux/input/teleop', Twist, queue_size=5)
    while(1):
        twist = Twist()
        twist.linear.x = 0; twist.linear.y = 0; twist.linear.z = 0
        twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0
        pub.publish(twist)
