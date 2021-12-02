# MNIST Tensorflow - fully distributed federated learning
In this tutorial we solve the [MNIST](http://yann.lecun.com/exdb/mnist/) classification problem in a federated setting using [Flower](https://github.com/adap/flower) with a minimal set-up; a server and two clients. The classifier is implemented in [Tensorflow](https://tensorflow.org/) using the Tensorflow [example](https://github.com/adap/flower/blob/main/src/py/flwr_example/quickstart_tensorflow). (There is also a Pytorch example in the github)

| Machine/function     | Type           | IP address  |
| ------------- |:-------------------------|:----------------|
| Server      | virtual |  ip.address.server|
| Client_1 | AGX Jetson Xavier     |  ip.address.client.1 |
| Client_2 | AGX Jetson Xavier     |  ip.address.client.2 |

All machines are residing on the same local network. Note that the IP addresses in the table above are 'variables' used in this tutorial -you will have to use addresses appropriate for your set-up. 

This is basically an extension of the [Flower quick-pytorch example](https://github.com/adap/flower/tree/main/examples/quickstart_tensorflow). We recommend to go through this example before proceeding here. 

## Setup the Server (The virual machine)
First connect to the VM via SSH and then run the following commands in any folder you would like.
````bash
git clone https://github.com/aidotse/EdgeLab.git
cd EdgeLab/tutorials/flower/mnist-tensorflow/server
````
To start the serverdocker now run these comands:
````bash
sudo docker build --tag flower_tensorflow_server .
sudo docker run -p 8080:8080 -it -v $PWD/model_weights:/server/model_weights flower_tensorflow_server
````
This will first build a docker Image with the tag server-docker, then the second command will create a container and start it. 
The server is now prepared and you can start it by running:
````bash
python3 server.py
````


## Setup the client_1 and client_2 (The AGX Jetson Xaviers)
First connect to the AGX via SSH and then run the following commands in any folder you would like.
````bash
git clone https://github.com/aidotse/EdgeLab.git
cd EdgeLab/tutorials/flower/mnist-tensorflow/client
````
To start the clientdocker now run these comands
````bash
sudo bash build.sh
sudo bash run.sh
````
This will first build a docker Image with the tag client-docker, then the second command will create a container and start it. 
The server is now prepared and you can connect it to the server by running
````bash
python3 client.py ip.address.server:8080
````
<strong>Note</strong>: ip.address.server is the adress of the server i.e. the Virtual Machine.

Now SSH into the second AGX and do the axact same thing.

## Check if it is working
If a loadingbar appears the clients is now training.
![image](https://user-images.githubusercontent.com/90322377/142621239-818c0687-ea0c-460e-8106-434b52093bc0.png)
On the second line you can can check if the training happens on the cpu or the gpu. If it says cuda: 0 you are training on the GPU else it will say cpu.

## Saving the model and customising your strategy
In this tutorial we customised the server strategy to save our models weights and you should be able to find them in your server-docker after the training. To find out more about how to change strategy or even customise it by yourself, visit flowers [docs](https://flower.dev/docs/strategies.html)
