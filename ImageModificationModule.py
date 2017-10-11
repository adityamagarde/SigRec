# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 23:41:17 2017

@author: ADITYA
"""

import cv2
import numpy as np

def getImageArray(string):
    #CONVERTING IMAGE INTO GRAYSCALE IMAGE ------------------------------------------------------------------------------
    img = cv2.imread(string)
    
    #GRAYSCALING --------------------------------------------------------------------------------------------------------
    grayFrame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    #OBTAINING THE SHAPE OF THE IMAGE -----------------------------------------------------------------------------------
    grayFrameShape = grayFrame.shape[:2]
    
    #RESIZING THE IMAGE -------------------------------------------------------------------------------------------------
    divisionValue = 200.0/grayFrameShape[0]
    rows = 200
    cols = int(grayFrameShape[1]*divisionValue)
    grayFrameResized = cv2.resize(grayFrame, (cols, rows))
    
    
    #THRESHOLDING THE IMAGE  --------------------------------------------------------------------------------------------
    ret, thresholdFrame = cv2.threshold(grayFrameResized, 250, 255, cv2.THRESH_BINARY)
    
    
    #BINARIZING THE RESIZED IMAGE ---------------------------------------------------------------------------------------
    finalImage = thresholdFrame
    finalBinary = np.clip(finalImage, 0 ,1)
    
    #FUNCTION TO RETURN THE IMAGE ---------------------------------------------------------------------------------------
    return finalBinary, finalImage


#cv2.imshow('grayImage', grayImage)
#cv2.imshow('threshold', thresholdFrame)
#cv2.imshow('resized', f)
#cv2.waitKey(0)
#cv2.destroyAllWindows()