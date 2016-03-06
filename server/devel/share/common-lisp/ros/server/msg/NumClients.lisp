; Auto-generated. Do not edit!


(cl:in-package server-msg)


;//! \htmlinclude NumClients.msg.html

(cl:defclass <NumClients> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (clientIds
    :reader clientIds
    :initarg :clientIds
    :type (cl:vector cl:fixnum)
   :initform (cl:make-array 0 :element-type 'cl:fixnum :initial-element 0)))
)

(cl:defclass NumClients (<NumClients>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <NumClients>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'NumClients)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name server-msg:<NumClients> is deprecated: use server-msg:NumClients instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <NumClients>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader server-msg:header-val is deprecated.  Use server-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'clientIds-val :lambda-list '(m))
(cl:defmethod clientIds-val ((m <NumClients>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader server-msg:clientIds-val is deprecated.  Use server-msg:clientIds instead.")
  (clientIds m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <NumClients>) ostream)
  "Serializes a message object of type '<NumClients>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'clientIds))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let* ((signed ele) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    ))
   (cl:slot-value msg 'clientIds))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <NumClients>) istream)
  "Deserializes a message object of type '<NumClients>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'clientIds) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'clientIds)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:aref vals i) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256)))))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<NumClients>)))
  "Returns string type for a message object of type '<NumClients>"
  "server/NumClients")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'NumClients)))
  "Returns string type for a message object of type 'NumClients"
  "server/NumClients")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<NumClients>)))
  "Returns md5sum for a message object of type '<NumClients>"
  "41f501fdc974f486e8d56df095ccd1de")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'NumClients)))
  "Returns md5sum for a message object of type 'NumClients"
  "41f501fdc974f486e8d56df095ccd1de")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<NumClients>)))
  "Returns full string definition for message of type '<NumClients>"
  (cl:format cl:nil "Header header~%int8[] clientIds~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'NumClients)))
  "Returns full string definition for message of type 'NumClients"
  (cl:format cl:nil "Header header~%int8[] clientIds~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <NumClients>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'clientIds) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 1)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <NumClients>))
  "Converts a ROS message object to a list"
  (cl:list 'NumClients
    (cl:cons ':header (header msg))
    (cl:cons ':clientIds (clientIds msg))
))
