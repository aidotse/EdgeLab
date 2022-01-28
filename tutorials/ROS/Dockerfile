FROM osrf/ros:noetic-desktop-full

RUN apt-get update
RUN apt-get install git -y
RUN apt-get install pip -y

COPY requirements.txt requirements.txt 

RUN pip install -r requirements.txt

RUN /bin/bash -c '. /opt/ros/noetic/setup.bash &&\
    mkdir -p /home/ai_sweden_ws/src &&\
    cd /home/ai_sweden_ws &&\
    catkin_make'

RUN ["/bin/bash", "-c", ". /home/ai_sweden_ws/devel/setup.bash"]
WORKDIR /home/ai_sweden_ws/src
COPY ROS_DecentralizedAI ROS_DecentralizedAI

RUN /bin/bash -c '. /opt/ros/noetic/setup.bash &&\
    cd /home/ai_sweden_ws &&\
    catkin_make'

WORKDIR /home/ai_sweden_ws

COPY run_server.sh run_server.sh
COPY run_client.sh run_client.sh
COPY run_gossip_client.sh run_gossip_client.sh

# launch ros package
CMD /bin/bash