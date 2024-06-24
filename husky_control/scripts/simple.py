#!/usr/bin/env python
# license removed for brevity
import rospy
import math
import numpy as np
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from std_msgs.msg import Float64MultiArray
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Float32
import csv

class recorder:
  
	scan_data = []
  
	def scan_callback(self,sc_msg):

		recorder.scan_data= sc_msg.ranges

	def move(self):
		pub = rospy.Publisher('/cmd_vel', Twist, queue_size=100)
		rospy.init_node('husky_teleop_keyboard')
		rate = rospy.Rate(1) # 1hz
		scn_arr = recorder.scan_data
		

		while not rospy.is_shutdown():               
			rospy.Subscriber('/scan',LaserScan,rec.scan_callback)
			if not scn_arr:
				scn_arr = list(np.zeros(360))	# GAZEBO L=360 / REAL L = 1153
			else:
				scn_arr = recorder.scan_data
			L = len(scn_arr)
			res = float(360)/L

			#scn_arr = [x if x>0 else 1000 for x in scn_arr]	#Comment out on GAZEBO
			
			####################@TODO write your code below##########################

			#print(scn_arr) # "arr" is the scan data array(list of 360 values)
			d = min(scn_arr)
			ind = scn_arr.index(min(scn_arr))*res		#This is for GAZEBO ROBOT / Comment out on REAL
			#ind = scn_arr.index(min(scn_arr))*res-180	#This is for REAL ROBOT / Comment out on GAZEBO
			print(d, ind)

			v_cmd=0
			w_cmd=0

			#########################################################################
			vel_msg=Twist()
			vel_msg.linear.x  = v_cmd
			vel_msg.angular.z = w_cmd

			#print("ind:% f v_cmd : % 2f, omega_cmd : % 5.2f" %(ind, v_cmd, w_cmd))
			pub.publish(vel_msg)
			rate.sleep()
	
if __name__ == '__main__': 

	try:         
		rec = recorder()
		rospy.Subscriber('/scan',LaserScan,rec.scan_callback)
		rec.move()         	
	except rospy.ROSInterruptException:
		pass
