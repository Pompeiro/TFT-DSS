# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 08:15:50 2020

@author: janusz
"""

# from PIL import ImageGrab
# snapshot = ImageGrab.grab()
# save_path = "C:\\Users\\janusz\\Pictures\\tft\\MySnapshot.jpg"
# snapshot.save(save_path)
import os
import cv2 as cv
# import os
# from time import time
from windowcapture import WindowCapture


# show avaliable apps names
WindowCapture.list_window_names()

wincap = WindowCapture('Spyder (Python 3.8)')

# wincap = None



###################################
####################################
##################################



def make_ss_and_show(loadImage=0, window=wincap, croppingY=0, croppingX=0, croppingHeight=1080, croppingWidth=1920):
    if loadImage:
        screenshot = cv.imread("ss.jpg",cv.IMREAD_UNCHANGED)
    else:
        screenshot = window.get_screenshot()
    #print(screenshot)
    crop_img = screenshot[croppingY:croppingY+croppingHeight, croppingX:croppingX+croppingWidth]
    cv.imshow("ss", crop_img)
    # OCRResult=reader.readtext(crop_img)
    # print(OCRResult)
    # listOfChampsToBuyThisTurn=sort_detected_champions_to_buy_by_position(OCRResult)
    # return listOfChampsToBuyThisTurn

make_ss_and_show()
    
# u=os.chdir(os.path.dirname(os.path.abspath(__file__)))
# print(u)
