; Auto-generated. Do not edit!


(cl:in-package server-msg)


;//! \htmlinclude CurrentClients.msg.html

(cl:defclass <CurrentClients> (roslisp-msg-protocol:ros-message)
  ((clientIds
    :reader clientIds
    :initarg :clientIds
    :type (cl:vector cl:fixnum)
   :initform (cl:make-array 0 :element-type 'cl:fixnum :initial-element 0)))
)

(cl:defclass CurrentClients (<CurrentClients>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <CurrentClients>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'CurrentClients)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name server-msg:<CurrentClients> is deprecated: use server-msg:CurrentClients instead.")))

(cl:ensure-generic-function 'clientIds-val :lambda-list '(m))
(cl:defmethod clientIds-val ((m <CurrentClients>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader server-msg:clientIds-val is deprecated.  Use server-msg:clientIds instead.")
  (clientIds m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <CurrentClients>) ostream)
  "Serializes a message object of type '<CurrentClients>"
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
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <CurrentClients>) istream)
  "Deserializes a message object of type '<CurrentClients>"
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
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<CurrentClients>)))
  "Returns string type for a message object of type '<CurrentClients>"
  "server/CurrentClients")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'CurrentClients)))
  "Returns string type for a message object of type 'CurrentClients"
  "server/CurrentClients")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<CurrentClients>)))
  "Returns md5sum for a message object of type '<CurrentClients>"
  "321d5ee1fa12e83bad0a9350af092cea")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'CurrentClients)))
  "Returns md5sum for a message object of type 'CurrentClients"
  "321d5ee1fa12e83bad0a9350af092cea")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<CurrentClients>)))
  "Returns full string definition for message of type '<CurrentClients>"
  (cl:format cl:nil "int8[] clientIds~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'CurrentClients)))
  "Returns full string definition for message of type 'CurrentClients"
  (cl:format cl:nil "int8[] clientIds~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <CurrentClients>))
  (cl:+ 0
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'clientIds) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 1)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <CurrentClients>))
  "Converts a ROS message object to a list"
  (cl:list 'CurrentClients
    (cl:cons ':clientIds (clientIds msg))
))
