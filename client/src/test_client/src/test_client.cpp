#include<stdio.h>
#include<unistd.h>

#include "ros/ros.h"
#include "geometry_msgs/Twist.h"

int main(int argc, char **argv){
    char direction;
    char id[2];

    // get id
    printf("Enter your id: ");
    scanf("%2s", id);

    // init ros node
    ros::init(argc, argv, "turtle");
    ros::NodeHandle n;
    
    // create Publisher
    ros::Publisher chatter_pub = n.advertise<geometry_msgs::Twist>("turtle1/cmd_vel", 1000);
    ros::Rate rate(1);
    geometry_msgs::Twist msg;

    // input loop
    while (direction != 'q'){
        printf("Input a direction (f b l r) or quit (q): ");
        while((direction = getchar()) != '\n'){

            if (direction == 'q'){
                break;
            }

            msg.linear.x = 0;
            msg.linear.y = 0;
            msg.linear.z = 0;
            msg.angular.x = 0;
            msg.angular.y = 0;
            msg.angular.z = 0;

            if (direction == 'f'){
                msg.linear.x = 2;
            }
            else if (direction == 'b'){
                msg.linear.x = -2;
            }
            else if (direction == 'l'){
                msg.angular.z = 2;

            }
            else if (direction == 'r'){
                msg.angular.z = -2;
            }

            chatter_pub.publish(msg);

            ros::spinOnce();

            rate.sleep();
        }
    }

    return 0;
}
