#!/usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan

#Note: This reads laser scans from the "scan" topic, 
#       then publishes them to a new topic, which we could use
#       to pass data to the server and back 
pub = rospy.Publisher('laserScanTEST', LaserScan, queue_size=10)



def callback(laserScan):
    # Publishes to new topic, which AMCL is now looking at 
    #   (instead of "scan")
    pub.publish(laserScan)
    print "published scan: %s" % laserScan.header.seq
    


def receiveScans():
    rospy.init_node('laserTEST', anonymous=True)

    # "Scan" is the topic that AMCL receives scans from
    rospy.Subscriber("scan", LaserScan, callback)

    rospy.spin()


if __name__ == '__main__':
    try:
        receiveScans()
    except rospy.ROSInterruptException:
        pass