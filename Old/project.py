# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 13:47:23 2017

@author: ADITYA
"""

#project.py


from PIL import Image
import base64

#Converting image into grayscale
img = Image.open(r'F:\Files\Projects\SignaturerRecognition\ExperimentalZone\NISDCC-001_001_001_6g.png').convert("L");
img.save("F:\Files\Projects\SignaturerRecognition\ExperimentalZone\sig1.png");

#Converting grayscale into binary
with open("F:\Files\Projects\SignaturerRecognition\ExperimentalZone\sig1.png", "rb") as imageFile:
    str = base64.b64encode(imageFile.read())
#    print(str)


#projectFile = open("F:\Files\Projects\SignaturerRecognition\alpha.txt","a")
#projectFile.write(str);
#projectFile.close;

#Resizing image
baseWidth = 256
aspectRatio = (baseWidth/float(img.size[0]));
hSize = int ((float(img.size[1])*float(aspectRatio)));
img = img.resize((baseWidth, hSize), Image.ANTIALIAS);
img.save(r'F:\Files\Projects\SignaturerRecognition\ExperimentalZone\resized_image.jpg')

