# Client

The external client machines.

## Set-up

Clone the repo

````bash
git clone https://github.com/aidotse/EdgeLab.git
cd EdgeLab/tutorials/fedn/mnist-pytorch/client
````

Copy client 2, data downloaded on your local machine, to the clint 2
Clone the repo

````bash
MY_ROOT_PATH/bycatch/fedex/client/data/clients/2/mnist.pt
````

In the 'client.yaml' change the 'discover_host' ip address to the ip address of your reducer.

In the 'run.sh' change the 'add-host=combiner' ip address to the ip address of your combiner.

(In this setup the ip address of the reducer and combiner is the same since they reside on the same machine.)

Build the docker image

````bash
sh ./build.sh
````

Start the client

````bash
sh ./run.sh
````
