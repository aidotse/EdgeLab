
# MNIST PyTorch with Pysft - federated learning
In this tutorial we solve the [MNIST](http://yann.lecun.com/exdb/mnist/) classification problem in a federated setting using [Pysyft](https://github.com/OpenMined/PySyft/tree/PySyft/syft_0.2.x) with a minimal set-up; a server and three clients. The classifier is implemented in [PyTorch](https://pytorch.org/) using the PyTorch [example](https://github.com/pytorch/examples/tree/master/mnist).


## Note
This tutorial is using an older version of PySyft (0.2.9). This is due to PySyft shifting their focus towards encrypted computation and not Federated Learnning. Read more [here](https://github.com/OpenMined/PySyft).

Due to an older verison of PySyft a older version of PyTorch is requiered. 

| Machine/function | Type | IP address | PORT | WORKER_ID|
|-|:-|:-|:-|:-|
| Server | virtual | ip.address.database| | |
| Client_1 | virtual |  client_ip_1 | 8777 | alice |
| Client_2 | virtual |  client_ip_2 | 8778 | bob |

All machines residing on the same local network. Note that the IP addresses in the table above are 'variables' used in this tutorial -you will have to use addresses appropriate for your set-up. 

This is basically an extension of the [Pystft mnist example](https://github.com/OpenMined/PySyft/tree/PySyft/syft_0.2.x/examples/tutorials/advanced/websockets_mnist). We recommend to go through this example before proceeding here.

## Clone the Edgelab repo
On the server and client machines; clone the Edgelab repo
````bash
git clone https://github.com/aidotset/edgelab.git
cd tutorial/pysyft/mnist-pytorch
````

## Deploy the clients
For each client: 

Log into the client machine.

Clone the Edgelab repo, see the 'Clone the Edgelab repo' section above.

Build and launch the client
````bash
cd client
docker build . -t client
docker run -e PORT=CLIENT_PORT -e WORKER_ID=CLIENT_WORKER_ID -it -CLIENT_PORT:CLIENT_PORT client
````

## Server
Log into the server machine.

Clone the Edgelab repo, see the 'Clone the Edgelab repo' section above.

Note the IP adresses of the clients. 

Build and launch the server
````bash
cd server
docker build . -t server
docker run -it server
````
Pass the clients IP when starting the server
````bash
python3 server.py --client_ip_1 CLIENT_IP_1 --client_ip_2 CLIENT_IP_2
````

