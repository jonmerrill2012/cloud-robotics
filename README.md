# cloud-robotics
## OSU Senior Capstone 2015-2016
For information running the Cloud Robotics project on a robot, see the wiki pages.

### To run navigation with computation location choice (Turtlebot):

- Open a lot of terminal windows
- Start Gazebo:

    `roslaunch cloud_robotics launch/turtlebot/turtlebot.launch`


- Start our laser scan redirect node:

    `rosrun cloud_roboticis master.py`
    
    -In a new terminal:    

    `rosrun server mockDiagnostics.py`
    
    or to use the diagnostics tool:
        
        - New terminal: `iperf -s` *Note: iperf must be installed
        
        - New terminal: `rosrun server diagnose.py`  
    

- Start the client AMCL demo:

    `roslaunch cloud_robotics/ aunch/turtlebot/client_amcl.launch`


- Start the server AMCL demo:
 
    `roslaunch cloud_robotics launch/turtlebot/server_amcl.launch`

 
- Start RVIZ:

    `roslaunch turtlebot_rviz_launchers view_navigation.launch --screen`
