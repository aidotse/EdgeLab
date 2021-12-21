# Federated Learning using Robot Operating System (ROS)

This repository constitute a testbed environment for training [TensorFlow](https://www.tensorflow.org/) models in *federated learning* settings using the communication protocols available in the [Robot Operating System](https://www.ros.org/).

### Why using ROS? 

For this particular testbed, ROS is, purely, used to simplify the communication between _server_ and _clients_ while training a joint model in federated settings. This communication is facilitated by the communication protocols available in ROS, which support both message passing, remote services, as well as shared global parameters -- all of which are transparently communicated between devices in a local network configuration.

## Usage

Open up a terminal and execute the following commands on all devices wich will particapate in the network. OBS this has to be done on both the server and the clients.

```
git clone https://github.com/aidotse/EdgeLearningROS.git
cd EdgeLearningROS/ROS
docker build --tag ros_container .
docker run -it --rm --network host ros_container
```
### Launch a server

When launching a server you will need to specify how many clients are necessary to begin training. Note:You can still connect more clients after the training has begun, they will just enter the trainingloop when they are launched. You also have to specify the ip adress of the servers machine.

To launch a server, execute the runscript.

```
bash run_server.sh SERVER_IP NUM_CLIENTS
```
### Launch a client

You have to first specify the ip adress of the clinets machine. You also have to specify the ip adress of the servers machine. And at last you will have to specify the name of this client.

To launch a client, execute the runscript.

```
bash run_client.sh CLIENT_IP SERVER_IP CLIENT_NAME
```


