export ROS_IP=$1
export ROS_MASTER_URI="http://${2}:11311"

chmod +x -R .
source devel/setup.bash
roslaunch gossip_lr_ros client.launch model:=cnn name:=$3 expected_clients:=2
