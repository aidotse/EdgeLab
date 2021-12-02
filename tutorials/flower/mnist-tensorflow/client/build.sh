#!/bin/bash

IMAGE_NAME="flower_tensor_client"

docker build -f Dockerfile -t $IMAGE_NAME .
