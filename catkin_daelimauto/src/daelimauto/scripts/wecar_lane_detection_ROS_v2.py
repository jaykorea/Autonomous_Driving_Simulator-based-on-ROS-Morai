#!/usr/bin/env python
from __future__ import print_function
import time
import roslib
import sys
import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import CompressedImage
from cv_bridge import CvBridgeError
from std_msgs.msg import Float64

from image_data_v2 import *

class image_converter:

  def __init__(self):
    rospy.init_node('image_converter', anonymous=True)
    
    # self.image_pub = rospy.Publisher("image_topic_2",Image)
    self.rate = rospy.Rate(30)
    self.timer_to_sending_data = 0
    

    self.speed = rospy.Publisher('/commands/motor/speed', Float64, queue_size=1) 
    self.position = rospy.Publisher('/commands/servo/position', Float64, queue_size=1) 

    self.speed_value = 0
    self.position_value = 0.5
    #self.speed.publish(0.0)
    #self.position.publish(self.position_value)
    self.image_sub = rospy.Subscriber("/image_jpeg/compressed", CompressedImage,self.callback)
    rospy.on_shutdown(self.shutdown)


  def callback(self, data):
    try:
      np_arr = np.fromstring(data.data, np.uint8)
      cv_image = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
    except CvBridgeError as e:
      print(e)
    
  #  cv2.imshow("Image window", cv_image)
   # cv2.waitKey(1)

    #self.speed.publish(self.speed_value)
#    self.position.publish(self.position_value)
    # if self.timer_to_sending_data %1 == 0:

    angle = line_detection(cv_image)
    print(angle)
    
    if angle > 0:   
       self.position_value = 0.0
       #self.speed_value = 2000
       self.position.publish(self.position_value)
       #self.speed.publish(self.speed_value)
    elif angle < 0:
       self.position_value = 1.0
       #self.speed_value = 2000
       self.position.publish(self.position_value)
       #self.speed.publish(self.speed_value)
    else:
       self.position_value = 0.5
       #self.speed_value = 2400
       #self.position.publish(self.position_value)
       #self.speed.publish(self.speed_value)
       time.sleep(0.1)
     
    self.timer_to_sending_data = 0


    self.timer_to_sending_data += 1
    
  def shutdown(self):
    self.speed.publish(0)
    self.position.publish(0.5)
    self.rate.sleep()
    
if __name__ == '__main__':
    ic = image_converter()
    time.sleep(1)
    rate = rospy.Rate(30)
            
    while not rospy.is_shutdown():
        ic
        rate.sleep()

    ic.shutdown()

