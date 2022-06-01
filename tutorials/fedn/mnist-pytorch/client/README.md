# Client

The external client machines.

## Set-up

Clone the repo

````bash
git clone https://github.com/aidotse/EdgeLab.git
cd EdgeLab/tutorials/fedn/mnist-pytorch/client
````

Copy client 1 and 2, data downloaded on your local machine, to the clint 1 and 2

````bash
~/EdgeLab/tutorials/fedn/mnist-pytorch/client/data/clients/1or2/mnist.pt
````

In the 'client.yaml' change the 'discover_host' ip address to the ip address of your reducer.

In the 'run.sh' change the 'add-host=combiner' ip address to the ip address of your combiner.

Build the docker image

````bash
sh ./build.sh
````

Start the client

````bash
sh ./run.sh
````
