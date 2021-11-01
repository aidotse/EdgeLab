#!/bin/bash

IMAGE_NAME="edgelab_mnist_pytorch"

docker build \
--build-arg u_id=$(id -u) \
--build-arg g_id=$(id -g) \
--build-arg username=$(id -gn $USER)  \
-f Dockerfile -t $IMAGE_NAME .
