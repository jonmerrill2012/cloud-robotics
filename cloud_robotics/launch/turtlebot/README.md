# Launching (real) Turtlebot with Cloud Robotics' AMCL
Run scripts/ros_master_setup.bash <turtlebot's IP address> <local machine's IP address>

On the Turtlebot's machine, run:
`roslaunch cloud_turtlebot.launch`
`rosrun cloud_robotics master.py`

On a remote machine, run:
`roslaunch cloud_robotics server_turtlebot_amcl.launch` 

To visualize navigation and send nav goals, run:
`roslaunch turtlebot_rviz_launchers view_navigation.launch --screen`
