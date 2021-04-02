#!/usr/bin/env python
# written by Hariharan (A.H.N)
import rospy
from sensor_msgs.msg import LaserScan 
from geometry_msgs.msg import Twist

def obst(scan):
 th = 1.0
 if scan.ranges[0] >th and scan.ranges[30] >th and scan.ranges[330] > th :
   twist.linear.x = 0.5
   twist.angular.z = 0.0
 elif scan.ranges[0] < th :
   if scan.ranges[30] <scan.ranges[330] :
      twist.linear.x = 0
      twist.angular.z = 0.5
   else :
      twist.linear.x = 0.0
      twist.angular.z = -0.5
 else : 
      twist.linear.x = 0.5
      twist.angular.z = 0.0
 pub.publish(twist)
 
 print "published "


twist = Twist()
rospy.init_node('obstacle_avoider')
pub = rospy.Publisher("/cmd_vel" , Twist , queue_size = 10 )
sub = rospy.Subscriber("/scan", LaserScan , obst)
rospy.spin()
