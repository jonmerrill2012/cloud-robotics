#!/usr/bin/env python
from std_msgs.msg import String
import rospy
import time
import subprocess
import multiprocessing
import sys

# Location of this program ( 1 == server, 0 == robot (local) )
location = -1

# Process to start AMCL
amcl_process = None


def startAmcl():
    subprocess.call(['rosrun', 'amcl', 'amcl'])
    return


def switchAmcl(diagnostic):
    if int(diagnostic.data) == location:
        print "Already there"
        return

    print "Starting teleop"
    teleop_proc = subprocess.Popen(['rosrun', 'server', 'interruptBot.py'])
    time.sleep(2.9)
    
    print "Killing AMCL..."
    subprocess.call(['rosnode', 'kill', 'amcl'])

    print "Starting new AMCL.."
    amcl_process = multiprocessing.Process(target=startAmcl)
    amcl_process.start()

    print "killing teleop..."
    teleop_proc.kill()
    teleop_proc.wait()
    print "Killed teleop"


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
        rospy.Subscriber('diagnostic', String, switchAmcl)
        print "ready."
        rospy.spin()