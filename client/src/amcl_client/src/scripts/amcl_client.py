#!/usr/bin/env python
import rospy
import json
from sensor_msgs.msg import LaserScan
from rospy_message_converter import message_converter, json_message_converter
import requests

#Note: This reads laser scans from the "scan" topic, 
#       then publishes them to a new topic, which we could use
#       to pass data to the server and back 
pub = rospy.Publisher('laserScanTEST', LaserScan, queue_size=10)



def callback(laserScan):
    jsonScan = json_message_converter.convert_ros_message_to_json(laserScan)

    # Someday we need to figure out a better way to handle NaN
    jsonScan = json.loads(jsonScan.replace("NaN", "1000000000000.0"))
    
    
    response = requests.post('http://192.168.1.33:3000/amcl', json=jsonScan)
    jsonScan = response.json()

    recvdScan = LaserScan()
    recvdScan.header.seq = jsonScan["header"]["seq"]
    recvdScan.header.stamp.nsecs = jsonScan["header"]["stamp"]["nsecs"]
    recvdScan.header.stamp.secs = jsonScan["header"]["stamp"]["secs"]

    # handle unicode string better from json
    recvdScan.header.frame_id = "/camera_depth_frame"#jsonScan["header"]["frame_id"]

    recvdScan.angle_min = jsonScan["angle_min"]
    recvdScan.angle_max = jsonScan["angle_max"]
    recvdScan.angle_increment = jsonScan["angle_increment"]
    recvdScan.scan_time = jsonScan["scan_time"]
    recvdScan.range_max = jsonScan["range_max"]
    recvdScan.range_min = jsonScan["range_min"]
    recvdScan.ranges = jsonScan["ranges"]
    recvdScan.intensities = []

    pub.publish(recvdScan)


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