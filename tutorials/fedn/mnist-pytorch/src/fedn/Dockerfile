FROM nvcr.io/nvidia/l4t-pytorch:r32.6.1-pth1.9-py3

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

RUN python3 -m pip install --upgrade pip

#RUN pip install -e git://github.com/scaleoutsystems/fedn.git@v0.2.3#egg=fedn\&subdirectory=fedn
RUN pip install -e git://github.com/scaleoutsystems/fedn.git@v0.3.0#egg=fedn\&subdirectory=fedn

WORKDIR /app
