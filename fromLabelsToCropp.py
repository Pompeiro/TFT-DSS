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
import cv2 as cv
  
  
# Reading the data inside the xml 
# file to a variable under the name  
# data 
with open('name00000005.xml', 'r') as f: 
    data = f.read() 
  
# Passing the stored data inside 
# the beautifulsoup parser, storing 
# the returned object  
Bs_data = BeautifulSoup(data, "xml") 
  

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


screenshot = cv.imread("name00000005.jpg",cv.IMREAD_UNCHANGED)
cv.imshow("ss", screenshot)








############# BASE CODE for single champion rectangle


# line_color = (255, 0, 255)
# line_color_odd = (0,255,0)
# line_type = cv.LINE_4
# marker_color = (255, 0, 255)
# marker_type = cv.MARKER_CROSS
# marker_type_rectangle = cv.MARKER_SQUARE


# championWidth = championXmaxFoundInXMLList[0] - championXminFoundInXMLList[0]

# championHeight = championYmaxFoundInXMLList[0] - championYminFoundInXMLList[0]


# topLeft = (championXminFoundInXMLList[0], championYminFoundInXMLList[0])
# bottomRight = (topLeft[0] + championWidth, topLeft[1] + championHeight)
# center = ((topLeft[0]+bottomRight[0])//2, (topLeft[1]+bottomRight[1])//2)

# marker_position = [topLeft, bottomRight, center]



# def draw_rectangle_and_center_and_show(screenshot, markerPosition=marker_position,line_coloring=line_color, showMode=1,name="wind"):
#     cv.drawMarker(screenshot, markerPosition[2], color=line_coloring,
#                   markerType=marker_type, markerSize=40, thickness=2)
#     cv.rectangle(screenshot, markerPosition[0], markerPosition[1], color=line_coloring,
#                           lineType=line_type, thickness=2)
#     if showMode:
#         cv.imshow(name, screenshot)
#     return screenshot


# draw_rectangle_and_center_and_show(screenshot)



line_color = (255, 0, 255)
line_color_odd = (0,255,0)
line_type = cv.LINE_4
marker_color = (255, 0, 255)
marker_type = cv.MARKER_CROSS
marker_type_rectangle = cv.MARKER_SQUARE


championWidthList = []
championHeightList = []
markerPositionList = []

for i in range(0,len(championXmaxFoundInXMLList),1):
    championWidthList.append(championXmaxFoundInXMLList[i] - championXminFoundInXMLList[i])
    
    championHeightList.append(championYmaxFoundInXMLList[i] - championYminFoundInXMLList[i])


    topLeft = (championXminFoundInXMLList[i], championYminFoundInXMLList[i])
    bottomRight = (topLeft[0] + championWidthList[i], topLeft[1] + championHeightList[i])
    center = ((topLeft[0]+bottomRight[0])//2, (topLeft[1]+bottomRight[1])//2)

    markerPositionList.append([topLeft, bottomRight, center])



def draw_rectangle_and_center_and_show(screenshot, markerPosition=markerPositionList[0],line_coloring=line_color, showMode=1,name="wind"):
    cv.drawMarker(screenshot, markerPosition[2], color=line_coloring,
                  markerType=marker_type, markerSize=40, thickness=2)
    cv.rectangle(screenshot, markerPosition[0], markerPosition[1], color=line_coloring,
                          lineType=line_type, thickness=2)
    if showMode:
        cv.imshow(name, screenshot)
    return screenshot

for i in range(0,len(championXmaxFoundInXMLList),1):
    draw_rectangle_and_center_and_show(screenshot,markerPositionList[i])