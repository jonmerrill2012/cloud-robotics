if [ $# -lt 2 ]
then
    echo "Required Arguments: <IP of Master> <own IP>"
else
    ping -q -c 1 $1
    if [ $? -eq 0 ]
    then
        export ROS_MASTER_URI=http://$1:11311
        export ROS_IP=$2
    else
        echo "Couldn't contact master"
    fi
fi
