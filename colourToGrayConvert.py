# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 16:31:27 2017

@author: ADITYA
"""


from PIL import Image
import base64


#Converting the image into black and white...
img = Image.open(r'C:\Users\ADITYA\Pictures\Untitled.png').convert('L')
img.save(r'C:\Users\ADITYA\Pictures\output_file.png')

#Converting the image into binary string
with open(r'C:\Users\ADITYA\Pictures\output_file.png', "rb") as imageFile:
    str = base64.b64encode(imageFile.read())
    print(str);
    
file1 = open(r'F:\Files\Projects\SignaturerRecognition\alpha.txt','a');
file1.write(str);
file1.close();



    
