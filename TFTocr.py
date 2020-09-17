# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 07:45:36 2020

@author: Janusz
"""

import easyocr

import cv2 as cv
import numpy as np
import os
from time import time
from windowcapture import WindowCapture
from computerVision import Vision

import pandas as pd


# list of window names 
# WindowCapture.list_window_names()




df = pd.read_csv("scaledChampionsdf.csv") 

df.drop('Unnamed: 0', axis=1, inplace=True)
reader = easyocr.Reader(['en'])

            
for champ in df.Champion:
    print("'{}'".format(champ), end = ', ')
    
championListForOCR = ['Aatrox', 'Ahri', 'Akali', 'Annie', 'Aphelios', 'Ashe',
                      'Azir', 'Cassiopeia', 'Diana', 'Elise', 'Evelynn',
                      'Ezreal', 'Fiora', 'Garen', 'Hecarim', 'Irelia', 'Janna',
                      'JarvanIV', 'Jax', 'Jhin', 'Jinx', 'Kalista', 'Katarina',
                      'Kayn', 'Kennen', 'Kindred', 'LeeSin', 'Lillia', 'Lissandra',
                      'Lulu', 'Lux', 'Maokai', 'Morgana', 'Nami', 'Nidalee', 'Nunu',
                      'Pyke', 'Riven', 'Sejuani', 'Sett', 'Shen', 'Sylas', 'TahmKench',
                      'Talon', 'Teemo', 'Thresh', 'TwistedFate', 'Vayne', 'Veigar',
                      'Vi', 'Warwick', 'Wukong', 'XinZhao', 'Yasuo', 'Yone', 'Yuumi',
                      'Zed', 'Zilean']


def sort_detected_champions_to_buy_by_position(OCRResultsSorted):
    
    # sort from lowest width (left to right side)
    OCRResultsSorted = sorted(OCRResultsSorted, key=lambda x: x[0])
    sortedChampionsToBuy = []
    for text in OCRResultsSorted:
        for champ in championListForOCR:
            if champ in text:
                sortedChampionsToBuy.append(champ)
                print("found {}".format(champ))
    print("List of sorted champions to buy: ",sortedChampionsToBuy)
    return sortedChampionsToBuy 











































# Change the working directory to the folder this script is in.
# Doing this because I'll be putting the files from each video in their own folder on GitHub
os.chdir(os.path.dirname(os.path.abspath(__file__)))
#'League of Legends (TM) Client'

# initialize the WindowCapture class
wincap = WindowCapture('League of Legends (TM) Client')
# initialize the Vision class









# First champion card to buy on screen
xFirstChampionCard = 505
wChampionCard = 175
yFirstChampionCard = 865
hChampionCard = 135

PADDINGBETWEENCHAMPIONCARDS = 10

#drawing rectangles

line_color = (255, 0, 255)
line_type = cv.LINE_4
marker_color = (255, 0, 255)



screenshot = cv.imread("ss.jpg",cv.IMREAD_UNCHANGED)



# next card, indexing from 0 = most left side
def calculate_card_position_on_screen(cardIndex):
    xCard = xFirstChampionCard+ PADDINGBETWEENCHAMPIONCARDS * cardIndex + wChampionCard * cardIndex
    return xCard




def build_list_of_champion_cards_rectangles():
    cardsRectangles=[0]*5
    for i in range(0, 5):
        topLeft = (calculate_card_position_on_screen(i), yFirstChampionCard)
        bottomRight = (calculate_card_position_on_screen(i) + wChampionCard, yFirstChampionCard + hChampionCard)
        cardsRectangles[i] = [topLeft, bottomRight]
    return cardsRectangles


line_color = (255, 0, 255)
line_type = cv.LINE_4
marker_color = (255, 0, 255)


screenshot = cv.imread("ss.jpg",cv.IMREAD_UNCHANGED)

listOfRGBColours = [(0, 255, 0), (0, 0, 255), (0, 125, 125), (0, 125, 125), (0, 125, 125), (0, 125, 125)]




def make_cropped_ss_and_get_champions_to_buy(loadImage=0, window=wincap, croppingY=970, croppingX=450, croppingHeight=30, croppingWidth=1000):
    if loadImage:
        screenshot = cv.imread("ss.jpg",cv.IMREAD_UNCHANGED)
    else:
        screenshot = window.get_screenshot()
    #print(screenshot)
    crop_img = screenshot[croppingY:croppingY+croppingHeight, croppingX:croppingX+croppingWidth]
    #cv.imshow("ss", crop_img)
    OCRResult=reader.readtext(crop_img)
    # print(OCRResult)
    listOfChampsToBuyThisTurn=sort_detected_champions_to_buy_by_position(OCRResult)
    return listOfChampsToBuyThisTurn

















# colors need to be changed by amount of points

listOfRGBColours = [(0, 255, 0), (0, 0, 255), (0, 125, 125), (0, 125, 125), (0, 125, 125), (0, 125, 125)]


f=build_list_of_champion_cards_rectangles()
for i in range(0,5):
    u = cv.rectangle(screenshot, f[i][0], f[i][1], color=listOfRGBColours[i], lineType=line_type, thickness=2)
    cv.imshow("wind", u)











### real time loop
# while(True):

#     # get an updated image of the game
#     screenshot = wincap.get_screenshot()
#     crop_img = screenshot[y:y+h, x:x+w]
#     OCRResult=reader.readtext(crop_img)
#     listOfChampsToBuyThisTurn=sort_detected_champions_to_buy_by_position(OCRResult)
#     # display the processed image
#     # points = vision_ziggs3.find(screenshot, (0, 255, 0), 0.3, 'points')
#     cv.imshow("ss", crop_img)

#     # debug the loop rate
#     print('FPS {}'.format(1 / (time() - loop_time)))
#     loop_time = time()

#     # press 'q' with the output window focused to exit.
#     # waits 1 ms every loop to process key presses
#     if cv.waitKey(1) == ord('q'):
#         cv.destroyAllWindows()
#         break

# print('Done.')
