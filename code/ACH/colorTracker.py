#!/usr/bin/env python

#import controller_include as ci
import csv


#import ach
import sys
import time
from ctypes import *
import socket
import cv2.cv as cv
import cv2
import numpy as np
import cog_include as ci

#import actuator_sim as ser

'''
CONTROLLER_REF_NAME  = 'cog-chan'
error = ach.Channel(ci.CONTROLLER_REF_NAME)
error.flush()
cog = ci.CONTROLLER_REF()
'''

cap = cv2.VideoCapture(0)
ret, frame = cap.read()
height, width, depth = frame.shape
#print 'H = ', height, ' W = ', width
cv2.waitKey(5)

while True:

    ret, frame = cap.read()
    img = frame

    # Convert RGB to HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Define upper and lower range of blue color in HSV
    lower_blue = np.array([100,50,50], dtype=np.uint8)
    upper_blue = np.array([130,255,255], dtype=np.uint8)

    # Threshold the HSV image to get only blue
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    kernel = np.ones((5,5), np.uint8)
    erosion = cv2.erode(mask, kernel, iterations = 5)
    dilation = cv2.dilate(erosion, kernel, iterations = 5)

    # Use findContours to get the boundry of the green blob
    contours,hierarchy = cv2.findContours(dilation,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    if (len(contours) > 0):
        cnt = contours[0]
        #Finding centroids of best_cnt and draw a circle there
        M = cv2.moments(cnt)
        x = int(M['m10']/M['m00'])
        y = int(M['m01']/M['m00'])
        cv2.circle(img,(x,y),5,(0,0,255),-1)

	dx = cx-width/2
	dy = cy-height/2

    else: #if no color seen, set error to 0
    	dx = 0
    	dy = 0

    cv2.imshow('wctrl',img)

    cv2.waitKey(5)

    print '\nError in x & y: ', x, '\t', y

    # send the error to controller
    #cog.x = x
    #cog.y = y
    #error.put(cog)
    #time.sleep(.1)

    kp = .5
    kd = .5
    ki = .5

    PIDx = kp*dx+kp(dx
    





