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


# show avaliable apps names
WindowCapture.list_window_names()

wincap = WindowCapture('Spyder (Python 3.8)')

# wincap = None



###################################
####################################
##################################

line_color = (255, 0, 255)
line_type = cv.LINE_4
marker_color = (255, 0, 255)
marker_type = cv.MARKER_CROSS
marker_type_rectangle = cv.MARKER_SQUARE


championWidth = 128
championHeight = 128

topLeftStart = (256, 256)


topLeft = (topLeftStart[0], topLeftStart[0])
bottomRight = (topLeft[0] + championWidth, topLeft[0] + championHeight)
center = (topLeft[0] + championWidth//2, topLeft[1] + championHeight//2)

marker_position = [topLeft, bottomRight, center]

def make_ss_and_show(loadImage=0, window=wincap, croppingY=0, croppingX=0, croppingHeight=1080, croppingWidth=1920, showMode=0):
    if loadImage:
        screenshot = cv.imread("ss.jpg",cv.IMREAD_UNCHANGED)
    else:
        screenshot = window.get_screenshot()
    #print(screenshot)
    crop_img = screenshot[croppingY:croppingY+croppingHeight, croppingX:croppingX+croppingWidth]
    if showMode:
        cv.imshow("ss", crop_img)
    
    return crop_img


def draw_rectangle_and_center_and_show(screenshot, showMode=0):
    cv.drawMarker(screenshot, marker_position[2], color=line_color,
                  markerType=marker_type, markerSize=40, thickness=2)
    cv.rectangle(screenshot, marker_position[0], marker_position[1], color=line_color,
                         lineType=line_type, thickness=2)
    if showMode:
        cv.imshow("wind", screenshot)



draw_rectangle_and_center_and_show(make_ss_and_show(), 1)
    
