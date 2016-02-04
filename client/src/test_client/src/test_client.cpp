#include<stdio.h>

#include "ros/ros.h"
#include "geometry_msgs/Twist.h"

int main(int argc, char **argv){
    char direction;
    ros::init(argc, argv, "turtle");
    ros::NodeHandle n;
    
    ros::Publisher chatter_pub = n.advertise<geometry_msgs::Twist>("turtle1/cmd_vel", 1000);
    ros::Rate loop_rate(10);

    printf("Input a direction (F B L R): ");
    direction = getchar();

    geometry_msgs::Twist msg;
    msg.linear.x = 0;
    msg.linear.y = 0;
    msg.linear.z = 0;
    msg.angular.x = 0;
    msg.angular.y = 0;
    msg.angular.z = 0;

    if (direction == 'F'){
        msg.linear.x = 2;
    }
    else if (direction == 'B'){
        msg.linear.x = -2;
    }
    else if (direction == 'L'){
        msg.angular.z = 2;

    }
    else if (direction == 'R'){
        msg.angular.z = -2;
    }

    chatter_pub.publish(msg);
    ros::spinOnce();

    return 0;
}
