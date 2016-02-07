// module includes
var express = require('express');
var bodyParser = require('body-parser');
var ROSLIB = require('roslib');
var exec = require('child_process').exec;

// initialize our express web app
var app = express();

// allow us to parse json in POST requets
app.use(bodyParser.urlencoded({extended: false}));
app.use(bodyParser.json());


// hold the states of all connected robots
states = {};

function disconnect_robot(id) {
    // kill ROS process
    var kill = exec('rosservice call kill turtle' + id, function (err, stdout, stderr){});
    states[id].process.kill('SIGINT')
    // clean up states Object
    delete states[id];
    
}

function check_timeouts(){
    for (id in states) {
        // if a robot hasn't sent a message in 2 minutes, delete it
        if (states[id].last_connect < Date.now() - (120 * 1000)){
            disconnect_robot(id);
        }
    }
}

// connect a robot. Returns null if all went well. Returns something if there was an err
function connect_robot(id) {
    if (Object.keys(states).length === 0) {
        var turtle = exec('rosrun turtlesim turtlesim_node', function (err, stdout, stderr){
            if (err || stderr){
                return err || stderr
            } 
        });
    } else {
        var turtle = exec('rosservice call spawn 5 5 0 turtle' + id, function (err, stdout, stderr){
            if (err || stderr){
                return err || stderr
            }
        });
    }

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
        talker: talker,
        last_connect: Date.now(),
        process: turtle
    }

    return null;
}

// accept a robot connection request at our base url
app.post('/', function root (req, res) {
    // get the id from the robot
    var id = req.body.id;
    if (id in states) {
        var err = 'Duplicate ID';
    }

    // connect the robot
    var err2 = connect_robot(id);

    if (err || err2) {
        res.sendStatus(400).end(err || err2);
    } else {
        res.sendStatus(200).end();
    }
});

// accept a robot command at <url>/command
app.post('/command', function command (req, res) {
    // get id and commands from robot
    var id = req.body.id;
    var data = JSON.parse(req.body.commands);

    // In case server goes down, we can reconnect a robot without robot knowing
    if (!(id in states)) {
        var err = connect_robot(id);
    }

    states[id].last_connect = Date.now()
    // upload state

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

            // now is a good time to check for timeouts
            check_timeouts();
        }
    });

    // publish our message
    states[id].talker.publish(twist);
    published = 1;
});

// disconnect a robot when it asks to be disconnected
app.post('/disconnect', function disconnect (req, res) {
    var id = req.body.id;
    disconnect_robot(id);
    res.sendStatus(200).end();
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
