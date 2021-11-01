#!/bin/bash

IMAGE_NAME="edgelab_mnist_pytorch"

ROOT_DIR=$PWD

username=$(whoami)

docker run --gpus all -it --rm --ipc=host \
-v $ROOT_DIR:/home/$username  \
$IMAGE_NAME \
python3 init_model.py
