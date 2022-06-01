#!/bin/bash

set -e

IMAGE_NAME="fedn-mnist-pytorch"

ROOT_DIR=$PWD

docker run --shm-size=1024m -it --rm --runtime nvidia \
--add-host=combiner:172.25.8.253 \
-v $ROOT_DIR/data:/app/data:ro \
-v $ROOT_DIR/client.yaml:/app/client.yaml:ro \
$IMAGE_NAME \
/bin/bash -c "fedn run client -in client.yaml"
