export ROS_IP=$1
export ROS_MASTER_URI="http://${1}:11311"

chmod +x -R .
source devel/setup.bash
roslaunch fed_lr_ros server.launch model:=cnn expected_clients:=$2
