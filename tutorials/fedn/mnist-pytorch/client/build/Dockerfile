
#FROM nvcr.io/nvidia/pytorch:21.03-py3
FROM nvcr.io/nvidia/l4t-pytorch:r32.6.1-pth1.9-py3

ENV DEBIAN_FRONTEND="noninteractive"

# Install python dependencies
COPY requirements.txt .
RUN python3 -m pip install --upgrade pip
RUN pip install --no-cache -r requirements.txt

WORKDIR /app