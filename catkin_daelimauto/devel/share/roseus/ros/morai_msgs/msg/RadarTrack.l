;; Auto-generated. Do not edit!


(when (boundp 'morai_msgs::RadarTrack)
  (if (not (find-package "MORAI_MSGS"))
    (make-package "MORAI_MSGS"))
  (shadow 'RadarTrack (find-package "MORAI_MSGS")))
(unless (find-package "MORAI_MSGS::RADARTRACK")
  (make-package "MORAI_MSGS::RADARTRACK"))

(in-package "ROS")
;;//! \htmlinclude RadarTrack.msg.html
(if (not (find-package "GEOMETRY_MSGS"))
  (ros::roseus-add-msgs "geometry_msgs"))


(defclass morai_msgs::RadarTrack
  :super ros::object
  :slots (_uuid _position _velocity _acceleration _size _classification _position_covariance _velocity_covariance _acceleration_covariance _size_covariance _amplitude ))

(defmethod morai_msgs::RadarTrack
  (:init
   (&key
    ((:uuid __uuid) 0)
    ((:position __position) (instance geometry_msgs::Point :init))
    ((:velocity __velocity) (instance geometry_msgs::Vector3 :init))
    ((:acceleration __acceleration) (instance geometry_msgs::Vector3 :init))
    ((:size __size) (instance geometry_msgs::Vector3 :init))
    ((:classification __classification) 0)
    ((:position_covariance __position_covariance) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:velocity_covariance __velocity_covariance) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:acceleration_covariance __acceleration_covariance) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:size_covariance __size_covariance) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:amplitude __amplitude) 0.0)
    )
   (send-super :init)
   (setq _uuid (round __uuid))
   (setq _position __position)
   (setq _velocity __velocity)
   (setq _acceleration __acceleration)
   (setq _size __size)
   (setq _classification (round __classification))
   (setq _position_covariance __position_covariance)
   (setq _velocity_covariance __velocity_covariance)
   (setq _acceleration_covariance __acceleration_covariance)
   (setq _size_covariance __size_covariance)
   (setq _amplitude (float __amplitude))
   self)
  (:uuid
   (&optional __uuid)
   (if __uuid (setq _uuid __uuid)) _uuid)
  (:position
   (&rest __position)
   (if (keywordp (car __position))
       (send* _position __position)
     (progn
       (if __position (setq _position (car __position)))
       _position)))
  (:velocity
   (&rest __velocity)
   (if (keywordp (car __velocity))
       (send* _velocity __velocity)
     (progn
       (if __velocity (setq _velocity (car __velocity)))
       _velocity)))
  (:acceleration
   (&rest __acceleration)
   (if (keywordp (car __acceleration))
       (send* _acceleration __acceleration)
     (progn
       (if __acceleration (setq _acceleration (car __acceleration)))
       _acceleration)))
  (:size
   (&rest __size)
   (if (keywordp (car __size))
       (send* _size __size)
     (progn
       (if __size (setq _size (car __size)))
       _size)))
  (:classification
   (&optional __classification)
   (if __classification (setq _classification __classification)) _classification)
  (:position_covariance
   (&optional __position_covariance)
   (if __position_covariance (setq _position_covariance __position_covariance)) _position_covariance)
  (:velocity_covariance
   (&optional __velocity_covariance)
   (if __velocity_covariance (setq _velocity_covariance __velocity_covariance)) _velocity_covariance)
  (:acceleration_covariance
   (&optional __acceleration_covariance)
   (if __acceleration_covariance (setq _acceleration_covariance __acceleration_covariance)) _acceleration_covariance)
  (:size_covariance
   (&optional __size_covariance)
   (if __size_covariance (setq _size_covariance __size_covariance)) _size_covariance)
  (:amplitude
   (&optional __amplitude)
   (if __amplitude (setq _amplitude __amplitude)) _amplitude)
  (:serialization-length
   ()
   (+
    ;; int8 _uuid
    1
    ;; geometry_msgs/Point _position
    (send _position :serialization-length)
    ;; geometry_msgs/Vector3 _velocity
    (send _velocity :serialization-length)
    ;; geometry_msgs/Vector3 _acceleration
    (send _acceleration :serialization-length)
    ;; geometry_msgs/Vector3 _size
    (send _size :serialization-length)
    ;; uint16 _classification
    2
    ;; float32[] _position_covariance
    (* 4    (length _position_covariance)) 4
    ;; float32[] _velocity_covariance
    (* 4    (length _velocity_covariance)) 4
    ;; float32[] _acceleration_covariance
    (* 4    (length _acceleration_covariance)) 4
    ;; float32[] _size_covariance
    (* 4    (length _size_covariance)) 4
    ;; float32 _amplitude
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int8 _uuid
       (write-byte _uuid s)
     ;; geometry_msgs/Point _position
       (send _position :serialize s)
     ;; geometry_msgs/Vector3 _velocity
       (send _velocity :serialize s)
     ;; geometry_msgs/Vector3 _acceleration
       (send _acceleration :serialize s)
     ;; geometry_msgs/Vector3 _size
       (send _size :serialize s)
     ;; uint16 _classification
       (write-word _classification s)
     ;; float32[] _position_covariance
     (write-long (length _position_covariance) s)
     (dotimes (i (length _position_covariance))
       (sys::poke (elt _position_covariance i) (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
       )
     ;; float32[] _velocity_covariance
     (write-long (length _velocity_covariance) s)
     (dotimes (i (length _velocity_covariance))
       (sys::poke (elt _velocity_covariance i) (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
       )
     ;; float32[] _acceleration_covariance
     (write-long (length _acceleration_covariance) s)
     (dotimes (i (length _acceleration_covariance))
       (sys::poke (elt _acceleration_covariance i) (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
       )
     ;; float32[] _size_covariance
     (write-long (length _size_covariance) s)
     (dotimes (i (length _size_covariance))
       (sys::poke (elt _size_covariance i) (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
       )
     ;; float32 _amplitude
       (sys::poke _amplitude (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int8 _uuid
     (setq _uuid (sys::peek buf ptr- :char)) (incf ptr- 1)
     (if (> _uuid 127) (setq _uuid (- _uuid 256)))
   ;; geometry_msgs/Point _position
     (send _position :deserialize buf ptr-) (incf ptr- (send _position :serialization-length))
   ;; geometry_msgs/Vector3 _velocity
     (send _velocity :deserialize buf ptr-) (incf ptr- (send _velocity :serialization-length))
   ;; geometry_msgs/Vector3 _acceleration
     (send _acceleration :deserialize buf ptr-) (incf ptr- (send _acceleration :serialization-length))
   ;; geometry_msgs/Vector3 _size
     (send _size :deserialize buf ptr-) (incf ptr- (send _size :serialization-length))
   ;; uint16 _classification
     (setq _classification (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; float32[] _position_covariance
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _position_covariance (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _position_covariance i) (sys::peek buf ptr- :float)) (incf ptr- 4)
     ))
   ;; float32[] _velocity_covariance
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _velocity_covariance (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _velocity_covariance i) (sys::peek buf ptr- :float)) (incf ptr- 4)
     ))
   ;; float32[] _acceleration_covariance
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _acceleration_covariance (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _acceleration_covariance i) (sys::peek buf ptr- :float)) (incf ptr- 4)
     ))
   ;; float32[] _size_covariance
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _size_covariance (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _size_covariance i) (sys::peek buf ptr- :float)) (incf ptr- 4)
     ))
   ;; float32 _amplitude
     (setq _amplitude (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get morai_msgs::RadarTrack :md5sum-) "da20584d0f09f9e2d2e7565bee064422")
(setf (get morai_msgs::RadarTrack :datatype-) "morai_msgs/RadarTrack")
(setf (get morai_msgs::RadarTrack :definition-)
      "# This message relates only to FMCW radar.  
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



(provide :morai_msgs/RadarTrack "da20584d0f09f9e2d2e7565bee064422")


