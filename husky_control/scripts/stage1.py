#!/usr/bin/env python3
# license removed for brevity

import math
import numpy as np
import matplotlib.pyplot as plt
import sys
#from path_planning_1 import *
from pid_controller import *
def stage1(est_pos,rx,ry):  
    
    #Current estimated state of the robot
    xc,yc,tc=est_pos
    ed=0
    edi=0
    for i in range(len(rx)):
        S=(rx[i]*0.1-xc)*np.cos(tc) + (ry[i]*0.1-yc)*np.sin(tc)
        d=(ry[i]*0.1-yc)*np.cos(tc) - (rx[i]*0.1-xc)*np.sin(tc)
        if S>0.08: 
          break
    print("xd", S, "yd", d)
    v_cmd,w_cmd,esi,edi = pid_controller(d,ed,edi)

    dl=np.sqrt((rx[-1]*0.1-xc)**2 + (ry[-1]*0.1-yc)**2)
    if dl<0.1:
            v_cmd=0
            w_cmd=0 
    print("final", dl)

    return v_cmd,w_cmd,ed,edi
