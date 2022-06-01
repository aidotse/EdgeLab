#!/bin/bash
set -e

rm -rf venv/
python3 -m venv venv
venv/bin/pip3 install --upgrade pip
venv/bin/pip3 install -r requirements.txt 
