# Decentralized AI

This repository is based of the repository: [Decentralized AI](https://github.com/aidotse/DecentralizedAI).  
So far, this repository contains the following sub-folders:

* _fed_lr_ros_: a testbed for traning TensorFlow models in *federated learning* settings using ROS.

* _dist_lr_ros_: a general testbed for traning TensorFlow models in *distributed learning* settings using ROS (Not yet implemented).

* _common_: common ROS mesages, utils, and packages used by both the *distributed learning* and the *federeated learning* testbed.

* _tf_privacy_: a rudimentary tutorial for using _differential privacy_ together with TensorFlow 2.x.

## Usage

The original ROS files have been modified to work on Nvidia AGX Xavier devices.

A tutorial for setting up a federated learning system using tensorflow in edgelab is located in the folder _fed_lr_ros_



## Questions?

__Q:__ What is _differential privacy_? \
__A:__ See the tutorial [__tf_privacy__](https://github.com/aidotse/DecentralizedAI/tree/main/tf_privacy).

__Q:__ What is _ROS_? \
__A:__ *“The Robot Operating System (ROS) is a flexible framework for writing robot software. It is a collection of tools, libraries, and conventions that aim to simplify the task of creating complex and robust robot behavior across a wide variety of robotic platforms.”* -- [ROS Webpage](https://www.ros.org/about-ros/)

