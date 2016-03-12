#!/usr/bin/env python
from std_msgs.msg import String
import rospy
import time
import subprocess
import multiprocessing
import sys


# Location of this program ( 1 == server, 0 == robot (local) )
location = -1
isHere = None
last_switch = None

# Process to start AMCL
amcl_process = None


def startAmcl():
    subprocess.call(['rosrun', 'amcl', 'amcl'])
    return


def switchAmcl(diagnostic):
    global isHere
    global last_switch
    global location
    global amcl_process

    if int(diagnostic.data) != location:
        print "Signal being handled on other side"
        isHere = False
        return

    if isHere:
        return

    if last_switch != None:
        if (location == 1 and time.time() < last_switch + 20):
            print "Not switching from client due to unstable network"
            return

    isHere = True
    print "Starting interrupt"
    teleop_proc = subprocess.Popen(['rosrun', 'server', 'interruptBot.py'])
    time.sleep(3)
    
    print "Killing AMCL..."
    subprocess.call(['rosnode', 'kill', 'amcl'])

    print "Starting new AMCL.."
    amcl_process = multiprocessing.Process(target=startAmcl)
    amcl_process.start()

    print "killing interrupt..."
    teleop_proc.kill()
    teleop_proc.wait()
    print "Killed interrupt"
    last_switch = time.time()

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
        sys.exit(0)

    rospy.init_node('amcl_' + sys.argv[1], anonymous=True)
    isHere = not location
    rospy.Subscriber('diagnostic', String, switchAmcl)
    print "ready."
    rospy.spin()