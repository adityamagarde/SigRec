# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 23:27:02 2017

@author: ADITYA
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 10:42:49 2017

@author: ADITYA
"""


import PIL
from PIL import Image
from matplotlib import pyplot as plt
from skimage.morphology import skeletonize
from skimage import img_as_bool, io, color, morphology
import numpy
import cv2
import scipy.misc


#CONVERTING IMAGE INTO GRAYSCALE IMAGE ------------------------------------------------------------------------------
img = PIL.Image.open(r'F:\Files\Projects\SignaturerRecognition\Experimental\NISDCC-001_001_001_6g.png').convert("L");
img.save(r"F:\Files\Projects\SignaturerRecognition\Experimental\sig1.png");


#CONVERTING IMAGE INTO BINARY ---------------------------------------------------------------------------------------
img_threshold = cv2.imread(r'F:\Files\Projects\SignaturerRecognition\Experimental\NISDCC-001_001_001_6g.png')
imgray = cv2.cvtColor(img_threshold,cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(imgray,(1,1),0)
ret , img_binary = cv2.threshold(imgray,250,255,cv2.THRESH_BINARY)

plt.imshow(img_binary, 'gray')
plt.show()


#SAVING THE BINARY IMAGE --------------------------------------------------------------------------------------------
scipy.misc.imsave(r'F:\Files\Projects\SignaturerRecognition\Experimental\binary_image1.png', img_binary)


#RESIZING THE IMAGE -------------------------------------------------------------------------------------------------
baseWidth = 256
aspectRatio = (baseWidth/float(img.size[0]));
hSize = int ((float(img.size[1])*float(aspectRatio)));
img_resized = img.resize((baseWidth, hSize), PIL.Image.ANTIALIAS);
img_resized.save(r'F:\Files\Projects\SignaturerRecognition\Experimental\resized_image.png')


#CONVERTING BINARY 255 TO 1 -------------------------------------------------------------------------------------------
img_binaryOne = img_binary
img_binaryOne[img_binaryOne == 255] = 1


#ERODE IMAGE ----------------------------------------------------------------------------------------------------------
imagem = img_threshold
imagem = cv2.bitwise_not(imagem)
plt.imshow(imagem, 'gray')
plt.show()


kernel = numpy.ones((5,5),numpy.uint8)
erosionbw = cv2.erode(imagem, kernel,iterations = 1)
plt.imshow(erosionbw, 'gray')
plt.show()
erosionbwInverted = erosionbw
erosionbw = cv2.bitwise_not(erosionbw)


#ONCE AGAIN COVERTING TO BINARY -------------------------------------------------------------------------------------
imgrayEroded = cv2.cvtColor(erosionbw,cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(imgrayEroded,(1,1),0)
ret , img_binaryEroded = cv2.threshold(imgrayEroded,250,255,cv2.THRESH_BINARY)


plt.imshow(img_binaryEroded, 'gray')
plt.show()

#SAVING THE BINARY ERODED IMAGE -------------------------------------------------------------------------------------
img_resizedBinaryEroded = scipy.misc.imresize(img_binaryEroded, 0.20)
scipy.misc.imsave(r'F:\Files\Projects\SignaturerRecognition\Experimental\erosion_imageBW.png', img_resizedBinaryEroded)

img_binaryEroded[img_binaryEroded == 255] = 1



