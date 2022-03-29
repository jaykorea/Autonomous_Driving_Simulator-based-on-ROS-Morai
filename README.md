# autonomous_driving_simulator-based-on-ROS-Morai

Dev env
OS : Ubuntu18.04
MiddleWare : Ros melodic (desktop-full ver)
python 2.7.17 (기본내장)
opencv 3.4.5 || 4.3 (별도로 빌드후 설치)
darknet ros with cuda11 ( cuda 10 버전에서도 사용가능  - generic compute 86 이하 버전세팅)

1. darknet_ros 설치

$ cd
$ mkdir -p ~/catkin_darknet/src
$ cd catkin_darknet/src
$ catkin_init_workspace
$ cd ..
$ catkin_make

darknet_ros 소스파일 src 폴더로 이동후

$ catkin_make

→ opencv , cvbridge 에러 관련 : : 95mkr.tistory.com/entry/ROS6

bashrc 또는 zshrc 에 setup.bash(zsh) source 하기

2. datkin_daelimauto 설치

$ cd
$ mkdir -p ~/catkin_daelimauto/src
$ cd catkin_daelimauto/src
$ catkin_init_workspace
$ cd ..
$ catkin_make

3. code 실행
1. roslaunch rosbridge_server rosbridge_websocket.launch

2. roslaunch daelim_auto daelim_main.launch 

“”” depthcamera Node, Hough Node, stoplineDetector Node, lidar for FOVNode, Darknet-Ros Node 가 모두 실행됩니다.“””

![image](https://user-images.githubusercontent.com/95605860/160551629-50db0005-a50c-4a95-b56e-1214ab26cc2e.png)
