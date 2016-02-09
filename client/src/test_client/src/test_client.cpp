#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <curl/curl.h>
#include <string>
#include <signal.h>
#include <turtlesim/Pose.h>
#include <turtlesim/TeleportAbsolute.h>
#include <vector>

#include "ros/ros.h"
#include "geometry_msgs/Twist.h"
#include "test_client/input.h"

using std::string;
using std::vector;

string id;
ros::NodeHandle *n;
ros::Publisher pub;

ros::ServiceClient teleportService;

const string BASEURL = "http://localhost:3000";


// Global current state of turtle
turtlesim::Pose currentState;

// 1.0: handle bad requests
string curlResp;
bool isCurlDone = false;
size_t curlCallback(char *ptr, size_t size, size_t nmemb, void *userdata){
    curlResp = ptr;
    isCurlDone = true;
    return size;
}
void sendData(string url, string message){
    CURL *curl = curl_easy_init();

    curl_easy_setopt(curl, CURLOPT_URL, url.c_str());
    curl_easy_setopt(curl, CURLOPT_POSTFIELDS, message.c_str());
    curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, curlCallback);

    curl_easy_perform(curl);

    /* always cleanup */ 
    curl_easy_cleanup(curl); 
}

string createGeoCommand(geometry_msgs::Twist msg){
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


void poseHandler(const turtlesim::Pose::ConstPtr& msg){
    currentState.x = msg->x;
    currentState.y = msg->y;
    currentState.theta = msg->theta;
    currentState.linear_velocity = msg->linear_velocity;
    currentState.angular_velocity = msg->angular_velocity;
}

// returned vector will be [x, y, theta]
vector<float> parseCurlResp(string str){
    vector<float> tokens;
    string buffer = "";

    for(int i = 0; i < str.length(); i++){
        if (str[i] == ','){
            tokens.push_back(atof(buffer.c_str()));
            buffer = "";
        } else {
            buffer += str[i];
        }
    }
    // handle last token 
    tokens.push_back(atof(buffer.c_str()));

    return tokens;
}

void syncState(){
    vector<float> state;
    while (!isCurlDone){}
    isCurlDone = false;

    state = parseCurlResp(curlResp);

    turtlesim::TeleportAbsolute srv;
    srv.request.x = state[0];
    srv.request.y = state[1];
    srv.request.theta = state[2];

    teleportService.call(srv);

    printf("STATE  x:%f y:%f t:%f\n", state[0], state[1], state[2]);
}

string createStateCommand(){
char cmd[1000];
    string x;
    string y;
    string theta;

    sprintf(cmd, "%f", currentState.x);
    x = cmd;
    sprintf(cmd, "%f", currentState.y);
    y = cmd;
    sprintf(cmd, "%f", currentState.theta);
    theta = cmd;

    return "{\"x\":" + x + ",\"y\":" + y + ",\"theta\":" + theta + "}";
}


void inputHandler(const test_client::input::ConstPtr& msg){    
    ros::Rate rate(1);
    geometry_msgs::Twist gmsg;

    string requestBody;
    string command;
    string state;

    char location = msg->location;
    char direction = msg->direction;

    if (location == 'q'){
        exit(0);
    }

    gmsg.linear.x = 0;
    gmsg.linear.y = 0;
    gmsg.linear.z = 0;
    gmsg.angular.x = 0;
    gmsg.angular.y = 0;
    gmsg.angular.z = 0;

    if (direction == 'f'){
        gmsg.linear.x = 2;
    }
    else if (direction == 'b'){
        gmsg.linear.x = -2;
    }
    else if (direction == 'l'){
        gmsg.angular.z = 2;
    }
    else if (direction == 'r'){
        gmsg.angular.z = -2;
    }

    command = createGeoCommand(gmsg);
    state = createStateCommand();

    requestBody = "id=" + id + "&commands=" + command + "&state=" + state;

    if (location == 's'){
        sendData(BASEURL + "/command", requestBody);
        syncState();
    } else {
        pub.publish(gmsg);
    }
    ros::spinOnce();

    rate.sleep();
}

int main(int argc, char **argv){
    char cid[3];

    // get id
    printf("Enter your id: ");
    scanf("%3s", cid);
    getchar();
    id = cid;
    string requestBody = "id=" + id;

    // connect to server
    sendData(BASEURL, requestBody);

    // init ros node
    ros::init(argc, argv, ("client_turtle" + id).c_str());
    ros::NodeHandle node;
    n = &node;

    // create client for teleport service
    teleportService = n->serviceClient<turtlesim::TeleportAbsolute>(
            "client/turtle" + id + "/teleport_absolute");
    
    // create Publisher
    pub = n->advertise<geometry_msgs::Twist>(
            "client/turtle" + id + "/cmd_vel", 1000);

    // create input Subscriber
    ros::Subscriber inputSub = n->subscribe("client/turtle_input" + id, 1000, inputHandler);

    // create turtle pose Subscriber
    ros::Subscriber turtleSub = n->subscribe("client/turtle" + id + "/pose", 1000, poseHandler);


    ros::spin();
    return 0;
}
