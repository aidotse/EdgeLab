#!/bin/bash

IMAGE_NAME="client-docker"

docker build -f Dockerfile -t $IMAGE_NAME .
