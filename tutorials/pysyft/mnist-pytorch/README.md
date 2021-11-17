
# MNIST PyTorch with pysft- federated learning
In this tutorial we solve the [MNIST](http://yann.lecun.com/exdb/mnist/) classification problem in a federated setting using [Pysyft](https://github.com/OpenMined/PySyft/tree/PySyft/syft_0.2.x) with a minimal set-up; a server and three clients. The classifier is implemented in [PyTorch](https://pytorch.org/) using the PyTorch [example](https://github.com/pytorch/examples/tree/master/mnist).

| Machine/function | Type | IP address | PORT | WORKER_ID|
|-|:-|:-|:-|:-|
| Server | virtual | ip.address.database| | |
| Client_1 | AGX Jetson Xavier |  client_ip_1 | 8777 | alice |
| Client_2 | AGX Jetson Xavier |  client_ip_2 | 8778 | bob |
| Client_3 | AGX Jetson Xavier |  client_ip_3 | 8779 | charlie |

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
docker build . -t client
docker run -it -p PORT:PORT client
````

## Server
Log into the server machine.

Clone the Edgelab repo, see the 'Clone the Edgelab repo' section above.

Copy the settings files

Build and launch the server
````bash
docker build . -t server
docker run -it server
````
Pass the clients IP when starting the server
````bash
python3 server.py --client_ip_1 CLIENT_IP_1 --client_ip_2 CLIENT_IP_2 --client_ip_3 CLIENT_IP_3
````

## Preparations for the client
On, for example, your desktop clone the EdgeLab, this, repo
````bash
git clone git@github.com:aidotse/EdgeLab.git
cd tutorials/fedn/mnist-pytorch
````

Build the Docker image
````bash
sh ./package_client_code.sh
````

### Creating a compute package
In order to package the model run
````bash
sh ./package_client_code.sh
````
The created 'package/client_code.tar.gz' file should be uploaded to the reducer via the FEDn dashboard.

### Creating a new initial model
In order to generate an initial model run
````bash
sh ./init_model.sh
````
The created 'package/initial_model.npz' file should be uploaded to the reducer via the FEDn dashboard.


### Train and validate locally (centralized)
Before deploying the model on the clients it is wise to test the models locally running 
````bash
sh ./training.sh
````
and
````bash
sh ./validate.sh.sh
````

## Clients
Copy the 'client/fedn' directory to the clients.

Log into the client host machines.

Go to the '~client/fedn' directory.

In 'remote/client.yaml' set the IP address of the reducer
````bash
discover_host: ip.address.reducer
````

Build the Docker image
````bash
sh ./build.sh
````

Start the clients
````bash
sh ./run.sh
````
Now you should be ready to start a simulation in the FEDn dashboard.

