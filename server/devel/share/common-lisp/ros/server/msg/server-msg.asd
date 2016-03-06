
(cl:in-package :asdf)

(defsystem "server-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :std_msgs-msg
)
  :components ((:file "_package")
    (:file "NewClient" :depends-on ("_package_NewClient"))
    (:file "_package_NewClient" :depends-on ("_package"))
    (:file "CurrentClients" :depends-on ("_package_CurrentClients"))
    (:file "_package_CurrentClients" :depends-on ("_package"))
  ))