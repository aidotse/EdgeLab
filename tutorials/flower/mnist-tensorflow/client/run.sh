#!/bin/bash

IMAGE_NAME="client-docker"

ROOT_DIR=$PWD

docker run -it --rm --runtime nvidia -e SERVER_ID=172.25.17.170:8080 \
-v $ROOT_DIR:/app \
$IMAGE_NAME \
bash
