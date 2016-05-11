# cloud-robotics
## OSU Senior Capstone 2015-2016

### To run navigation with computation location choice (Turtlebot):

- Open a lot of terminal windows
- Start Gazebo:

    `roslaunch cloud_roboticis/launch/turtlebot/turtlebot.launch`


- Start our laser scan redirect node:

    `rosrun cloud_roboticis master.py`
    
    -In a new terminal:    

    `rosrun server mockDiagnostics.py`
    
    or to use the diagnostics tool:
        
        - New terminal: `iperf -s` *Note: iperf must be installed
        
        - New terminal: `rosrun server diagnose.py`  
    

- Start the client AMCL demo:

    `roslaunch cloud_robotics/launch/turtlebot/client_amcl.launch`


- Start the server AMCL demo:
 
    `roslaunch cloud_robotics/launch/turtlebot/server_amcl.launch`

 
- Start RVIZ:

    `roslaunch turtlebot_rviz_launchers view_navigation.launch --screen`


### To run PR2 simulations (broken):

- Open 3 terminal windows, navigate to `cloud_robotics`
    - Source the project for each terminal window

Terminal 1:

`export ROBOT=sim`

`roslaunch cloud_robotics/launch/pr2/pr2_nav_tutorial.launch`

Terminal 2:

    `roslaunch pr2_navigation_global rviz_move_base.launch`


