# cloud-robotics
## OSU Senior Capstone 2015-2016
This project aims to reduce robot battery usage and decrease the robot processor load by performing calculations on a remote server. In this proof of concept, [AMCL](http://wiki.ros.org/amcl) is moved to the server to perform localization computations off-robot. The network diagnostics code will dynamically determine whether AMCL calculations should happen on the server or robot. This is based on network strength. There is also an option to manually set the computation location instead.

For information on the Cloud Robotics project (such as dependencies and specific instructions), see the repository wiki. The following instructions are for running this project on a simulated turtlebot. "Robot" and "Server" are simply two different computers when simulating. 

### Initial Setup
See wiki for dependencies. This must be done on both Robot and Server.

- `mkdir cloud-robotics`
- `cd cloud-robotics`
- `git clone https://github.com/chonny24/cloud-robotics.git`
- `mv cloud-robotics src`
- `cd src`
- `catkin_init_workspace`
- `cd ..`
- `catkin_make`

### ROS Remote Master Set Up
This project relies on ROS multi-machine functionality. We have provided a script to easily configure remote machines. This must be done for each terminal.
###### On Robot:
- navigate to src/cloud-robotics/scripts

- determine ip address: 

    `ifconfig`
- `bash ros_master_setup.bash <robot ip> <robot ip>`

###### On Server:
- navigate to src/cloud-robotics/scripts

- determine ip address: 

    `ifconfig`
- `bash ros_master_setup.bash <robot ip> <server ip>`

### Running the Project
- Source workspace (for each open terminal): 
    
    `source devel/setup.bash`
###### On Robot:

- Start Gazebo: 
    
    `roslaunch cloud_robotics sim_turtlebot_nav.launch`
- Start our laser scan redirect node:

    `rosrun cloud_robotics redirect.py`
- Start RVIZ (can be run on either robot or server):

    `roslaunch turtlebot_rviz_launchers view_navigation.launch --screen`

###### On Server:
- Start the server AMCL demo:
 
    `roslaunch cloud_robotics server_turtlebot_amcl.launch`

###### Diagnostics:
**Option 1**: Automatic computation location switching

- **On Server**: Start iperf:

    `iperf -s`
- **On Robot**: Start network diagnostic node:

    `rosrun cloud_robotics diagnose.py <server ip>`

**Option 2**: Manual computation location switching

- **On either Robot or Server**: Start mockDiagnostic node:

    `rosrun cloud_robotics mockDiagnostics.py`

 
### Usage
- In RVIZ, give the turtlebot navigation goals by clicking the 2D Nav Goal button to move the robot around.
- **For manual computation location switching**: In mockDiagnostics terminal, enter `s` to switch computation to the server; `r` to switch to robot; `q` to quit.
