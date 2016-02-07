#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <curl/curl.h>
#include <string>
#include <signal.h>

#include "ros/ros.h"
#include "geometry_msgs/Twist.h"

using std::string;

void sendData(string url, string message){
    CURL *curl = curl_easy_init();

    curl_easy_setopt(curl, CURLOPT_URL, url.c_str());
    curl_easy_setopt(curl, CURLOPT_POSTFIELDS, message.c_str());

    curl_easy_perform(curl);

    /* always cleanup */ 
    curl_easy_cleanup(curl); 
}

string createCommand(geometry_msgs::Twist msg){
    char cmd[1000];
    string linearCommand;
    string angularCommand;

    sprintf(cmd, "%f", msg.linear.x);
    linearCommand = cmd;
    linearCommand = "\"linear\":{\"x\":" + linearCommand + ", \"y\":0, \"z\":0}";
    sprintf(cmd, "%f", msg.angular.z);
    angularCommand = cmd;
    angularCommand = "\"angular\":{\"x\":0, \"y\":0, \"z\":" + angularCommand + "}";

    return "{" + linearCommand + ", " + angularCommand + "}";
}


int main(int argc, char **argv){    
    char direction;
    char cid[3];

    // get id
    printf("Enter your id: ");
    scanf("%3s", cid);
    getchar();

    string id = cid;
    string requestBody = "id=" + id;
    string baseUrl = "http://localhost:3000"; 
    sendData(baseUrl, requestBody);

    // init ros node
    ros::init(argc, argv, ("client_turtle" + id).c_str());
    ros::NodeHandle n;
    
    // create Publisher
    ros::Publisher chatter_pub = n.advertise<geometry_msgs::Twist>(
                                     "client/turtle" + id + "/cmd_vel", 1000);
    ros::Rate rate(1);
    geometry_msgs::Twist msg;

    string command;
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

            command = createCommand(msg);

            requestBody = "id=" + id + "&commands=" + command;
            sendData(baseUrl + "/command", requestBody);
            chatter_pub.publish(msg);

            ros::spinOnce();

            rate.sleep();
        }
    }
    return 0;
}
