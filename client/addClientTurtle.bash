if [ $# -eq 0 ]
then
    echo "No arguments supplied"
else
    export ROS_NAMESPACE=/client
    rosservice call spawn 5 5 0  turtle$1
fi
