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


