
# MNIST PyTorch with Pysft - federated learning
In this tutorial we solve the [MNIST](http://yann.lecun.com/exdb/mnist/) classification problem in a federated setting using [Pysyft](https://github.com/OpenMined/PySyft/tree/PySyft/syft_0.2.x) with a minimal set-up; a server and two clients. The classifier is implemented in [PyTorch](https://pytorch.org/) using the PyTorch [example](https://github.com/pytorch/examples/tree/master/mnist).


## Note
This tutorial is using an older version of PySyft (0.2.9). This is due to PySyft shifting their focus towards encrypted computation and not Federated Learnning. Read more [here](https://github.com/OpenMined/PySyft). 

This version of PySyft uses an older version of PyTorch and TorchVision. Therefore this tutorial does not work on Nvidia AGX machines. 

| Machine/function | Type | IP address | PORT | WORKER_ID|
|-|:-|:-|:-|:-|
| Server | virtual | ip.address.database| | |
| Client_1 | virtual |  client_ip_1 | 8777 | alice |
| Client_2 | virtual |  client_ip_2 | 8778 | bob |



All devices are residing on the same local network. Note that the IP addresses in the table above are 'variables' used in this tutorial -you will have to use addresses that are appropriate for your set-up. 

This is basically an extension of the [Pystft mnist example](https://github.com/OpenMined/PySyft/tree/PySyft/syft_0.2.x/examples/tutorials/advanced/websockets_mnist). 

## Clone the Edgelab repo
On the server and client machines; clone the Edgelab repo:
````bash
$ git clone https://github.com/aidotse/edgelab.git
$ cd EdgeLab/tutorials/pysyft/mnist-pytorch
````

## Deploy the clients
For each client: 

[Clone the Edgelab repo](#Clone-the-Edgelab-repo)

Log into the client machine.

Build and launch the client (Remember to specify client_port and worker_id) 
````bash
$ cd client
$ docker build . -t client
$ docker run -e PORT=CLIENT_PORT_HERE -e WORKER_ID=CLIENT_WORKER_ID_HERE -it -p CLIENT_PORT_HERE:CLIENT_PORT_HERE client
````

## Server
Log into the server machine.

[Clone the Edgelab repo](#Clone-the-Edgelab-repo)


Build and launch the server container
````bash
$ cd server
$ docker build . -t server
$ docker run -it server
````
Pass the clients IP when starting the server
````bash
$ python3 server.py --client_ip_1 CLIENT_IP_1 --client_ip_2 CLIENT_IP_2
````
