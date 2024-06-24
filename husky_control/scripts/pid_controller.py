#!/usr/bin/env python3
# license removed for brevity
import rospy
import math
import numpy as np

def pid_controller(d,ed,edi):

	kp=1      #To be set by students
	ki=0.0005 #To be set by students
	kd=0      #To be set by students

	
	edi=edi+ed #error integration
	  
	w=max(min(1.86, kp*d + ki*edi + kd*(d-ed)),-1.86)
	v=0.2*np.exp(-10*abs(w))  # Max speed set as 0.15
	
	ed=d #previus error

	print("v_cmd", v, "w_cmd", w)
	return v,w,ed,edi   
	#######################################################################################

