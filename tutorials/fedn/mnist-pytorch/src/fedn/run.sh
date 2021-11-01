#!/bin/bash

IMAGE_NAME="mnist-pytorch"

ROOT_DIR=$PWD

docker run --shm-size=1024m -it --rm --runtime nvidia \
--add-host=combiner:172.25.17.69 \
-v $ROOT_DIR/data:/app/data:ro \
-v $ROOT_DIR/client.yaml:/app/client.yaml \
-v $ROOT_DIR/settings.yaml:/app/settings.yaml \
$IMAGE_NAME \
/bin/bash -c "fedn run client -in client.yaml"
