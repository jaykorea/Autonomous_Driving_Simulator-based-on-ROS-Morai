#!/usr/bin/env python
  
import rospy
import cv2
import numpy as np
from sensor_msgs.msg import Image, CompressedImage, LaserScan, PointCloud
from cv_bridge import CvBridge, CvBridgeError
from std_msgs.msg import Float64, Bool
from math import cos,sin,pi
import time

    
class Detector():
    def __init__(self):
        rospy.init_node('Stopline_Detector', anonymous=True)
        
        self.image_sub = rospy.Subscriber("/image_jpeg/compressed", CompressedImage, self.callback)
        self.stopline_pub = rospy.Publisher("/stop_line/info", Bool, queue_size=1)

        self.bridge = CvBridge()
        self.stopline_detection_flag = Bool()
        
        rospy.spin()
            
    def callback(self, data):
        
        np_arr = np.fromstring(data.data, np.uint8)
        self.img_bgr = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
        
        self.stopline_detection_flag = self.detect_stoplineB(self.img_bgr)
        self.stopline_pub.publish(self.stopline_detection_flag)

        # try:
        #     self.camera_image = self.bridge.cv2_to_imgmsg(img_bgr, "bgr8")
        #     self.camera_image2 = self.bridge.cv2_to_imgmsg(data, "bgr8")
        # except CvBridgeError,e:
        #     print(e)

        # self.execute(self.img_bgr)
        # cv2.imshow("Image window", img_bgr)
        # cv2.waitKey(1)
        
    def rgbscale(self,img):
        return cv2.cvtColor(img, cv2.COLOR_RGBA2RGB)

    def region_of_interest(self, img, vertices, color3=(255, 255, 255), color1=255):
        mask = np.zeros_like(img)
        if len(img.shape) > 2:
            color = color3
        else:
            color = color1
        cv2.fillPoly(mask, vertices, color)
        ROI_image = cv2.bitwise_and(img, mask)
        return ROI_image


    def detect_stopline(self, x):
        frame = x.copy()
        img = frame.copy()
        min_stopline_length = 300
        max_distance = 100

        # blur
        kernel_size = 5
        blur_frame = cv2.GaussianBlur(frame, (kernel_size, kernel_size), 0)

        # roi
        vertices = np.array([[
            (80, frame.shape[0]),
            (120, frame.shape[0] - 100),
            (frame.shape[1] - 120, frame.shape[0] - 12),
            (frame.shape[1] - 80, frame.shape[0])
        ]], dtype=np.int32)
    



        roi = self.region_of_interest(blur_frame, vertices)
        #     roi = blur_frame  # for test

        # yellow RGB
        lower_yellow, upper_yellow = (195, 195, 70), (255, 255, 180)
        img_mask = cv2.inRange(roi, lower_yellow, upper_yellow)
        img_result = cv2.bitwise_and(roi, roi, mask=img_mask)

        # gray
        gray = cv2.cvtColor(img_result, cv2.COLOR_BGR2GRAY)

        # binary
        ret, dest = cv2.threshold(gray, 160, 255, cv2.THRESH_BINARY)

        # canny
        low_threshold, high_threshold = 70, 210
        edge_img = cv2.Canny(np.uint8(dest), low_threshold, high_threshold)

        # find contours, opencv4
        contours, hierarchy = cv2.findContours(edge_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # find contours, opencv3
        #_, contours, hierarchy = cv2.findContours(edge_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        if contours:
            stopline_info = [0, 0, 0, 0]
            for contour in contours:
                epsilon = 0.01 * cv2.arcLength(contour, True)
                approx = cv2.approxPolyDP(contour, epsilon, True)
                # result = cv2.drawContours(frame, [approx], 0, (0,255,0), 4)
                x, y, w, h = cv2.boundingRect(contour)
                if stopline_info[2] < w:
                    stopline_info = [x, y, w, h]
                # cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 3)
                rect = cv2.minAreaRect(approx)
                box = cv2.boxPoints(rect)
                box = np.int0(box)
                result = cv2.drawContours(frame, [box], 0, (0, 255, 0), 3)

            cx, cy = stopline_info[0] + 0.5 * stopline_info[2], stopline_info[1] + 0.5 * stopline_info[3]
            center = np.array([cx, cy])
            stopline_length = stopline_info[2]
            bot_point = np.array([frame.shape[1] // 2, frame.shape[0]])
            distance = np.sqrt(np.sum(np.square(center - bot_point)))

            # OUTPUT
            #print('length : {},  distance : {}'.format(stopline_length, distance))

            if stopline_length > min_stopline_length and distance < max_distance:
                #cv2.imshow('stopline', result)
                #cv2.waitKey(1)
                print('STOPLINE Detected')
                return True

        #cv2.imshow('stopline', img)
        #cv2.waitKey(1)
        #print('No STOPLINE.')
        return False


    def detect_stoplineB(self,x):
        frame = x.copy()
        img = frame.copy()
        min_stopline_length = 330 #defualt 250
        #max_stopline_length = 250
        max_distance = 120 #defualt 70
        min_distance = 80

        # gray
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # blur
        kernel_size = 5
        blur_frame = cv2.GaussianBlur(gray, (kernel_size, kernel_size), 0)

        # roi
        vertices = np.array([[
            (80, frame.shape[0]),
            (120, frame.shape[0] - 120),
            (frame.shape[1] - 80, frame.shape[0] - 120),
            (frame.shape[1] - 120, frame.shape[0])
        ]], dtype=np.int32)

        roi = self.region_of_interest(blur_frame, vertices)

        # filter
        img_mask = cv2.inRange(roi, 100, 400) ## default 160, 220
        img_result = cv2.bitwise_and(roi, roi, mask=img_mask)

        # cv2.imshow('bin', img_result)

        # binary
        ret, dest = cv2.threshold(img_result, 160, 255, cv2.THRESH_BINARY)

        # canny
        low_threshold, high_threshold = 70, 210
        edge_img = cv2.Canny(np.uint8(dest), low_threshold, high_threshold)

        # find contours, opencv4
        contours, hierarchy = cv2.findContours(edge_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # find contours, opencv3
        #_, contours, hierarchy = cv2.findContours(edge_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        if contours:
            stopline_info = [0, 0, 0, 0]
            for contour in contours:
                epsilon = 0.01 * cv2.arcLength(contour, True)
                approx = cv2.approxPolyDP(contour, epsilon, True)
                # result = cv2.drawContours(frame, [approx], 0, (0,255,0), 4)
                x, y, w, h = cv2.boundingRect(contour)
                if stopline_info[2] < w:
                    stopline_info = [x, y, w, h]
                # cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 3)
                rect = cv2.minAreaRect(approx)
                box = cv2.boxPoints(rect)
                box = np.int0(box)
                result = cv2.drawContours(frame, [box], 0, (0, 255, 0), 3)

            cx, cy = stopline_info[0] + 0.5 * stopline_info[2], stopline_info[1] + 0.5 * stopline_info[3]
            center = np.array([cx, cy])
            stopline_length = stopline_info[2]
            bot_point = np.array([frame.shape[1] // 2, frame.shape[0]])
            distance = np.sqrt(np.sum(np.square(center - bot_point)))

            # OUTPUT
            #print('length : {},  distance : {}'.format(stopline_length, distance))
            # red_color = (0,0,255)
            # cv2.rectangle(img, vertices, red_color, 3)
            if stopline_length > min_stopline_length and min_distance <distance < max_distance:
            #if min_stopline_length <= stopline_length <= max_stopline_length and min_distance < distance < max_distance:
                cv2.imshow('stopline', result)
                cv2.waitKey(1)
                print('STOPLINE Detected')
                # self.stopline_detection_flag = True
                return True

        cv2.imshow('stopline', img)
        cv2.waitKey(1)
        # print('No STOPLINE.')
        return False
 
if __name__ == '__main__':       
    try:
        sld=Detector() 
    except rospy.ROSInterruptException:
        pass
