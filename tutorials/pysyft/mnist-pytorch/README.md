
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

## Check if it is working
The following output means that it is working.
````bash
Downloading http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz to ../data/MNIST/raw/train-images-idx3-ubyte.gz
100.1%Extracting ../data/MNIST/raw/train-images-idx3-ubyte.gz to ../data/MNIST/raw
Downloading http://yann.lecun.com/exdb/mnist/train-labels-idx1-ubyte.gz to ../data/MNIST/raw/train-labels-idx1-ubyte.gz
113.5%Extracting ../data/MNIST/raw/train-labels-idx1-ubyte.gz to ../data/MNIST/raw
Downloading http://yann.lecun.com/exdb/mnist/t10k-images-idx3-ubyte.gz to ../data/MNIST/raw/t10k-images-idx3-ubyte.gz
100.4%Extracting ../data/MNIST/raw/t10k-images-idx3-ubyte.gz to ../data/MNIST/raw
Downloading http://yann.lecun.com/exdb/mnist/t10k-labels-idx1-ubyte.gz to ../data/MNIST/raw/t10k-labels-idx1-ubyte.gz
180.4%Extracting ../data/MNIST/raw/t10k-labels-idx1-ubyte.gz to ../data/MNIST/raw
Processing...
Done!
2021-11-24 12:23:54,213 INFO dataset.py(l:266) - Scanning and sending data to alice, bob...
2021-11-24 12:24:01,422 DEBUG dataset.py(l:275) - Sending data to worker alice
2021-11-24 12:24:10,941 DEBUG dataset.py(l:275) - Sending data to worker bob
2021-11-24 12:24:13,019 DEBUG dataset.py(l:280) - Done!
2021-11-24 12:24:13,045 INFO server.py(l:290) - Starting epoch 1/2
````

## Additional options
Additional options can be found [here.](https://github.com/aidotse/EdgeLab/blob/1bd6ebd2f58066340ceb49cb6e00885db2eb13e9/tutorials/pysyft/mnist-pytorch/server/server.py#L175)