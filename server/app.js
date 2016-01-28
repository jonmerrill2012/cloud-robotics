// module includes
var express = require('express');
var bodyParser = require('body-parser');
var ROSLIB = require('roslib');

// initialize our express web app
var app = express();

// allow us to parse json in POST requets
app.use(bodyParser.urlencoded({extended: false}));
app.use(bodyParser.json());


// hold the states of all connected robots
states = {};

// accept a POST request at our base url
// when we get a request, we enter the contained function
app.post('/', function root (req, res) {
    // get the id from the robot
    var id = req.body.id;

    // tap into a ros topic that we can talk to 
    // (Currently using turtlesim stuff for testing)
    var talker = new ROSLIB.Topic({
        ros: ros,
        name: 'turtle' + id + '/cmd_vel',
        messageType : 'geometry_msgs/Twist'
    });

    // update the state for the robot
    states[id] = {
        state: {},
        talker: talker
    }

    // send a 200 response and end the request
    res.sendStatus(200).end();
});

// accept a POST request at <url>/command
// when we get a request, we enter the contained function
app.post('/command', function command (req, res) {
    // get id and commands from robot
    var id = req.body.id;
    var data = req.body.rosData;

    // construct a message of the correct type for our "talker" topic using POST data
    var twist = new ROSLIB.Message({
        linear : {
          x : data.linear.x,
          y : data.linear.y,
          z : data.linear.z 
        },
        angular : {
          x : data.angular.x,
          y : data.angular.y, 
          z : data.angular.z
        }
    });

    // tap in to a ROS topic we can listen Topic
    // (currently using turtlesim stuff for testing)
    var listener = new ROSLIB.Topic({
        ros: ros,
        name: 'turtle' + id + '/pose',
        messageType: 'turtlesim/Pose'
    });

    published = 0;

    // subscribe to our topic
    // enter the contained function when we get a message
    listener.subscribe(function(message) {
        // we only want to read the data after we publish and the turtle has stopped
        if (published === 1 && message.linear_velocity === 0 && message.angular_velocity === 0) {
            // unsubscribe from the topic so we stop getting messages
            listener.unsubscribe();

            // update the robot state
            states[id].state = message
            // send the state back to the robot and end the request
            res.end(JSON.stringify(message));
        }
    });

    // publish our message
    states[id].talker.publish(twist);
    published = 1;
});

// connect to ROS
var ros = new ROSLIB.Ros({
    url: 'ws://localhost:9090'
});

// on ROS connection...
ros.on('connection', function() {
    console.log('connected to ROS');
    // spin up server on port 3000
    app.listen(3000);
});

// on ROS connection error...
ros.on('error', function(err) {
    console.log(err);
});
