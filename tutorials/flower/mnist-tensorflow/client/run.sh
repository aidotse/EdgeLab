#!/bin/bash

IMAGE_NAME="client-docker"

ROOT_DIR=$PWD

docker run -it --rm --runtime nvidia -e SERVER_IP=$1 \
-v $ROOT_DIR:/app \
$IMAGE_NAME
