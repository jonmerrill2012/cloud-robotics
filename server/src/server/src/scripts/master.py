#!/usr/bin/env python
#****************************************
# Handles registration of clients on
#   server side
#****************************************
import rospy
from sensor_msgs.msg import LaserScan
from server.msg import CurrentClients, NewClient

# Change to publish list of clients that we have
pub = rospy.Publisher('current_clients', CurrentClients, queue_size=10)

# These are the current clients that we are servicing
clientIds = []

# Keep advertising the robotIds that server is servicing
def talker():
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        currentClients = CurrentClients()
        currentClients.clientIds = clientIds
        pub.publish(currentClients)
        print 'all clients: %s' % clientIds
        rate.sleep()


def registerNew(newClientMSG):
    newId = newClientMSG.id
    if newId in clientIds:
        print "Robot with conflicting id (%s) tried to register" % newId
        return
    else:
        clientIds.append(newId)
        ##########################################
        # TODO: Spin up new AMCL node
        # Set it to accept msgs w/id of new clients
        ##########################################


def initialize():
    # publishes clients we are currently servicing
    rospy.init_node('current_clients', anonymous=True)

    # listen for new clients
    rospy.Subscriber('new_client', NewClient, registerNew)

    # Publish all of the clients that we have
    talker()



if __name__ == '__main__':
    try:
        initialize()
    except rospy.ROSInterruptException:
        pass
