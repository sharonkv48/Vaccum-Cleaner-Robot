# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 13:16:54 2022

@author: sharo
"""

import vrep
import sys
import numpy as np
import matplotlib.pyplot as mlp



vrep.simxFinish(-1) # just in case, close all opened connections

clientID=vrep.simxStart('127.0.0.1',19999,True,True,5000,5)

if clientID!=-1:
    print 'Connected to remote API server'
else:
    print 'connection not successful'
    sys.exit('Error could not connect')
    
errorCode,left_motor_handle=vrep.simxGetObjectHandle(clientID,'Pioneer_p3dx_leftMotor',vrep.simx_opmode_oneshot_wait)
errorCode,right_motor_handle=vrep.simxGetObjectHandle(clientID,'Pioneer_p3dx_rightMotor',vrep.simx_opmode_oneshot_wait)


errorCode=vrep.simxSetJointTargetVelocity(clientID,left_motor_handle,0.2,vrep.simx_opmode_streaming)
errorCode=vrep.simxSetJointTargetVelocity(clientID,right_motor_handle,0.2,vrep.simx_opmode_streaming)

errorCode,resolution,image=vrep.simxGetVisionSensorImage(clientID,cam_handle,0,vrep.simx_opmode_buffer)

