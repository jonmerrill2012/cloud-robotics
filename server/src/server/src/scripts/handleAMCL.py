#!/usr/bin/env python
from geometry_msgs.msg import PoseWithCovarianceStamped
from server.msg import ComputationLocation
import rospy
import time
import subprocess
import multiprocessing
import sys

# Publisher for custom topic to initialize AMCL to a new position
pub_pose_init = rospy.Publisher('pose_init', PoseWithCovarianceStamped, queue_size=10)

# Last published pose from AMCL
amcl_pose = None

# Location of this program ( 1 == server, 0 == robot (local) )
location = -1

# Process to start AMCL
amcl_process = None

# If AMCL has published a pose 
amcl_pose_recvd = False


def updatePose(pose):
    global amcl_pose_recvd 
    amcl_pose_recvd = True
    global amcl_pose 
    amcl_pose = pose 

def startAmcl():
    subprocess.call(['rosrun', 'amcl', 'amcl'])

def switchAmcl(diagnostic):
    print "switching..."
    if diagnostic.location == location:
        return

    print "Killing AMCL..."
    
    #TODO: May want to check that AMCL has successfully been killed
    subprocess.call(['rosnode', 'kill', '/amcl'])
    
    print "Starting new AMCL..."
    amcl_process = multiprocessing.Process(target=startAmcl)
    amcl_process.start() 
    # TODO: Figure out when to join, or if we need to...

    # TODO: Do we need to check to make sure AMCL received this?
    print "publishing init pose:"
    print "%s" % amcl_pose
    pub_pose_init.publish(amcl_pose)

    print "Initialization of new AMCL complete."



if __name__ == '__main__':
    if(len(sys.argv) < 2):
        print "Enter \"client\" or \"server\" as a command line argument."
        exit(0)

    amcl_type = sys.argv[1]
    if amcl_type == 'client':
        location = 0
    elif amcl_type == 'server':
        location = 1
    else:
        print "please specify either server or client"

    if location != -1:
        rospy.init_node('amcl_' + sys.argv[1], anonymous=True)
        rospy.Subscriber('amcl_pose', PoseWithCovarianceStamped, updatePose)
        rospy.Subscriber('diagnostic', ComputationLocation, switchAmcl)
        print "spinning..."
        rospy.spin()