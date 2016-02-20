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

### Running Everything
* Start rosbridge. In a new terminal, run:
```
roslaunch rosbridge_server rosbridge_websocket.launch
```
* Start the server. In a new terminal, navigate to the server directory and run:
```
node app.js
```
* Start the client stuff in new terminals (either AMCL or turtlesim at the moment)
