#!/bin/bash

IMAGE_NAME="mnist-pytorch"

docker build -f Dockerfile -t $IMAGE_NAME .
