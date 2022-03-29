#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy
import math
from sensor_msgs.msg import LaserScan
from math import *
import numpy as np
import copy

f_ranges_filter = []
f_intensities_filter = []
r_ranges_filter = []
r_intensities_filter = []


class lidarFilter :
#copy the range and intensities of "/scan" topic to "f_ranges_filter" and "f_intensities_filter" 
#you need to convert them to "list" as "data.ranges" and "data.intensities" are "tuple"
    def __init__(self):
        #define a new topic called "frontScan" to store all laser scanner data
        rospy.init_node('laser_scan_filter')
        rospy.Subscriber("/lidar2D", LaserScan, self.callback_scan) 
        
        self.fscan_pub = rospy.Publisher('/front_scan', LaserScan, queue_size=50)
        self.rscan_pub = rospy.Publisher('/rear_scan', LaserScan, queue_size=50)

        #it is based on the type of laser scanner (length of data.ranges)
        self.num_readings = 360
        self.laser_frequency = 60
        self.count = 0
        
        rospy.spin()
    
    
    def callback_scan(self,data):
        current_time = rospy.Time.now()
        global f_ranges_filter, f_intensities_filter, r_ranges_filter, r_intensities_filter

        len(data.ranges) #360
        len(data.intensities) #360

        f_ranges_filter = copy.copy(data.ranges)
        f_intensities_filter = copy.copy(data.intensities)
        r_ranges_filter = copy.copy(data.ranges)
        r_intensities_filter = copy.copy(data.intensities)        
        

        #convert them to list
        f_ranges_filter = list(f_ranges_filter)
        f_intensities_filter = list(f_intensities_filter)
        r_ranges_filter = list(r_ranges_filter)
        r_intensities_filter = list(r_intensities_filter)        

         #filtering those angles that I do not want them (based on the question)
        for x in range(180, 359):
            f_ranges_filter[x] = 0
            #f_intensities_filter[x] = 0
            
        for i in range(366):   
            f_ranges_filter.append(10.0)
            
        for y in range(0,179):
            r_ranges_filter[y] = 0
            #r_intensities_filter[y] = 0 
            
        for i in range(366):   
            r_ranges_filter.append(10.0)
        
        frontScan = LaserScan()
        rearScan = LaserScan()

        frontScan.header.stamp = current_time
        frontScan.header.frame_id = 'front_scanner'
        frontScan.angle_min = -2.35619449615 # start angle of the scan [rad]
        frontScan.angle_max = 2.09234976768  # end angle of the scan [rad]
        frontScan.angle_increment = 0.0174532923847 # angular distance between measurements [rad]
        frontScan.time_increment = 0.000125000005937 # time between measurements [seconds]
        frontScan.scan_time = 0.10000000149
        frontScan.range_min = 0.0 # minimum range value [m]
        frontScan.range_max = 10.0 # maximum range value [m]
        
        frontScan.ranges = []
        frontScan.intensities = []
        
        rearScan.header.stamp = current_time
        rearScan.header.frame_id = 'rear_scanner'
        rearScan.angle_min = -2.35619449615 # start angle of the scan [rad]
        rearScan.angle_max = 2.09234976768 # end angle of the scan [rad]
        rearScan.angle_increment = 0.00613592332229 # angular distance between measurements [rad]
        rearScan.time_increment = 9.76562732831e-05 # time between measurements [seconds]
        rearScan.scan_time = 0.10000000149
        rearScan.range_min = 0.019999999553 # minimum range value [m]
        rearScan.range_max = 10.0 # maximum range value [m]
        
        rearScan.ranges = []
        rearScan.intensities = []


        for i in range(0, self.num_readings-1):
            frontScan.ranges = copy.copy(f_ranges_filter)
            frontScan.intensities = copy.copy(f_intensities_filter)
            
        for b in range(0, self.num_readings-1):
            frontScan.ranges = copy.copy(f_ranges_filter)
            rearScan.ranges = copy.copy(r_intensities_filter)

        self.fscan_pub.publish(frontScan)
        self.rscan_pub.publish(rearScan)
        rospy.loginfo(frontScan)
        rospy.loginfo(rearScan)
        
            
            
if __name__ == '__main__' :
    try:
        a=lidarFilter()
    except rospy.ROSInterruptException:
        pass
    
    
