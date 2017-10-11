# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 00:29:47 2017

@author: ADITYA
"""
import numpy as np
from ImageModificationModule import *
import cv2
import pandas as pd
import csv
import os


#DATASET PREPARATION AND COMPILATION
option = input('\nWelcome to the signature verification system.')

directory = input('Enter the directory name : ')
DIR = 'Images\\' + directory
for img in (os.listdir(DIR)):
        path = os.path.join(DIR,img)
        
        #ACCESSING THE IMAGE        
        imageB, image  = getImageArray(path)
    #    directory = directory - '.png'
    #    directory = directory - string2
        dims = imageB.shape
        
        
        #MAXIMUM HORIZONTAL HISTOGRAM
        nb_zerosH = 0
        horizontalMax = 0
        for i in range(0, dims[0]):
            temp = np.count_nonzero(imageB[i , :])
            temp = dims[1]- 1 - temp
            if nb_zerosH<temp:
                nb_zerosH = temp
                horizontalMax = i
        
        
        #MAXIMUM VERTICAL HISTOGRAM
        nb_zerosV = 0
        verticalMax = 0
        for i in range(0, dims[1]):
            temp = np.count_nonzero(imageB[:, i])
            temp = dims[0] - 1 - temp
            if nb_zerosV<temp:
                nb_zerosV = temp
                verticalMax = i
                
        
        #FINDING CENTER OF MASS
        from scipy import ndimage
        comLeftHalf = ndimage.measurements.center_of_mass(imageB[:, 0:int(dims[1]/2)])
        comLeftHalfX = comLeftHalf[0]
        comLeftHalfY = comLeftHalf[1]
        comRightHalf = ndimage.measurements.center_of_mass(imageB[:, int(dims[1]/2):]) 
        comRightHalfY = comRightHalf[0]
        comRightHalfX = comRightHalf[1]
        
        #NORMALISED SIGNATURE AREA
        signatureArea = np.count_nonzero(imageB == 0)
        normalisedSignatureArea = signatureArea/(dims[0]*dims[1])
        
        
        #FINDING THE RATIO OF WIDTH AND HEIGHT
        yzero = 1
        for i in range(0, dims[0]):
            temp = np.count_nonzero(imageB[i, :])
            if temp<(dims[1]-1):
                yzero = i
                break
            
        yfinal = 0
        for i in range(dims[0]-1, 0, -1):
            temp = np.count_nonzero(imageB[i, :])
            if temp<(dims[1]-1):
                yfinal = i
                break
            
        xzero = 0    
        for i in range(0, dims[1]):
            temp = np.count_nonzero(imageB[:, i])
            if temp<(dims[0]-1):
                xzero = i
                break
            
        xfinal = 0
        for i in range(dims[1]-1, 0, -1):
            temp = np.count_nonzero(imageB[:, i])
            if temp<(dims[0]-1):
                xfinal = i
                break
            
        ratio = (yfinal - yzero)/(xfinal - xzero)
        
        
        #NORMALISED AREA FOR 3 HALVES
        #areaOfFirstHalf
        count = np.count_nonzero(imageB[:, 0:int(dims[1]/3)] == 0)
        areaOneThirdFirst = count/(dims[0]*(dims[1]/3))
        count = np.count_nonzero(imageB[:, int(dims[1]/3):2*int(dims[1]/3)] == 0)
        areaOneThirdSecond = count/(dims[0]*(dims[1]/3))
        count = np.count_nonzero(imageB[:, 2*int(dims[1]/3):3*int(dims[1]/3)] == 0)
        areaOneThirdThird = count/(dims[0]*(dims[1]/3))
        
        
        #NORMALISED AREA FOR 6 HALVES
        count = np.count_nonzero(imageB[0:int(dims[0]/2), 0:int(dims[1]/3)] == 0)
        areaOneSixthFirst = count/((dims[0]/2)*(dims[1]/3))
        count = np.count_nonzero(imageB[int(dims[0]/2):2*int(dims[0]/2), 0:int(dims[1]/3)] == 0)
        areaOneSixthSecond = count/((dims[0]/2)*(dims[1]/3))
        
        count = np.count_nonzero(imageB[0:int(dims[0]/2), int(dims[1]/3):2*int(dims[1]/3)] == 0)
        areaOneSixthThird = count/((dims[0]/2)*(dims[1]/3))
        count = np.count_nonzero(imageB[int(dims[0]/2):2*int(dims[0]/2), int(dims[1]/3):2*(int(dims[1]/3))] == 0)
        areaOneSixthFourth = count/((dims[0]/2)*(dims[1]/3))
        
        count = np.count_nonzero(imageB[0:int(dims[0]/2), 2*(int(dims[1]/3)):3*int(dims[1]/3)] == 0)
        areaOneSixthFifth = count/((dims[0]/2)*(dims[1]/3))
        count = np.count_nonzero(imageB[int(dims[0]/2):2*int(dims[0]/2), int(dims[1]/3):2*(int(dims[1]/3))] == 0)
        areaOneSixthSixth = count/((dims[0]/2)*(dims[1]/3))
        
        #FLIP AND BITWISE AND
        imageDash = cv2.bitwise_not(image)
        flip = imageDash.copy()
        flip = cv2.flip(flip, 1)
        andedImage = cv2.bitwise_and(imageDash, flip)
        andedImage = cv2.bitwise_not(andedImage)
        bitwiseAnd = np.count_nonzero(andedImage)
        
        
        #CREATING THE CSV FILE
        if directory=='Real':
            rowVariable = (horizontalMax, verticalMax, comLeftHalfX, comLeftHalfY, comRightHalfX, comLeftHalfY, normalisedSignatureArea, 
                           ratio, areaOneThirdFirst, areaOneThirdSecond, areaOneThirdThird, areaOneSixthFirst, 
                           areaOneSixthSecond, areaOneSixthThird, areaOneSixthFourth, areaOneSixthFifth, areaOneSixthSixth)
            with open(r'DatasetsCreated\oneSet1.csv', 'a', newline='') as outfile:
                writer = csv.writer(outfile)
                writer.writerow(rowVariable)
            print('The features have been extracted and stored into the csv file')
            
        else:
            rowVariable = (horizontalMax, verticalMax, comLeftHalfX, comLeftHalfY, comRightHalfX, comLeftHalfY, normalisedSignatureArea, 
                           ratio, areaOneThirdFirst, areaOneThirdSecond, areaOneThirdThird, areaOneSixthFirst, 
                           areaOneSixthSecond, areaOneSixthThird, areaOneSixthFourth, areaOneSixthFifth, areaOneSixthSixth)
            with open(r'DatasetsCreated\testSet.csv', 'a', newline='') as outfile:
                writer = csv.writer(outfile)
                writer.writerow(rowVariable)
            print('The features have been extracted and stored into the csv file')
        
    