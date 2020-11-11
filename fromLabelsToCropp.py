# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 08:35:15 2020

@author: janusz

This file should pickup .xml file with pascalVoc format labels, 
then cropp this image for every bounding box
and at the end save cropped images into right [training] directory 
which will be nammed as [characters] in label name.
At the end i hope for looping this all over for every .xml file in specified directory.
Plan:
    1. Open .xml file.
    2. Pickup bounding box.
    3. Cropp img at bounding box.
    4. Save cropped image into specified directory.
    
    1. Makedirs if not exist for training directory named as characters in labels.
    2. Pickup right path to save cropped image into specified directory.
    3. Check file with highest number in name [ {:08d} or name+{:08d} format ].
    4. Save cropped image.
    

"""

