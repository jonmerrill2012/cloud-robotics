#!/usr/bin/env python
from std_msgs.msg import String
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import PoseWithCovarianceStamped
import rospy
import time

servScanPub = rospy.Publisher('server_scan', LaserScan)
clientScanPub = rospy.Publisher('client_scan', LaserScan)
activePub = clientScanPub

servPosePub = rospy.Publisher('server_initial_pose', PoseWithCovarianceStamped)
clientPosePub = rospy.Publisher('client_initial_pose', PoseWithCovarianceStamped)

isLocal = True
latestPose = None


def forwardScan(scan):
    activePub.publish(scan)


def updatePose(pose):
    global latestPose
    latestPose = pose


def switchAmcl(diagnostic):
    global isLocal
    global activePub
    global clientScanPub
    global servScanPub

    if isLocal:
        print "switching to server"
        servPosePub.publish(latestPose)
        activePub = servScanPub
    else:
        print "switching to client"
        clientPosePub.publish(latestPose)
        activePub = clientScanPub
    isLocal = not isLocal


if __name__ == '__main__':
    rospy.init_node('amcl_master', anonymous=True)
    rospy.Subscriber('diagnostic', String, switchAmcl)
    rospy.Subscriber('scan', LaserScan, forwardScan)
    rospy.Subscriber('amcl_pose', PoseWithCovarianceStamped, updatePose)

    print "ready."
    rospy.spin()
