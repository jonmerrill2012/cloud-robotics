#include <stdio.h>
#include <stdlib.h>
#include <string>

#include "ros/ros.h"
#include "test_client/input.h"

using std::string;

test_client::input createCommand(string id, char direction, char location){
    test_client::input input;
    input.id = id;
    input.direction = direction;
    input.location = location;

    return input;
}

int main(int argc, char **argv){
    char cid[3];

    // get id
    printf("Enter your id: ");
    scanf("%3s", cid);
    getchar();

    string id = cid;

    // init ros node
    ros::init(argc, argv, ("client_turtle_input" + id).c_str());
    ros::NodeHandle n;
    
    // create Publisher
    ros::Publisher pub = n.advertise<test_client::input>(
            "client/turtle_input" + id, 1000);
    ros::Rate rate(1);

    test_client::input msg;
    // input loop
    char input[3] = "0";
    char location;
    char direction;
    while (strcmp(input, "q")){

        printf("local, server, or quit (l, s, q): ");
        scanf("%s", input);
        getchar();
        location = input[0];

        if (!strcmp(input, "q")){
            msg = createCommand(id, 'q', 'q');
            pub.publish(msg);
            break;
        }

        printf("Input a direction or quit (f b l r q): ");
        scanf("%s", input);
        getchar();
        direction = input[0];

        msg = createCommand(id, direction, location);

        pub.publish(msg);
        ros::spinOnce();

        rate.sleep();
    }

    return 0;
}
