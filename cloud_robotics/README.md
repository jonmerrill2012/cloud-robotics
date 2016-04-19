# cloud-robotics
## OSU Senior Capstone 2015-2016

### To run PR2 simulations (not totally functional yet):

- Open 3 terminal windows, navigate to `cloud_robotics`
    - Source the project for each terminal window

Terminal 1:

    `roslaunch launch/other/test.launch`

Terminal 2:

    `roslaunch pr2_navigation_global rviz_move_base.launch`

Terminal 3: 
    `roslaunch /launch/other/amclpr2.launch`


### To run navigation with computation location choice (Turtlebot):

- Open 6 terminal windows, navigate to `cloud_robotics/launch`

- Start Gazebo:

    `roslaunch ./turtlebot.launch`

- Start our custom AMCL handler:

    `. devel/setup.bash`
    
    `rosrun cloud_roboticis master.py`
    
    -In a new terminal:    

    `cd cloud_robotics/server`
    
    `. devel/setup.bash`
    
    `rosrun server mockDiagnostics.py`
    

- Start the client AMCL demo:

    `roslaunch ./client_amcl.launch`


- Start the server AMCL demo:
 
    `roslaunch ./server_amcl.launch`

 
- Start RVIZ:

    `roslaunch turtlebot_rviz_launchers view_navigation.launch --screen`
