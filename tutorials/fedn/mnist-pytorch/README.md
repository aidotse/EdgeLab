# MNIST PyTorch - fully distributed federated learning

In this tutorial we solve the [MNIST](http://yann.lecun.com/exdb/mnist/) classification problem in a federated setting using [FEDn](https://github.com/scaleoutsystems/fedn), version 0.3.2, with a minimal set-up; database, reducer, combiner and two clients. The classifier is implemented in [PyTorch](https://pytorch.org/).

| Machine/function     | Type           | IP address  | OS |
| ------------- |:-------------------------|:----------------|:----------------|
| Database      | virtual |  ip.address.database| Ubuntu 20.04.3 LTS |
| Reducer      | virtual      |   ip.address.reducer | Ubuntu 20.04.3 LTS |
| Combiner | virtual     |    ip.address.combiner | Ubuntu 20.04.3 LTS |
| Client_1 | AGX Jetson Xavier     |  ip.address.client.1 | JetPack 5.0.1-b118 |
| Client_2 | AGX Jetson Xavier     |  ip.address.client.2 | JetPack 5.0.1-b118 |

All machines residing on the same local network. Note that the IP addresses in the table above are 'variables' used in this tutorial -you will have to use addresses appropriate for your set-up.

This is basically an extension of the [FEDn mnist-pytorch example](https://github.com/scaleoutsystems/fedn/tree/master/examples/mnist-pytorch). We recommend to go through this example before proceeding here.

## Prerequisites

You will need have docker and docker-compose installed, see for example [Install Docker Engine on Ubuntu](https://docs.docker.com/engine/install/ubuntu/).

## Clone the FEDn repo

On the database, reducer and combiner host machines; clone and checkout appropriate FEDn version

````bash
git clone https://github.com/scaleoutsystems/fedn.git
cd fedn
git checkout tags/v0.3.2 -b v0.3.2
````

## Deploy the base services (Minio and MongoDB)

Log into the database host machine.

Clone the FEDn repo and checkout the right version, see the 'Clone the FEDn repo' section above.

Build and launch the data base

````bash
docker compose -f config/base-services.yaml up -d
````

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

Build and launch the reducer

````bash
docker compose -f config/reducer-dev.yaml -f config/extra-hosts-reducer.yaml up -d
````

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

Build and launch the combiner

````bash
docker compose -f config/combiner-dev.yaml up -d
````

## Preparations for the client

Follow the instructions in [README.md](local/README.md) which will; download the data, build the initial model and package the client code.

## Clients

Follow the instructions in [README.md](client/README.md) which will; upload the data to the clients and build and start the client docker images.

## Run the training

Now you should be ready to start the training in the FEDn dashboard.
