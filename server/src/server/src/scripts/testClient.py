#!/usr/bin/env python
#********************************
# Test client registration with
#   server
#********************************


from server.msg import CurrentClients, NewClient
import rospy
import array
from random import randint

pub = rospy.Publisher('new_client', NewClient, queue_size=10)


def generateId(serverClients):
    notDone = True
    while(notDone):
        robotId = randint(0,100) % 100
        if robotId in serverClients:
            print 'Id is already in use by another robot. Trying again...'
        else:
            notDone = False
            print "id (%s) is not in use. Sending to server..." % robotId
    return robotId


def register_self():
    # Get current ids of server's clients
    rospy.init_node('new_client', anonymous=True)
    msg = rospy.wait_for_message('current_clients', CurrentClients)
    serverClients = list(array.array("B", msg.clientIds))
    print serverClients

    robotId = generateId(serverClients)
    print "generatedId: %s" % robotId

    # publish our id to server
    newClientMSG = NewClient()
    newClientMSG.id = robotId
    pub.publish(newClientMSG)
    print 'published our id \'%s\' to the server' % robotId

    msg = rospy.wait_for_message('current_clients', CurrentClients)
    serverClients = list(array.array("B", msg.clientIds))
    if robotId in serverClients:
        print 'Server successfully registered me.'
    else:
        print 'Server did not successfully register me.'



if __name__ == '__main__':
    register_self()
