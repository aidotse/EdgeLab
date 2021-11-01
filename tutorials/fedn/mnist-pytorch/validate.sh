#!/bin/bash

IMAGE_NAME="edgelab_mnist_pytorch"

ROOT_DIR=$PWD
CLIENT_FEDN_DIR=$ROOT_DIR/src/fedn
CLIENT_SRC_DIR=$ROOT_DIR/src/client
DATA_DIR=$ROOT_DIR/src/fedn/data
PACKAGE_DIR=$ROOT_DIR/package
TMP_DIR=/tmp

username=$(whoami)

docker run --gpus all -it --rm --ipc=host \
-v $CLIENT_SRC_DIR:/home/$username \
-v $DATA_DIR:/home/data \
-v $PACKAGE_DIR:/home/package \
-v $CLIENT_FEDN_DIR/settings.yaml:/home/settings.yaml \
-v $TMP_DIR:/home/tmp \
$IMAGE_NAME \
python3 validate.py ../package/initial_model.npz ../tmp/report.json
