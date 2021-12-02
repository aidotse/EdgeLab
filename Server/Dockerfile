FROM ubuntu:20.04

RUN apt-get update
RUN apt-get install -y software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt-get install -y python3.7
RUN apt-get install -y python3-pip

RUN mkdir /app
WORKDIR /app

RUN pip3 install syft==0.2.5 -f https://download.pytorch.org/whl/torch_stable.html

COPY /app .

CMD /bin/bash