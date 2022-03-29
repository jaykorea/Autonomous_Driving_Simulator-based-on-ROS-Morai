#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys,os,time
from xmlrpc.client import FastMarshaller
import rospy
import rospkg
import numpy as np
from nav_msgs.msg import Path,Odometry
from std_msgs.msg import Float64,Bool,Int32,Int16,Float32MultiArray,Int8
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import PoseStamped,Point
from morai_msgs.msg import EgoVehicleStatus,GPSMessage,ObjectStatusList,CtrlCmd,GetTrafficLightStatus,SetTrafficLight
from darknet_ros_msgs.msg import BoundingBoxes,BoundingBox,ObjectCount
from lib.utils import pathReader, findLocalPath,purePursuit,cruiseControl,vaildObject,pidController,velocityPlanning,latticePlanner
import tf
from math import cos,sin,sqrt,pow,atan2,pi
from forward_object_detector import ForwardObjectDetector

cur_path =0 

class wecar_planner():
    def __init__(self):
        rospy.init_node('daelim_auto_planner', anonymous=True)

        arg = rospy.myargv(argv=sys.argv)

        #publisher
        global_path_pub= rospy.Publisher('/global_path',Path, queue_size=1) ## global_path publisher
        local_path_pub= rospy.Publisher('/local_path',Path, queue_size=1) ## local_path publisher
        self.motor_pub = rospy.Publisher('/commands/motor/speed',Float64, queue_size=1)
        self.servo_pub = rospy.Publisher('/commands/servo/position',Float64, queue_size=1)

        ########################  lattice  ########################
        for i in range(1,8):            
            globals()['lattice_path_{}_pub'.format(i)]=rospy.Publisher('lattice_path_{}'.format(i),Path,queue_size=1)  
        ########################  lattice  ########################
        
        #subscriber
        rospy.Subscriber("/Ego_topic", EgoVehicleStatus, self.statusCB) ## Vehicl Status Subscriber 
        rospy.Subscriber("/darknet_ros/bounding_boxes", BoundingBoxes, self.objectDataCB) ## Object information Subscriber
        rospy.Subscriber("/darknet_ros/found_object", ObjectCount, self.objectInfoCB)
        rospy.Subscriber("/gps", GPSMessage, self.gpsCB)
        rospy.Subscriber("/stop_line/info", Bool, self.stoplineinfoCB)
        rospy.Subscriber("/GetTrafficLightStatus", GetTrafficLightStatus, self.trafficlightinfoCB)
        rospy.Subscriber("/lidarfov", LaserScan, self.lidarfovdataCB)    
        #def
        self.is_status=False 
        self.is_obj=False 
        self.objectCnt = 0
        self.object_info=[]
        self.print_info_flag = False
        self.steering_angle_to_servo_offset=0.5304 ## servo moter offset
        self.rpm_gain = 4616 #4616
        self.motor_msg=Float64()
        self.servo_msg=Float64()
        self.mission = 0
        self.vgla = 0.0
        self.vglo = 0.0
        self.vgeo = 0.0
        self.vgno = 0.0
        self.mission0_flag = False
        self.mission1_flag = False
        self.mission2_flag = False
        self.mission3_flag = False
        self.stop_line_flag = Bool()
        self.stop_line_counter = 0
        self.trafficlightinfo = GetTrafficLightStatus()
        self.objbox = BoundingBox()
        self.m_pub_threshold = 0.4
        self.distance_flag = False
        self.distance_flag2 = False
        self.lflag = bool
        self.lidardata =[]
        self.selected_lane =-1
        global cur_path
        

        #class
        path_reader=pathReader('daelim_auto') 
        pure_pursuit=purePursuit()
        self.cc=cruiseControl(0.5,1) 
        self.vo=vaildObject() 
        pid=pidController() 
        
        vel_planner=velocityPlanning(1,0.15) 
       
        #time var
        count=0
        rate = rospy.Rate(60) # defualt 30hz

        lattice_current_lane=3
        # fod = ForwardObjectDetector()

        while not rospy.is_shutdown():
            print(self.is_status , self.is_obj)
            # self.object_info = fod.detect_object(self.status_msg)
            
            if self.mission0_flag != True:
                print("mission start")
                self.mission = 0
                      
            elif  (37.6121902410 <= self.vgla <= 37.6121904947) and ( 126.994007823 <= self.vglo <= 126.994034096) and (self.mission1_flag != True):
                print("mission 1 activated")
                self.mission = 1
                self.servo_pub.publish(0)
                self.motor_pub.publish(0.5) 
            elif (37.6122000738 <= self.vgla <= 37.6122008869) and ( 126.994060005 <= self.vglo <= 126.994085439) and (self.mission2_flag != True):
                print("mission 2 activated")
                self.mission = 2
                self.servo_pub.publish(0)
                self.motor_pub.publish(0.5)
            elif (37.6121268793 <= self.vgla <= 37.6121415540) and ( 126.993966184 <= self.vglo <= 126.993972195) and (self.mission3_flag != True): 
                self.mission = 3
                self.servo_pub.publish(0)
                self.motor_pub.publish(0.5)
                
            #read path
            if self.mission == 0:
                self.mission0_flag = True
                self.mission = 5
                self.global_path=path_reader.read_txt('path07'+".txt") 
                vel_profile=vel_planner.curveBasedVelocity(self.global_path,30)
                cur_path = 1
                self.delay(0.1)
                
                
            elif self.mission == 1:
                self.mission1_flag = True
                self.mission = 5
                self.global_path=path_reader.read_txt('path08'+".txt") 
                vel_profile=vel_planner.curveBasedVelocity(self.global_path,30)
                cur_path = 2
                self.delay(0.1)

                
            elif self.mission == 2:
                self.mission2_flag = True
                self.mission = 5
                self.global_path=path_reader.read_txt('path09'+".txt")
                vel_profile=vel_planner.curveBasedVelocity(self.global_path,30)
                cur_path = 3
                self.delay(0.1)

            elif self.mission == 3:
                self.mission3_flag = True
                self.mission = 5
                self.global_path=path_reader.read_txt('path10'+".txt")
                vel_profile=vel_planner.curveBasedVelocity(self.global_path,30)
                cur_path = 4
                self.delay(0.1)
                
            if self.distance_flag == True:
                self.motor_pub.publish(0.0)
                self.servo_pub.publish(0.5)
                time.sleep(0.2)
                self.distance_flag=False
            
            if ((self.distance_flag2 == True) and (self.mission2_flag == True or self.mission3_flag == True)):
                self.distance_flag2 = False
                self.servo_pub.publish(1.0)
                self.motor_pub.publish(115) # 120 , 0.7
                self.servo_pub.publish(1.0)
                time.sleep(0.5)
                
            if self.stop_line_flag == True and self.stop_line_counter==0:
                self.motor_pub.publish(0.0)
                self.servo_pub.publish(0.5)
                self.stop_line_counter +=1
                #print(self.stop_line_counter)
                time.sleep(5)
                
            if ( (37.6121276278 <= self.vgla <= 37.612134285) and (126.994064639 <= self.vglo <= 126.994065473) ):
                print("mission 1_trafficlight activated")
                while (self.trafficlightinfo.trafficLightStatus != 33):
                    self.servo_pub.publish(0)
                    self.motor_pub.publish(0.5)
                    time.sleep(1)
                                            
            if ( (37.6121684099 <= self.vgla <= 37.6121740608) and ( 126.994051669 <= self.vglo <= 126.994052128) ): 
                print("mission 2_trafficlight activated")
                
                while (self.trafficlightinfo.trafficLightStatus != 33):
                    self.servo_pub.publish(0)
                    self.motor_pub.publish(0.5)
                    time.sleep(1)
                
                        
            if self.is_status==True and self.is_obj==True:

                local_path,self.current_waypoint=findLocalPath(self.global_path, self.status_msg) 

                self.vo.get_object(self.objectCnt,self.object_info[0],self.object_info[1],self.object_info[2],self.object_info[3])
                global_obj,local_obj=self.vo.calc_vaild_obj([self.status_msg.position.x,self.status_msg.position.y,(self.status_msg.heading)/180*pi])

                ########################  lattice  ########################
                vehicle_status=[self.status_msg.position.x,self.status_msg.position.y,(self.status_msg.heading)/180*pi,self.status_msg.velocity.x/3.6]
                lattice_path,self.selected_lane=latticePlanner(local_path,global_obj,vehicle_status,lattice_current_lane)
                lattice_current_lane=self.selected_lane
                
                # for i in range(180):
                #     if 0 < self.lidardata[i] <= 0.8:
                #         self.lflag = True
                #         print("lflag triggered!!!")
                    
                # if (self.lflag == True and (cur_path ==3 or cur_path ==4)):
                #     self.lflag = False
                #     print("Lane Changed!!!")
                #     self.selected_lane = self.selected_lane+1
                                
                if self.selected_lane != -1: 
                    local_path=lattice_path[self.selected_lane]                
                
                if len(lattice_path)==7:                    
                    for i in range(1,8):
                        globals()['lattice_path_{}_pub'.format(i)].publish(lattice_path[i-1])
                ########################  lattice  ########################
                self.cc.checkObject(local_path,global_obj,local_obj)

                
                pure_pursuit.getPath(local_path)
                pure_pursuit.getEgoStatus(self.status_msg)

                self.steering=pure_pursuit.steering_angle()
                
                self.cc_vel = self.cc.acc(local_obj,self.status_msg.velocity.x,vel_profile[self.current_waypoint],self.status_msg)

                self.servo_msg = self.steering*0.021 + self.steering_angle_to_servo_offset
                self.motor_msg = self.cc_vel *self.rpm_gain /3.6
                
    
                local_path_pub.publish(local_path)
                   
                self.servo_pub.publish(self.servo_msg)
                self.motor_pub.publish(self.motor_msg)
                #self.print_info()
            
            if count==30 : 
                global_path_pub.publish(self.global_path)
                count=0
            count+=1

            
            rate.sleep()


    def print_info(self):

        os.system('clear')
        print('--------------------status-------------------------')
        print('position :{0} ,{1}, {2}'.format(self.status_msg.position.x,self.status_msg.position.y,self.status_msg.position.z))
        print('velocity :{} km/h'.format(self.status_msg.velocity.x))
        print('heading :{} deg'.format(self.status_msg.heading))

        print('--------------------object-------------------------')
        print('object num :{}'.format(self.objectCnt))
        for i in range(0,self.objectCnt) :
            print('{0} : type = {1}, x = {2}, y = {3}, z = {4} '.format(i,self.object_info[0][i],self.object_info[1][i],self.object_info[2][i],self.object_info[3][i]))

        print('--------------------controller-------------------------')
        print('target vel_planning :{} km/h'.format(self.cc_vel))
        print('target steering_angle :{} deg'.format(self.steering))

        print('--------------------localization-------------------------')
        print('all waypoint size: {} '.format(len(self.global_path.poses)))
        print('current waypoint : {} '.format(self.current_waypoint))
        
        #self.print_info_flag = False


    def statusCB(self,data): ## Vehicle Status Subscriber 
        self.status_msg=data
        br = tf.TransformBroadcaster()
        br.sendTransform((self.status_msg.position.x, self.status_msg.position.y, self.status_msg.position.z),
                        tf.transformations.quaternion_from_euler(0, 0, (self.status_msg.heading)/180*pi),
                        rospy.Time.now(),
                        "gps",
                        "map")
        self.is_status=True
                    
        # print(self.status_msg.yaw)
    # def objectCntCB(self,data):
    #     self.objectCnt = data.count

    def objectInfoCB(self,data): ## Object information Subscriber
        #object_boxes = data.bounding_boxes
        self.objectCnt = 0
        object_type=[]
        object_pose_x=[]
        object_pose_y=[]
        object_velocity=[]
        # for num in range(data.num_of_npcs) :
        #     object_type.append(data.npc_list[num].type)
        #     object_pose_x.append(data.npc_list[num].position.x)
        #     object_pose_y.append(data.npc_list[num].position.y)
        #     object_velocity.append(data.npc_list[num].velocity.x)
        # if self.objectCnt != 0 :
        #     for i in range(0, len(object_boxes)) :
        #         if object_boxes[i].Class == 'person':
        #             object_type.append(object_boxes[i].id)
        #             object_pose_x.append(((object_boxes[i].xmax+object_boxes[i].xmin)/2))
        #             object_pose_y.append(((object_boxes[i].ymax+object_boxes[i].ymin)/2))
        #             object_velocity.append(0)
        #         else:
        #             object_type.append(object_boxes[i].id)
        #             object_pose_x.append(((object_boxes[i].xmax+object_boxes[i].xmin)/2))
        #             object_pose_y.append(((object_boxes[i].ymax+object_boxes[i].ymin)/2))
        #             object_velocity.append(0)
                    
        #     self.object_info=[object_type,object_pose_x,object_pose_y,object_velocity]
        # else: 
        self.object_info=['None',0,0,0]
           
        self.is_obj=True
        # if self.objectCnt == len(self.object_info):
        #     self.print_info_flag = True
        # else :
        #     self.print_info_flag = False
    
    def gpsCB(self,data):
        self.vgla = data.latitude
        self.vglo = data.longitude
        self.vgeo = data.eastOffset
        self.vgno = data.northOffset
        # print("latitude {}".format(data.latitude))
        # print("longitude {}".format(data.longitude))
        # print("eastOffset {}".format(data.eastOffset))
        # print("northOffset {}".format(data.northOffset))
        
    def objectDataCB(self,data):
        bbox = data.bounding_boxes
        objbox = BoundingBox()
        if len(bbox) != 0:
            for i, bb in enumerate(bbox):
                if ( bbox[i].Class == 'person' and bbox[i].probability >= self.m_pub_threshold ) and (bbox[i].Class == 'car' and bbox[i].probability >= self.m_pub_threshold ):
                    objbox = bbox[i]
            self.objbox = objbox
    
    def stoplineinfoCB(self,data):
        self.stop_line_flag = data.data
        
    def trafficlightinfoCB(self,data):
        self.trafficlightinfo.trafficLightIndex = data.trafficLightIndex
        self.trafficlightinfo.trafficLightStatus = data.trafficLightStatus
        # print(self.trafficlightinfo.trafficLightIndex)
        # print(self.trafficlightinfo_status)
        
    def lidarfovdataCB(self,data):
       
        for i in range(90):
            # self.lidardata.append(data.ranges[i])
            # print(self.lidardata)
            if 0.0 < data.ranges[i] <= 0.7:
                #print("Distance warning!!")
                self.distance_flag = True
            if 0.0 < data.ranges[i] <= 1.05:
                #print("Object warning!!")
                self.distance_flag2 = True
            
        
    def shutdown(self):
        self.servo_pub.publish(0.5)
        self.motor_pub.publish(0)
        print("Program Finished")
        
    def delay(self, sec):
        time.sleep(sec)
    
if __name__ == '__main__':
    try:
        kcity_pathtracking=wecar_planner()
    except rospy.ROSInterruptException:
        pass
    kcity_pathtracking.shutdown()
