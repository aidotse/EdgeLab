#!/bin/bash

IMAGE_NAME="flower_pytotch_client"

docker build -f Dockerfile -t $IMAGE_NAME .
