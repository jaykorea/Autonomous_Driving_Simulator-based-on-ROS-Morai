;; Auto-generated. Do not edit!


(when (boundp 'morai_msgs::RadarTracks)
  (if (not (find-package "MORAI_MSGS"))
    (make-package "MORAI_MSGS"))
  (shadow 'RadarTracks (find-package "MORAI_MSGS")))
(unless (find-package "MORAI_MSGS::RADARTRACKS")
  (make-package "MORAI_MSGS::RADARTRACKS"))

(in-package "ROS")
;;//! \htmlinclude RadarTracks.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass morai_msgs::RadarTracks
  :super ros::object
  :slots (_header _tracks ))

(defmethod morai_msgs::RadarTracks
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:tracks __tracks) (let (r) (dotimes (i 0) (push (instance morai_msgs::RadarTrack :init) r)) r))
    )
   (send-super :init)
   (setq _header __header)
   (setq _tracks __tracks)
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:tracks
   (&rest __tracks)
   (if (keywordp (car __tracks))
       (send* _tracks __tracks)
     (progn
       (if __tracks (setq _tracks (car __tracks)))
       _tracks)))
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; morai_msgs/RadarTrack[] _tracks
    (apply #'+ (send-all _tracks :serialization-length)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; morai_msgs/RadarTrack[] _tracks
     (write-long (length _tracks) s)
     (dolist (elem _tracks)
       (send elem :serialize s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; morai_msgs/RadarTrack[] _tracks
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _tracks (let (r) (dotimes (i n) (push (instance morai_msgs::RadarTrack :init) r)) r))
     (dolist (elem- _tracks)
     (send elem- :deserialize buf ptr-) (incf ptr- (send elem- :serialization-length))
     ))
   ;;
   self)
  )

(setf (get morai_msgs::RadarTracks :md5sum-) "e7a281654e489a7faa3eacc0f9a4cf33")
(setf (get morai_msgs::RadarTracks :datatype-) "morai_msgs/RadarTracks")
(setf (get morai_msgs::RadarTracks :definition-)
      "Header header

RadarTrack[] tracks

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id

================================================================================
MSG: morai_msgs/RadarTrack
# This message relates only to FMCW radar.  
# All variables below are relative to the radar's frame of reference.
# This message is not meant to be used alone but as part of a stamped or array message.

# Object classifications (Additional vendor-specific classifications are permitted starting from 32000 eg. Car)

int8 uuid

                                            # Note: The z component of these fields is ignored for 2D tracking.
geometry_msgs/Point position                # x, y, z coordinates of the centroid of the object being tracked.
geometry_msgs/Vector3 velocity              # The velocity of the object in each spatial dimension.
geometry_msgs/Vector3 acceleration          # The acceleration of the object in each spatial dimension.
geometry_msgs/Vector3 size                  # The object size as represented by the radar sensor eg. length, width, height OR the diameter of an ellipsoid in the x, y, z, dimensions
                                            # and is from the sensor frame's view.
uint16 classification                       # An optional classification of the object (see above)

float32[] position_covariance              # Upper-triangle covariance about the x, y, z axes
float32[] velocity_covariance              # Upper-triangle covariance about the x, y, z axes
float32[] acceleration_covariance          # Upper-triangle covariance about the x, y, z axes
float32[] size_covariance                  # Upper-triangle covariance about the x, y, z axes

float32 amplitude


================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: geometry_msgs/Vector3
# This represents a vector in free space. 
# It is only meant to represent a direction. Therefore, it does not
# make sense to apply a translation to it (e.g., when applying a 
# generic rigid transformation to a Vector3, tf2 will only apply the
# rotation). If you want your data to be translatable too, use the
# geometry_msgs/Point message instead.

float64 x
float64 y
float64 z
")



(provide :morai_msgs/RadarTracks "e7a281654e489a7faa3eacc0f9a4cf33")


