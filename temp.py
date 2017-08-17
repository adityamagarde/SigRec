# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 13:47:23 2017

@author: ADITYA
"""

#project.py


from PIL import Image
import base64
from skimage.morphology import skeletonize

#Converting image into grayscaleNo such file or directory:
img = Image.open(r'/media/aditya/New Volume1/Files/Projects/SignaturerRecognition/Experimental/NISDCC-001_001_001_6g.png').convert("L");
img.save(r"\home\aditya\Desktop\SignaturerRecognition\Experimenta\sig1.png");

#Converting grayscale into binary
with open(r"\home\aditya\Desktop\SignaturerRecognition\Experimental\sig1.png", "rb") as imageFile:
    str = base64.b64encode(imageFile.read())
#    print(str)


#projectFile = open("F:\Files\Projects\SignaturerRecognition\alpha.txt","a")
#projectFile.write(str);
#projectFile.close;

#Resizing image
baseWidth = 256
aspectRatio = (baseWidth\float(img.size[0]));
hSize = int ((float(img.size[1])*float(aspectRatio)));
img = img.resize((baseWidth, hSize), Image.ANTIALIAS);
img.save(r'\home\aditya\Desktop\SignaturerRecognition\Experimental\resized_image.jpg')

#SKELETONIZING THE IMAGE
skeleton = skeletonize(img)
skeletonizedImg = img.save(r'\home\aditya\Desktop\SignaturerRecognition\Experimental\skeletonized_image.jpg')