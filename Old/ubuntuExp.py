#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 17:50:49 2017

@author: aditya
"""

from PIL import Image
import base64
from skimage.morphology import skeletonize
import os

#os.chdir("/path/to/Desktop")
#Converting image into binary
img = Image.open(r'/home/aditya/Desktop/SignaturerRecognition/Experimental/NISDCC-001_001_001_6g.PNG').convert('L');
img.save(r"/home/aditya/Desktop/SignaturerRecognition/Experimental/sig1.png");

#Converting grayscale into binary
with open(r"/home/aditya/Desktop/SignaturerRecognition/Experimental/sig1.png", "rb") as imageFile:
    str = base64.b64encode(imageFile.read())
 
    
#Resizing image
baseWidth = 256
aspectRatio = (baseWidth/float(img.size[0]))
hSize = int ((float(img.size[1])*float(aspectRatio)))
img = img.resize((baseWidth, hSize), Image.ANTIALIAS)
img.save(r'/home/aditya/Desktop/SignaturerRecognition/Experimental/resized_image.PNG')
