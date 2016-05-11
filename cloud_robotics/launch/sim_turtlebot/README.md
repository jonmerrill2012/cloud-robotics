# Simulating Turtlebot with the Cloud Robotics AMCL

Run `roslaunch cloud_robotics sim_turtlebot_nav.launch`

In a new terminal, run:
`roslaunch cloud_robotics server_turtlebot_amcl.launch`

In another new terminal, run:
`rosrun cloud_robotics master.py`

View navigation and send nav goals through RVIZ:
roslaunch turtlebot_rviz_launchers view_navigation.launch --screen
