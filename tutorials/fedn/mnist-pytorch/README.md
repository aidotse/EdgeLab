# MNIST PyTorch - fully distributed federated learning
In this tutorial we solve the [MNIST](http://yann.lecun.com/exdb/mnist/) classification problem in a federated setting using [FEDn](https://github.com/scaleoutsystems/fedn), version 0.3.0, with a minimal set-up; database, reducer, combiner and two clients. The classifier is implemented in [PyTorch](https://pytorch.org/) using the PyTorch [example](https://github.com/pytorch/examples/tree/master/mnist).

| Machine/function     | Type           | IP address  | OS |
| ------------- |:-------------------------|:----------------|:----------------|
| Database      | virtual |  ip.address.database| Ubuntu 20.04.3 LTS |
| Reducer      | virtual      |   ip.address.reducer | Ubuntu 20.04.3 LTS |
| Combiner | virtual     |    ip.address.combiner | Ubuntu 20.04.3 LTS |
| Client_1 | AGX Jetson Xavier     |  ip.address.client.1 | JetPack 4.6 |
| Client_2 | AGX Jetson Xavier     |  ip.address.client.2 | JetPack 4.6 |

All machines residing on the same local network. Note that the IP addresses in the table above are 'variables' used in this tutorial -you will have to use addresses appropriate for your set-up. 

This is basically an extension of the [FEDn mnist-pytorch example](https://github.com/scaleoutsystems/examples/tree/main/mnist-pytorch). We recommend to go through this example before proceeding here.

## Clone the FEDn repo
On the database, reducer and combiner host machines; clone and checkout appropriate FEDn version
````bash
git clone https://github.com/scaleoutsystems/fedn.git
cd fedn
git checkout tags/v0.3.0 -b v0.3.0
````
<!-- git checkout tags/v0.2.3 -b v0.2.3 -->

## Deploy the base services (Minio and MongoDB)
Log into the database host machine.

Clone the FEDn repo and checkout the right version, see the 'Clone the FEDn repo' section above.

For reference see the [FEDn documentation](https://github.com/scaleoutsystems/fedn).

Build and launch the database inside a terminal multiplexer (eg., tmux)
````bash
docker-compose -f config/base-services.yaml up --build
````
Omit the '--build' flag after the first time.

## Reducer
Log into the reducer host machine.

Clone the FEDn repo and checkout the right version, see the 'Clone the FEDn repo' section above.

Copy the settings files
````bash
cp config/settings-reducer.yaml.template config/settings-reducer.yaml
cp config/extra-hosts-reducer.yaml.template config/extra-hosts-reducer.yaml
````

In 'config/settings-reducer.yaml' set the IP address of the database
````bash
host: ip.address.database
storage_hostname: ip.address.database
````

In 'config/extra-hosts-reducer.yaml' set the IP of the combiner
````bash
combiner: ip.address.combiner
````

For reference see the [FEDn documentation](https://github.com/scaleoutsystems/fedn).

Build and launch the reducer inside a terminal multiplexer (eg., tmux)
````bash
docker-compose -f config/reducer-dev.yaml -f config/extra-hosts-reducer.yaml up --build
````
Omit the '--build' flag after the first time.

## Combiner
Log into the combiner host machine.

Clone the FEDn repo and checkout the right version, see the 'Clone the FEDn repo' section above.

Copy the settings files
````bash
cp config/settings-combiner.yaml.template config/settings-combiner.yaml
````

In 'config/settings-combiner.yaml' set the IP address of the reducer
````bash
discover_host: ip.address.reducer
````    

For reference see the [FEDn documentation](https://github.com/scaleoutsystems/fedn).

Build and launch the combiner inside a terminal multiplexer (eg., tmux)
````bash
docker-compose -f config/combiner-dev.yaml up --build
````
Omit the '--build' flag after the first time.

## Preparations for the client
On, for example, your desktop clone the EdgeLab, this, repo
````bash
git clone https://github.com/aidotse/EdgeLab.git
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
Copy the '~/EdgeLab/tutorials/fedn/mnist-pytorch/src/fedn' directory to the clients.

Log into the client host machines.

Go to the '~/fedn' directory.

In 'client.yaml' set the IP address of the reducer
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

