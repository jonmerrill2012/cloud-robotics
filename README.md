# cloud-robotics
## OSU Senior Capstone 2015-2016

### To run navigation with computation location choice (Turtlebot):

- Start Gazebo:

    `source /opt/ros/indigo/setup.bash`

    `roslaunch turtlebot_gazebo turtlebot_world.launch`

- Start our custom AMCL handler:

    `cd cloud_robotics/server`

    `. devel/setup.bash`
    
    `rosrun server handleAMCL.py client`
 
- New terminal:

    `cd cloud_robotics/server`
    
    `. devel/setup.bash`
    
    `rosrun server mockDiagnostics.py`
    

- Start the AMCL demo:

    `roslaunch turtlebot_gazebo amcl_demo.launch`
 
- Start RVIZ:

    `roslaunch turtlebot_rviz_launchers view_navigation.launch --screen`


### Now, everything should be running as usual.
#### To see our work in action:
- In the terminal that mockDiagnostics.py was run in, type: `s`
    - This causes the AMCL handler to kill the current instance of AMCL
    (started by the AMCL demo), and then start a new instance of it.
    - This new AMCL instance is initialized using the last known pose of
    the robot, as published by the previous instance of AMCL.
    - Some delay/disruption is noticable in the simulator, but overall,
    it works well!

\* NOTE: Don't forget to use our custom AMCL code:
- `cd cloud_robotics/navigation`
- `catkin_make` (will take a long time if this is the first time building the nav package)
- `sudo cp devel/lib/amcl/amcl /opt/ros/indigo/lib/amcl/`

