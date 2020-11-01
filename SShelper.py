# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 08:15:50 2020

@author: janusz
"""


"""
Make SS.
Crop it on champion tiles.
Save cropped images.
"""



import os
import cv2 as cv

from windowcapture import WindowCapture

import keyboard



# show avaliable apps names
WindowCapture.list_window_names()

# wincap = WindowCapture('Spyder (Python 3.8)')

# wincap = WindowCapture('League of Legends (TM) Client') 


wincap = None



###################################
####################################
##################################

line_color = (255, 0, 255)
line_color_odd = (0,255,0)
line_type = cv.LINE_4
marker_color = (255, 0, 255)
marker_type = cv.MARKER_CROSS
marker_type_rectangle = cv.MARKER_SQUARE


# FIRST WIDTH THEN HEIGHT

championWidth = 108
championHeight = 150

topLeftStart = [580, 130]


topLeft = (topLeftStart[0], topLeftStart[1])
bottomRight = (topLeft[0] + championWidth, topLeft[1] + championHeight)
center = ((topLeft[0]+bottomRight[0])//2, (topLeft[1]+bottomRight[1])//2)


marker_position = [topLeft, bottomRight, center]


basicSSname = 'C:\\Users\\janusz\\Pictures\\tft\\testingimages\\screen.jpg'


def make_ss_and_show(loadImage=1, window=wincap, croppingY=0, croppingX=0, croppingHeight=1080, croppingWidth=1920, showMode=0, saveMode=0, savingSSName=basicSSname):
    if loadImage:
        screenshot = cv.imread("C:\\Users\\janusz\\Documents\\TFT-DSS\\scren.jpg",cv.IMREAD_UNCHANGED)
    else:
        screenshot = window.get_screenshot()
    #print(screenshot)
    crop_img = screenshot[croppingY:croppingY+croppingHeight, croppingX:croppingX+croppingWidth]
    if showMode:
        cv.imshow("ss", crop_img)
    if saveMode:
        # while True:
        #     if keyboard.is_pressed("p"):
        #         print("You pressed p")
        #         break
        # screenshot = window.get_screenshot()
        # crop_img = screenshot[croppingY:croppingY+croppingHeight, croppingX:croppingX+croppingWidth]
        cv.imwrite(savingSSName, crop_img)
    
    return crop_img


def draw_rectangle_and_center_and_show(screenshot, markerPosition=marker_position,line_coloring=line_color, showMode=0,name="wind"):
    cv.drawMarker(screenshot, markerPosition[2], color=line_coloring,
                  markerType=marker_type, markerSize=40, thickness=2)
    cv.rectangle(screenshot, markerPosition[0], markerPosition[1], color=line_coloring,
                          lineType=line_type, thickness=2)
    if showMode:
        cv.imshow(name, screenshot)
    return screenshot




# need to add row offset because hexes in row arent in the same positions

rowOffset =[0,40,-20,25]
championWidthOffset = [0,5,7,11]

saving_marker_position = []

for row in range(0,4,1):
    for column in range(0,7,1):
        if row % 2 == 0:
            line_coloring = line_color
        else:
            line_coloring = line_color_odd
        
        topLeftStart = [520 + rowOffset[row]  + (championWidth + championWidthOffset[row]) * column, 290 + championHeight//2 * row]
        
        
        topLeft = (topLeftStart[0], topLeftStart[1])
        bottomRight = (topLeft[0] + championWidth, topLeft[1] + championHeight)
        center = ((topLeft[0]+bottomRight[0])//2, (topLeft[1]+bottomRight[1])//2)
        
        marker_position = [topLeft, bottomRight, center]
        saving_marker_position.append(marker_position)
        
        if column == 0 and row == 0:
            u=draw_rectangle_and_center_and_show(make_ss_and_show(showMode=0,saveMode=0),markerPosition=marker_position, line_coloring=line_coloring, showMode=0)
        else:
            u=draw_rectangle_and_center_and_show(u, markerPosition=marker_position, line_coloring=line_coloring, showMode=0)
        
        
        
u=draw_rectangle_and_center_and_show(u, markerPosition=saving_marker_position[4], line_coloring=line_color_odd, showMode=0)       

        

        
cv.imshow("window",u)



#### saving cropped images with single champion

for i,markerpos in enumerate(saving_marker_position):
    screenName='C:\\Users\\janusz\\Pictures\\tft\\testingimages\\name{:08}.jpg'.format(i)
    make_ss_and_show(croppingY=markerpos[0][1], croppingX=markerpos[0][0], croppingHeight=markerpos[1][1]-markerpos[0][1], croppingWidth=markerpos[1][0]-markerpos[0][0], saveMode=1, savingSSName=screenName)







# cv.imwrite('C:\\Users\\janusz\\Documents\\TFT-DSS\\screnUpdated.jpg',u)

# for row in range(0,4,1):
#     if row % 2 == 0:
#         line_coloring = line_color
#     else:
#         line_coloring = line_color_odd
    
#     topLeftStart = [490 , 300 + (championHeight//2) * row]
    
    
#     topLeft = (topLeftStart[0], topLeftStart[1])
#     bottomRight = (topLeft[0] + championWidth, topLeft[1] + championHeight)
#     center = ((topLeft[0]+bottomRight[0])//2, (topLeft[1]+bottomRight[1])//2)
    
#     marker_position = [topLeft, bottomRight, center]
    
#     if  row == 0:
#         u=draw_rectangle_and_center_and_show(make_ss_and_show(), line_coloring, 0)
#     else:
#         u=draw_rectangle_and_center_and_show(u, line_coloring, 0)
    
    
    
    
    
    
#     print(topLeftStart)
#     print(marker_position)
        
# cv.imshow("window",u)
