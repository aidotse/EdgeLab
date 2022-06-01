#!/bin/bash

set -e

IMAGE_NAME="fedn_mnist_env"

ROOT_DIR=$PWD

docker run --ipc=host -it --rm --runtime nvidia \
-v $ROOT_DIR:/home/$USERNAME \
$IMAGE_NAME \
python3 client/entrypoint init_seed seed.npz
