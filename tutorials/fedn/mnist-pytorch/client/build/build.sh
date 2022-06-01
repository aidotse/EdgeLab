#!/bin/bash

set -e

IMAGE_NAME="fedn-mnist-pytorch"

docker build -f Dockerfile -t $IMAGE_NAME .
