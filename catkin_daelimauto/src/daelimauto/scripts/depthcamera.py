#!/usr/bin/env python
  
import rospy
import cv2
import numpy as np
from sensor_msgs.msg import Image, CompressedImage, LaserScan, PointCloud
from cv_bridge import CvBridge, CvBridgeError
from std_msgs.msg import Float64
from math import cos,sin,pi
from geometry_msgs.msg import Point32


class IMGParser:
    def __init__(self):
        rospy.init_node('depthcamera', anonymous=True)
        
        self.bridge = CvBridge()
    
        self.image_sub = rospy.Subscriber("/image_jpeg/compressed", CompressedImage, self.callback)
        self.camera_pub = rospy.Publisher("/camera/image_jpeg", Image, queue_size=10)
        
        rospy.Subscriber("/lidar2D", LaserScan, self.laser_callback)
        self.pcd_pub = rospy.Publisher('laser2pcd',PointCloud, queue_size=1)
        self.lidar_pub_fov = rospy.Publisher('/lidarfov', LaserScan, queue_size=1)
                         
        rospy.spin()
        

    def callback(self, data):
        np_arr = np.fromstring(data.data, np.uint8)
        img_bgr = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
        
        try:
            camera_image = self.bridge.cv2_to_imgmsg(img_bgr, "rgb8")
            self.camera_pub.publish(camera_image)
        except CvBridgeError,e:
            print(e) # modified here
        cv2.imshow("Image window", img_bgr)
        cv2.waitKey(1)
    
    
    def laser_callback(self,msg):
        pcd=PointCloud()
        distance = LaserScan()
        pcd.header.frame_id=msg.header.frame_id
        distance.header.frame_id=msg.header.frame_id
        
        angle=0

        for r in msg.ranges :

            tmp_point=Point32()
            tmp_point.x=r*cos(angle)
            tmp_point.y=r*sin(angle)
            #print(angle,tmp_point.x,tmp_point.y)
            angle=angle+(1.0/180*pi)
            if r<12  :
                pcd.points.append(tmp_point)
                
        for i in range(135, 225):
            distance.ranges.append(msg.ranges[i])
                
        self.pcd_pub.publish(pcd)
        self.lidar_pub_fov.publish(distance)    

if __name__ == '__main__':
    try:
        image_parser = IMGParser()
    except rospy.ROSInterruptException:
        pass
