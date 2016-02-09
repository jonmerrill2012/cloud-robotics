# Server

### Setting Up
###### (If you haven't set up yet. Skip any step you have already done)
* Install [Node.js](https://nodejs.org/en/)
* Install [Rosbridge](http://wiki.ros.org/rosbridge_suite)
* After installing Node, intall NVM (Node Version Manager). In a terminal, run:
```
curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.30.2/install.sh | bash
nvm install stable
nvm alias default stable
```
This downloads nvm, installs the latest stable version of node, and then sets node start up with the most recent version
* Install server dependencies. Navigate to the server directory, and run:
```
npm install
```
This looks at the `package.json` file to install all the required dependencies for the nodejs server
* Install the Requests module for the test python client. Run:
```
pip install requests
```

### Running Everything
* Start rosbridge. In a new terminal, run:
```
roslaunch rosbridge_server rosbridge_websocket.launch
```
* Start turtlesim (it is used for testing in place of AMCL). In a new terminal, run:
```
rosrun rosrun turtlesim turtlesim_node
```
* Start the server. In a new terminal, navigate to the server directory and run:
```
node app.js
```
OR, if that fails...
```
nodejs app.js
```
* Run the test python client. In a new terminal, navigate to the server directory and run:
```
python test_client.py
```

##### What you should see once everything is running
###### Python Client
In the python client, you should see a bunch of objects being outputted every second or so. This is the state of the turtle the client is connected to.
###### Turtlesim
In the turtlesim graphical window, you should see a turtle moving around in a regular pattern.
###### Rosbridge
In the rosbridge window, you should see a bunch of subscriber disconnect/connect messages scrolling by.
