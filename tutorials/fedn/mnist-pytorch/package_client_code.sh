#!/bin/bash

mkdir package

FILE_NAME=client_code.tar.gz
#Add timestamp
#STEM_FILE_NAME=client_code
#CURRENT_TIME=$(date "+%Y%m%d%H%M%S")
#FILE_NAME=$STEM_FILE_NAME\_$CURRENT_TIME\.tar.gz

cd src

tar -czvf ../package/$FILE_NAME client

echo done