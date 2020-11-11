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

from bs4 import BeautifulSoup 
  
  
# Reading the data inside the xml 
# file to a variable under the name  
# data 
with open('name00000005.xml', 'r') as f: 
    data = f.read() 
  
# Passing the stored data inside 
# the beautifulsoup parser, storing 
# the returned object  
Bs_data = BeautifulSoup(data, "xml") 
  
# Finding all instances of tag  
# `unique` 

championNamesFoundInXMLList = []

championXminFoundInXMLList = []
championYminFoundInXMLList = []
championXmaxFoundInXMLList = []
championYmaxFoundInXMLList = []


def findSomethingInXMLFormatReturnStandardTypeList(tagToFind="name", standardTypeToConvert = str):
    b_ChampNames = Bs_data.find_all(tagToFind) 
      
    print("BS4 found names with tags: ", b_ChampNames) 
    
    listWithStandardType = []
    
    for points in b_ChampNames:
        listWithStandardType.append(standardTypeToConvert(points.text))
        
    print("type inside listWithStandardType: ", standardTypeToConvert)    
    print("listWithStandardType: ", listWithStandardType)
    return listWithStandardType



championNamesFoundInXMLList = findSomethingInXMLFormatReturnStandardTypeList("name", str)

championXminFoundInXMLList = findSomethingInXMLFormatReturnStandardTypeList("xmin", int)
championYminFoundInXMLList = findSomethingInXMLFormatReturnStandardTypeList("ymin", int)
championXmaxFoundInXMLList = findSomethingInXMLFormatReturnStandardTypeList("xmax", int)
championYmaxFoundInXMLList = findSomethingInXMLFormatReturnStandardTypeList("ymax", int)










  
# Using find() to extract attributes  
# of the first instance of the tag 
b_name = Bs_data.find('object') 
  
print(b_name) 
  
# Extracting the data stored in a 
# specific attribute of the  
# `child` tag 
value = b_name.get('bndbox') 
  
print(value) 