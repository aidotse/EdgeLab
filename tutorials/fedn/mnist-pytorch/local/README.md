# Local

On your local machine (or in fact any machine that is convenient for you).

## Set-up

Clone the repo

````bash
git clone https://github.com/aidotse/EdgeLab.git
cd EdgeLab/tutorials/fedn/mnist-pytorch/local
````

Build the virtual environment

````bash
./init_venv.sh
````

Download and split the data

````bash
venv/bin/python3 src/get_data
venv/bin/python3 src/split_data
````

Package the code

````bash
./package.sh
````

This will package the client code to the 'package.tgz.' file.

Build the initial model

````bash
./init_seed.sh
````

This will initiate the model with random wights and save the model to the 'seed.npz' file.

The client code, 'package.tgz' and the initial model 'seed.npz' will be uploaded to the clients via the FEDn dashboard.
