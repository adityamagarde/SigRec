# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 13:47:23 2017

@author: ADITYA
"""

#project.py


import PIL
import base64
from skimage.morphology import skeletonize
import numpy
import cv2

#Converting image into grayscaleNo such file or directory:
img = PIL.Image.open(r'F:\Files\Projects\SignaturerRecognition\Experimental\NISDCC-001_001_001_6g.png').convert("L");
img.save(r"F:\Files\Projects\SignaturerRecognition\Experimental\sig1.png");

#Converting grayscale into binary
#with open(r"F:\Files\Projects\SignaturerRecognition\Experimental\sig1.png", "rb") as imageFile:
#   str = base64.b64encode(imageFile.read())
#    print(str)


#projectFile = open("F:\Files\Projects\SignaturerRecognition\alpha.txt","a")
#projectFile.write(str);
#projectFile.close;

#Resizing image
baseWidth = 256
aspectRatio = (baseWidth/float(img.size[0]));
hSize = int ((float(img.size[1])*float(aspectRatio)));
img = img.resize((baseWidth, hSize), Image.ANTIALIAS);
img.save(r'F:\Files\Projects\SignaturerRecognition\Experimental\resized_image.jpg')



#Converting image into binary numpy array

img = cv2.imread(r"F:\Files\Projects\SignaturerRecognition\Experimental\sig1.png",0)
ret,thresh_img = cv2.threshold(img,127,255,cv2.THRESH_BINARY)


#-----------------------------------------------------------------------------------------------------------------------------
#Converting image into NumPy Array


# Convert Image to array
#img = PIL.Image.open("foo.jpg").convert("L")
#arr = numpy.array(img)


# Convert array to Image
#img = PIL.Image.fromarray(arr)

img = img.convert("L")
imageArray = numpy.array(img)


#-----------------------------------------------------------------------------------------------------------------------------

#Skeletonize the image
skeleton = skeletonize(thresh_img)

