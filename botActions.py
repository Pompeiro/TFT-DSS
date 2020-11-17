# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 07:59:35 2020

@author: janusz
"""


"""0x10588 Spyder (Python 3.8)
0x10482 Python pyautogui window handle - Stack Overflow – Brave
0x50428 Eksplorator plików
0x20290 Discord
0x1041c CN=Microsoft Windows, O=Microsoft Corporation, L=Redmond, S=Washington, C=US
0x20408 Ustawienia
0x103fa 
0x30350 Kalkulator
0x110210 Kalkulator

Plan:
    OCR 
    Points
    Actions

"""
import pyautogui

import time

import mouseinfo


#########################################################################################################
########## OCR MODULE ##############################
#########################################################################################################

import easyocr
import cv2 as cv


championListForOCR = ['Aatrox', 'Elise', 'Evelynn', 'Jhin', 'Kalista', 'Pyke',
                      'Twisted Fate', 'Zilean', 'Jax', 'Lee Sin', 'Lux', 'Warwick',
                      'Wukong', 'Cassiopeia', 'Lillia', 'Riven', 'Thresh', 'Vayne',
                      'Ashe', 'Ezreal', 'Hecarim', 'Lulu', 'Maokai', 'Nunu',
                      'Veigar', 'Fiora', 'Irelia', 'Janna', 'Morgana', 'Nami',
                      'Talon', 'Yasuo', 'Yone', 'Annie', 'Jinx', 'Sejuani',
                      'Tahm Kench', 'Aphelios', 'Diana', 'Lissandra', 'Sylas',
                      'Akali', 'Kennen', 'Shen', 'Zed', 'Ahri', 'Kindred', 'Teemo',
                      'Yuumi', 'Sett', 'Kayn', 'Azir', 'Garen', 'Jarvan IV',
                      'Katarina', 'Nidalee', 'Vi', 'Xin Zhao']


reader = easyocr.Reader(['en'])

screenshot = cv.imread("ss.jpg",cv.IMREAD_UNCHANGED)

###################################### 
######################################
###### IF U WANT TEST WITHOUT GAME THEN COMMENT HERE
######################################
######################################




# wincap = WindowCapture('League of Legends (TM) Client')

wincap = None

def sort_detected_champions_to_buy_by_position(OCRResultsSorted):
    """
    
    Parameters
    ----------
    OCRResultsSorted : OCRresult not parsed

    Returns
    -------
    sortedChampionsToBuy : parsed champions list

    """
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


def make_cropped_ss_and_get_champions_to_buy(loadImage=1, window=wincap, croppingY=970, croppingX=450, croppingHeight=30, croppingWidth=1000):
    if loadImage:
        screenshot = cv.imread("ss.jpg",cv.IMREAD_UNCHANGED)
    else:
        screenshot = window.get_screenshot()
    #print(screenshot)
    crop_img = screenshot[croppingY:croppingY+croppingHeight, croppingX:croppingX+croppingWidth]
    cv.imshow("ss", crop_img)
    OCRResult=reader.readtext(crop_img)
    print(OCRResult)
    listOfChampsToBuyThisTurn=sort_detected_champions_to_buy_by_position(OCRResult)
    return listOfChampsToBuyThisTurn





def update_champions_to_buy_from_ocr_detection():
    listOfChampsToBuyThisTurn=make_cropped_ss_and_get_champions_to_buy()
    for champToBuy in listOfChampsToBuyThisTurn:
        for i,champ in enumerate(championListForOCR):
            if champToBuy == champ:
                print(i)
                print(champ)
                print("Succesfully added detected champion")
                break
    print("List of champions detected: ",listOfChampsToBuyThisTurn)            
    return listOfChampsToBuyThisTurn



#########################################################################################################
########## OCR MODULE END ##############################
#########################################################################################################


# pyautogui.getWindowsWithTitle("Spyder (Python 3.8)")[0].minimize()

# pyautogui.getWindowsWithTitle("Discord")[0].restore()

# time.sleep(2)

# pyautogui.getWindowsWithTitle("TFTDSS")[0].maximize()

TFTDSSwindow = pyautogui.getWindowsWithTitle("TFTDSS")[0]
TFTDSSwindow.minimize()
time.sleep(1)
TFTDSSwindow.restore()
TFTDSSwindow.activate()

# try:
#     pyautogui.getWindowsWithTitle("TFTDSS")[0].minimize()
#     time.sleep(1)
#     pyautogui.getWindowsWithTitle("TFTDSS")[0].restore()
# except:
#     pyautogui.getWindowsWithTitle("TFTDSS")[0].minimize()
#     time.sleep(1)
#     pyautogui.getWindowsWithTitle("TFTDSS")[0].activate()

# pyautogui.getWindowsWithTitle("TFTDSS")[0].restore()

# time.sleep(1)

pyautogui.click(x=850, y=450) ### first iteration with gui


# pyautogui.click(x=1010, y=450) ### after first iteration with gui

# 862,347 last champion on gui
# 699,347
# 535,346
# 376,346
# 211,346 first champion on gui



championToBuyPositionOnGUI = [ (210,345), (375,345), (535, 346), (700, 345), (860,345)]

championToBuyPositionOnGame = [ (600,975), (794,975), (984,975), (1173,975), (1363,975) ]

time.sleep(2)

try:
    TFTDSSwindow.restore()
    TFTDSSwindow.activate()
except:
    TFTDSSwindow.restore()


gameWindow = pyautogui.getWindowsWithTitle("wind")[0]

# for i in range(2,5,1):
#     time.sleep(1)
#     TFTDSSwindow.activate()
#     pyautogui.click(x=championToBuyPositionOnGUI[i][0], y=championToBuyPositionOnGUI[i][1])
#     time.sleep(1)
#     gameWindow.activate()
#     pyautogui.click(x=championToBuyPositionOnGame[i][0], y=championToBuyPositionOnGame[i][1])
    
    
    
def click_on_champion_to_buy_on_GUI_then_click_on_champion_in_game(positionOnGUI=0,positionInGame=0,GUIwindow=TFTDSSwindow,inGameWindow=gameWindow):
    time.sleep(1)
    GUIwindow.activate()
    pyautogui.click(x=championToBuyPositionOnGUI[positionOnGUI][0], y=championToBuyPositionOnGUI[positionOnGUI][1])
    time.sleep(1)
    inGameWindow.activate()
    pyautogui.click(x=championToBuyPositionOnGame[positionInGame][0], y=championToBuyPositionOnGame[positionInGame][1])

# 600,975 ## first champion to buy in game
# 794,975
# 984,975
# 1173,975
# 1363,975 ## last champion to buy in game


