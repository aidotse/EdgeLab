#!/bin/bash

IMAGE_NAME="flower_pytotch_client"

ROOT_DIR=$PWD

docker run -it --rm --runtime nvidia -e SERVER_IP=$1 \
-v $ROOT_DIR:/app \
$IMAGE_NAME
