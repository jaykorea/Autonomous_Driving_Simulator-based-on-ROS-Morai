#! /usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Bool
import math

class ObjectDetector:
    def __init__(self):
        self.DISTANCE_TH = 0.8
        rospy.init_node('object_detector', anonymous=False)
        self.sub_ls = rospy.Subscriber(
            '/lidar2D',
            LaserScan,
            callback=self.callback
        )
        self.pub_flag = rospy.Publisher(
            "/lidar_flag",
            Bool,
            queue_size=3
        )

    def callback(self, _ls):
        cnt = 0
        for i in range(len(_ls.ranges)):
            angle = _ls.angle_min + i * _ls.angle_increment
            # print(angle)
            if -20.0 * math.pi / 180.0 <= angle <= 20.0 * math.pi / 180.0:
                if _ls.ranges[i] < self.DISTANCE_TH:
                    cnt += 1



        # for distance in _ls.ranges[170:190]:
        #     if distance > 0 and distance < 0.9:
        #         self.pub_flag.publish(False)
                # return
        print(cnt)
        if cnt >= 5:
            self.pub_flag.publish(False)
        else:
            self.pub_flag.publish(True)
        # self.pub_flag.publish(True)

def run():
    od = ObjectDetector()
    rospy.spin()

if __name__ == "__main__":
    run()
