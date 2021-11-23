FROM nvcr.io/nvidia/l4t-pytorch:r32.6.1-pth1.9-py3

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

WORKDIR /client

COPY requirements.txt requirements.txt

RUN python3 -m pip install --upgrade pip

RUN pip3 install -r requirements.txt

COPY . .

WORKDIR /app

CMD [ "python3", "client.py"]
