# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 10:54:45 2020

@author: Janusz
"""

import tkinter as tk
import tkinter.font as tkFont
# import random
# from functools import partial


# import collections
# from enum import IntEnum
# import operator



import pandas as pd


# import skfuzzy as fuzz
# from skfuzzy import control as ctrl
# import numpy as np

from collections import namedtuple

import pyautogui


import easyocr

import cv2 as cv
# import os
# from time import time
from windowcapture import WindowCapture
# from computerVision import Vision



import logging

logging.basicConfig(level=logging.DEBUG)

Champion = namedtuple("Champion", ["name", "nameOcr", "indexOcr", "champCounter", 
                                   "originPrim", "originSec", "classPrim", 
                                   "classSec", "originPrimCounter", "originSecCounter",
                                   "classPrimCounter", "classSecCounter"])


CARDSTOBUYAMOUNT = 5

pointsForChampionsToBuy = [0] * CARDSTOBUYAMOUNT

VARIABLEPRINTMODE = 0
# VARIABLEPRINTMODE = 1

# IMAGESDEBUGMODE = 0
IMAGESDEBUGMODE = 1

reader = easyocr.Reader(['en'])


###################################### 
######################################
###### IF U WANT TEST WITHOUT GAME THEN COMMENT HERE
######################################
######################################




# wincap = WindowCapture('League of Legends (TM) Client')

wincap = None



###################################
####################################
##################################

def add(intVariable):
    """Adding one to counter"""
    logging.debug("Function add() called")
    
    logging.info("input = {}".format(intVariable.get()))
    intVariable.set(intVariable.get() + 1)
    
    logging.info("after call = {}".format(intVariable.get()))
    logging.debug("Function add() end")


def sub(intVariable):
    """Minus one to counter"""
    logging.debug("Function sub() called")
    
    logging.info("input = {}".format(intVariable.get()))
    if intVariable.get() >0:
        intVariable.set(intVariable.get() - 1)

    logging.info("after call = {}".format(intVariable.get()))
    logging.debug("Function sub() end")









df = pd.read_csv("scaledChampionsdf.csv") 

df.drop('Unnamed: 0', axis=1, inplace=True)
df.Points = df["Points"].round(3)

originList = list(set(df.OriginPrimary)) + list(set(df.OriginSecondary))
originList = list(set(originList))
originList.remove("None")
originList.sort()

if VARIABLEPRINTMODE:
    for origin in originList:
        print(origin+"Champs = list(df.query("+"'OriginPrimary == "+'"'+"%s"%origin+'"'+"').Champion)")

if VARIABLEPRINTMODE:
    print("OriginChampsFromDFList = [", end = ' ')
    for origin in originList:
        print(origin+"Champs", end = ', ')
    print("]")  

CultistChamps = list(df.query('OriginPrimary == "Cultist"').Champion)
DivineChamps = list(df.query('OriginPrimary == "Divine"').Champion)
DuskChamps = list(df.query('OriginPrimary == "Dusk"').Champion)
ElderwoodChamps = list(df.query('OriginPrimary == "Elderwood"').Champion)
EnlightenedChamps = list(df.query('OriginPrimary == "Enlightened"').Champion)
ExileChamps = list(df.query('OriginPrimary == "Exile"').Champion)
FortuneChamps = list(df.query('OriginPrimary == "Fortune"').Champion)
MoonlightChamps = list(df.query('OriginPrimary == "Moonlight"').Champion)
NinjaChamps = list(df.query('OriginPrimary == "Ninja"').Champion)
SpiritChamps = list(df.query('OriginPrimary == "Spirit"').Champion)
TheBossChamps = list(df.query('OriginPrimary == "TheBoss"').Champion)
TormentedChamps = list(df.query('OriginPrimary == "Tormented"').Champion)
WarlordChamps = list(df.query('OriginPrimary == "Warlord"').Champion)

OriginChampsFromDFList = [CultistChamps, DivineChamps, DuskChamps, ElderwoodChamps,
                          EnlightenedChamps, ExileChamps, FortuneChamps,
                          MoonlightChamps, NinjaChamps, SpiritChamps, TheBossChamps,
                          TormentedChamps, WarlordChamps]

if VARIABLEPRINTMODE:
    for origin in originList:
        print(origin+"ChampsSecondary = list(df.query("+"'OriginSecondary == "+'"'+"%s"%origin+'"'+"').Champion)")

if VARIABLEPRINTMODE:
    print("OriginChampsSecondaryFromDFList = [", end = ' ')
    for origin in originList:
        print(origin+"ChampsSecondary", end = ', ')
    print("]") 


##################### !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
###################### manually replaced NoneChampsSecondary to the end
##################### !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
CultistChampsSecondary = list(df.query('OriginSecondary == "Cultist"').Champion)
DivineChampsSecondary = list(df.query('OriginSecondary == "Divine"').Champion)
DuskChampsSecondary = list(df.query('OriginSecondary == "Dusk"').Champion)
ElderwoodChampsSecondary = list(df.query('OriginSecondary == "Elderwood"').Champion)
EnlightenedChampsSecondary = list(df.query('OriginSecondary == "Enlightened"').Champion)
ExileChampsSecondary = list(df.query('OriginSecondary == "Exile"').Champion)
FortuneChampsSecondary = list(df.query('OriginSecondary == "Fortune"').Champion)
MoonlightChampsSecondary = list(df.query('OriginSecondary == "Moonlight"').Champion)
NinjaChampsSecondary = list(df.query('OriginSecondary == "Ninja"').Champion)
SpiritChampsSecondary = list(df.query('OriginSecondary == "Spirit"').Champion)
TheBossChampsSecondary = list(df.query('OriginSecondary == "TheBoss"').Champion)
TormentedChampsSecondary = list(df.query('OriginSecondary == "Tormented"').Champion)
WarlordChampsSecondary = list(df.query('OriginSecondary == "Warlord"').Champion)
NoneChampsSecondary = list(df.query('OriginSecondary == "None"').Champion)



##################### !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
###################### manually replaced NoneChampsSecondary to the end
##################### !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
OriginChampsSecondaryFromDFList = [CultistChampsSecondary, DivineChampsSecondary,
        DuskChampsSecondary, ElderwoodChampsSecondary, EnlightenedChampsSecondary,
        ExileChampsSecondary, FortuneChampsSecondary, MoonlightChampsSecondary,
        NinjaChampsSecondary, SpiritChampsSecondary, TheBossChampsSecondary,
        TormentedChampsSecondary, WarlordChampsSecondary, NoneChampsSecondary]



















classList = list(set(df.ClassPrimary))+list(set(df.ClassSecondary))
classList = list(set(classList))
classList.remove("None")
classList.sort()

if VARIABLEPRINTMODE:
    for clas in classList:
        print(clas+"Champs = list(df.query("+"'ClassPrimary == "+'"'+"%s"%clas+'"'+"').Champion)")
        ################################3
        #################################
        ###### Watch out to change ClassSecondary
        #################################
        #################################
if VARIABLEPRINTMODE:
    print("classChampsFromDFList = [", end = ' ')
    for clas in classList:
        print(clas+"Champs", end = ', ')
    print("]")  




AdeptChamps = list(df.query('ClassPrimary == "Adept"').Champion)
AssassinChamps = list(df.query('ClassPrimary == "Assassin"').Champion)
BrawlerChamps = list(df.query('ClassPrimary == "Brawler"').Champion)
DazzlerChamps = list(df.query('ClassPrimary == "Dazzler"').Champion)
DuelistChamps = list(df.query('ClassPrimary == "Duelist"').Champion)
EmperorChamps = list(df.query('ClassSecondary == "Emperor"').Champion)
HunterChamps = list(df.query('ClassPrimary == "Hunter"').Champion)
KeeperChamps = list(df.query('ClassPrimary == "Keeper"').Champion)
MageChamps = list(df.query('ClassPrimary == "Mage"').Champion)
MysticChamps = list(df.query('ClassPrimary == "Mystic"').Champion)
ShadeChamps = list(df.query('ClassPrimary == "Shade"').Champion)
SharpshooterChamps = list(df.query('ClassPrimary == "Sharpshooter"').Champion)
VanguardChamps = list(df.query('ClassPrimary == "Vanguard"').Champion)

classChampsFromDFList = [AdeptChamps, AssassinChamps, BrawlerChamps, DazzlerChamps,
                         DuelistChamps, EmperorChamps, HunterChamps, KeeperChamps,
                         MageChamps, MysticChamps, ShadeChamps, SharpshooterChamps,
                         VanguardChamps]






# OCR things

if VARIABLEPRINTMODE:
    print("championListForOCR = [", end = ' ')
    for champ in df.Champion:
        print("'"+champ+"'", end = ', ')
    print("]")  


championListForOCR = ['Aatrox', 'Elise', 'Evelynn', 'Jhin', 'Kalista', 'Pyke',
                      'Twisted Fate', 'Zilean', 'Jax', 'Lee Sin', 'Lux', 'Warwick',
                      'Wukong', 'Cassiopeia', 'Lillia', 'Riven', 'Thresh', 'Vayne',
                      'Ashe', 'Ezreal', 'Hecarim', 'Lulu', 'Maokai', 'Nunu & Willump',
                      'Veigar', 'Fiora', 'Irelia', 'Janna', 'Morgana', 'Nami',
                      'Talon', 'Yasuo', 'Yone', 'Annie', 'Jinx', 'Sejuani',
                      'Tahm Kench', 'Aphelios', 'Diana', 'Lissandra', 'Sylas',
                      'Akali', 'Kennen', 'Shen', 'Zed', 'Ahri', 'Kindred', 'Teemo',
                      'Yuumi', 'Sett', 'Kayn', 'Azir', 'Garen', 'Jarvan IV',
                      'Katarina', 'Nidalee', 'Vi', 'Xin Zhao']




#drawing rectangles things
# First champion card to buy on screen
    
xFirstChampionCard = 505
wChampionCard = 175
yFirstChampionCard = 865
hChampionCard = 135

PADDINGBETWEENCHAMPIONCARDS = 14

#drawing rectangles

line_color = (255, 0, 255)
line_type = cv.LINE_4
marker_color = (255, 0, 255)
marker_type = cv.MARKER_CROSS


listOfRGBColours = [(255, 0, 255), (0, 255, 255), (0, 255, 255), (0, 255, 255), (0, 255, 0)]

# listOfRGBColours = ["worst", "medium3", "medium2", "medium1", "best"]

# worst magenta mediums in yellow and best in green

# listOfRGBColours=range(0,5)
# next card, indexing from 0 = most left side



############### WINDOW THINGS

      

MainWindow = tk.Tk()
MainWindow.geometry('1900x800+0+0')
MainWindow.title('TFTDSS')



############### COUNTERS FOR HEARTS CARDS $$$$$$$$$$$$$$$$$$

if VARIABLEPRINTMODE:
    for champ in CultistChamps:
        print("counter"+champ+"= tk.IntVar()")
    
    print("CultistCounters = [")
    for champ in CultistChamps:
        print("counter"+champ,end = ", ")
    print("]")
    print()
        
    for champ in DivineChamps:
        print("counter"+champ+"= tk.IntVar()")
    
    print("DivineCounters = [")
    for champ in DivineChamps:
        print("counter"+champ,end = ", ")
    print("]")
    print()
    
        
    for champ in DuskChamps:
        print("counter"+champ+"= tk.IntVar()")
    
    print("DuskCounters = [")
    for champ in DuskChamps:
        print("counter"+champ,end = ", ")
    print("]")
    print()
    
        
    for champ in ElderwoodChamps:
        print("counter"+champ+"= tk.IntVar()")
    
    print("ElderwoodCounters = [")
    for champ in ElderwoodChamps:
        print("counter"+champ,end = ", ")
    print("]")
    print()
    
        
    for champ in EnlightenedChamps:
        print("counter"+champ+"= tk.IntVar()")
    
    print("EnlightenedCounters = [")
    for champ in EnlightenedChamps:
        print("counter"+champ,end = ", ")
    print("]")
    print()
    
        
    for champ in ExileChamps:
        print("counter"+champ+"= tk.IntVar()")
    
    print("ExileCounters = [")
    for champ in ExileChamps:
        print("counter"+champ,end = ", ")
    print("]")
    print()
    
        
    for champ in FortuneChamps:
        print("counter"+champ+"= tk.IntVar()")
    
    print("FortuneCounters = [")
    for champ in FortuneChamps:
        print("counter"+champ,end = ", ")
    print("]")
    print()
    
        
    for champ in MoonlightChamps:
        print("counter"+champ+"= tk.IntVar()")
    
    print("MoonlightCounters = [")
    for champ in MoonlightChamps:
        print("counter"+champ,end = ", ")
    print("]")
    print()
    
        
    for champ in NinjaChamps:
        print("counter"+champ+"= tk.IntVar()")
    
    print("NinjaCounters = [")
    for champ in NinjaChamps:
        print("counter"+champ,end = ", ")
    print("]")
    print()
    
        
    for champ in SpiritChamps:
        print("counter"+champ+"= tk.IntVar()")
    
    print("SpiritCounters = [")
    for champ in SpiritChamps:
        print("counter"+champ,end = ", ")
    print("]")
    print()
    
    
    for champ in TheBossChamps:
        print("counter"+champ+"= tk.IntVar()")
    
    print("TheBossCounters = [")
    for champ in TheBossChamps:
        print("counter"+champ,end = ", ")
    print("]")
    print()
    
    for champ in TormentedChamps:
        print("counter"+champ+"= tk.IntVar()")
    
    print("TormentedCounters = [")
    for champ in TormentedChamps:
        print("counter"+champ,end = ", ")
    print("]")
    print()
    
    for champ in WarlordChamps:
        print("counter"+champ+"= tk.IntVar()")
    
    print("WarlordCounters = [")
    for champ in WarlordChamps:
        print("counter"+champ,end = ", ")
    print("]")
    print()
    
    
    ################################ !!!!!!!!!!!!!!!!!!!!!!!!!!
    ############################### WARNING MESSAGE TO ADD MANUALLY these champs
    ################################ !!!!!!!!!!!!!!!!!!!!!!!!!!
    print("NEED TO MANUALLY WRTIE THESE CHAMPS INTO ORIGIN COUNTERS!!!!!!!!!\
          !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\
              !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\
                  counter should be declared only once !!!!!!!!! \n\
            add counter manually to the first appending Origin \
                          and delete duplicates manually!!!!!!!!!!!")
    for i,champ in enumerate(OriginChampsSecondaryFromDFList[0:-1]):
        if champ:
            print(originList[i])
            print(champ)
    
counterAatrox= tk.IntVar()
counterElise= tk.IntVar()
counterEvelynn= tk.IntVar()
counterJhin= tk.IntVar()
counterKalista= tk.IntVar()
counterPyke= tk.IntVar()
counterTwistedFate= tk.IntVar()
counterZilean= tk.IntVar()
CultistCounters = [counterAatrox, counterElise, counterEvelynn, counterJhin,
                   counterKalista, counterPyke, counterTwistedFate, counterZilean]


counterJax= tk.IntVar()
counterLeeSin= tk.IntVar()
counterLux= tk.IntVar()
counterWarwick= tk.IntVar()
counterWukong= tk.IntVar()

counterIrelia= tk.IntVar() 

DivineCounters = [counterJax, counterLeeSin, counterLux, counterWarwick, counterWukong, counterIrelia]

counterCassiopeia= tk.IntVar()
counterLillia= tk.IntVar()
counterRiven= tk.IntVar()
counterThresh= tk.IntVar()
counterVayne= tk.IntVar()
DuskCounters = [counterCassiopeia, counterLillia, counterRiven, counterThresh,
                counterVayne]

counterAshe= tk.IntVar()
counterEzreal= tk.IntVar()
counterHecarim= tk.IntVar()
counterLulu= tk.IntVar()
counterMaokai= tk.IntVar()
counterNunu= tk.IntVar()
counterVeigar= tk.IntVar()
ElderwoodCounters = [counterAshe, counterEzreal, counterHecarim, counterLulu,
                     counterMaokai, counterNunu, counterVeigar]

counterFiora= tk.IntVar()
# counterIrelia= tk.IntVar() 
counterJanna= tk.IntVar()
counterMorgana= tk.IntVar()
counterNami= tk.IntVar()
counterTalon= tk.IntVar()
EnlightenedCounters = [counterFiora, counterIrelia, counterJanna, counterMorgana,
                       counterNami, counterTalon]

counterYasuo= tk.IntVar()
counterYone= tk.IntVar()
ExileCounters = [counterYasuo, counterYone]

counterAnnie= tk.IntVar()
counterJinx= tk.IntVar()
counterSejuani= tk.IntVar()
counterTahmKench= tk.IntVar()

counterKatarina= tk.IntVar() 

FortuneCounters = [counterAnnie, counterJinx, counterSejuani, counterTahmKench, counterKatarina]

counterAphelios= tk.IntVar()
counterDiana= tk.IntVar()
counterLissandra= tk.IntVar()
counterSylas= tk.IntVar()
MoonlightCounters = [counterAphelios, counterDiana, counterLissandra, counterSylas]

counterAkali= tk.IntVar()
counterKennen= tk.IntVar()
counterShen= tk.IntVar()
counterZed= tk.IntVar()
NinjaCounters = [counterAkali, counterKennen, counterShen, counterZed]

counterAhri= tk.IntVar()
counterKindred= tk.IntVar()
counterTeemo= tk.IntVar()
counterYuumi= tk.IntVar()
SpiritCounters = [counterAhri, counterKindred, counterTeemo, counterYuumi]

counterSett= tk.IntVar()
TheBossCounters = [counterSett]

counterKayn= tk.IntVar()
TormentedCounters = [counterKayn]

counterAzir= tk.IntVar()
counterGaren= tk.IntVar()
counterJarvanIV= tk.IntVar()
# counterKatarina= tk.IntVar() 
counterNidalee= tk.IntVar()
counterVi= tk.IntVar()
counterXinZhao= tk.IntVar()
WarlordCounters = [counterAzir, counterGaren, counterJarvanIV, counterKatarina,
                   counterNidalee, counterVi, counterXinZhao]



####################### COUNTERS for champions to buy

counterBuyAatrox= tk.IntVar()
counterBuyElise= tk.IntVar()
counterBuyEvelynn= tk.IntVar()
counterBuyJhin= tk.IntVar()
counterBuyKalista= tk.IntVar()
counterBuyPyke= tk.IntVar()
counterBuyTwistedFate= tk.IntVar()
counterBuyZilean= tk.IntVar()
CultistCountersBuy = [counterBuyAatrox, counterBuyElise, counterBuyEvelynn, counterBuyJhin,
                   counterBuyKalista, counterBuyPyke, counterBuyTwistedFate, counterBuyZilean]

counterBuyJax= tk.IntVar()
counterBuyLeeSin= tk.IntVar()
counterBuyLux= tk.IntVar()
counterBuyWarwick= tk.IntVar()
counterBuyWukong= tk.IntVar()
DivineCountersBuy = [counterBuyJax, counterBuyLeeSin, counterBuyLux,
                     counterBuyWarwick, counterBuyWukong]

counterBuyCassiopeia= tk.IntVar()
counterBuyLillia= tk.IntVar()
counterBuyRiven= tk.IntVar()
counterBuyThresh= tk.IntVar()
counterBuyVayne= tk.IntVar()
DuskCountersBuy = [counterBuyCassiopeia, counterBuyLillia, counterBuyRiven,
                   counterBuyThresh, counterBuyVayne]

counterBuyAshe= tk.IntVar()
counterBuyEzreal= tk.IntVar()
counterBuyHecarim= tk.IntVar()
counterBuyLulu= tk.IntVar()
counterBuyMaokai= tk.IntVar()
counterBuyNunu= tk.IntVar()
counterBuyVeigar= tk.IntVar()
ElderwoodCountersBuy = [counterBuyAshe, counterBuyEzreal, counterBuyHecarim, counterBuyLulu,
                     counterBuyMaokai, counterBuyNunu, counterBuyVeigar]

counterBuyFiora= tk.IntVar()
counterBuyIrelia= tk.IntVar()
counterBuyJanna= tk.IntVar()
counterBuyMorgana= tk.IntVar()
counterBuyNami= tk.IntVar()
counterBuyTalon= tk.IntVar()
EnlightenedCountersBuy = [counterBuyFiora, counterBuyIrelia, counterBuyJanna, counterBuyMorgana,
                       counterBuyNami, counterBuyTalon]

counterBuyYasuo= tk.IntVar()
counterBuyYone= tk.IntVar()
ExileCountersBuy = [counterBuyYasuo, counterBuyYone]

counterBuyAnnie= tk.IntVar()
counterBuyJinx= tk.IntVar()
counterBuySejuani= tk.IntVar()
counterBuyTahmKench= tk.IntVar()
FortuneCountersBuy = [counterBuyAnnie, counterBuyJinx, counterBuySejuani,
                      counterBuyTahmKench]

counterBuyAphelios= tk.IntVar()
counterBuyDiana= tk.IntVar()
counterBuyLissandra= tk.IntVar()
counterBuySylas= tk.IntVar()
MoonlightCountersBuy = [counterBuyAphelios, counterBuyDiana, counterBuyLissandra, counterBuySylas]

counterBuyAkali= tk.IntVar()
counterBuyKennen= tk.IntVar()
counterBuyShen= tk.IntVar()
counterBuyZed= tk.IntVar()
NinjaCountersBuy = [counterBuyAkali, counterBuyKennen, counterBuyShen, counterBuyZed]

counterBuyAhri= tk.IntVar()
counterBuyKindred= tk.IntVar()
counterBuyTeemo= tk.IntVar()
counterBuyYuumi= tk.IntVar()
SpiritCountersBuy = [counterBuyAhri, counterBuyKindred, counterBuyTeemo, counterBuyYuumi]

counterBuySett= tk.IntVar()
TheBossCountersBuy = [counterBuySett]

counterBuyKayn= tk.IntVar()
TormentedCountersBuy = [counterBuyKayn]

counterBuyAzir= tk.IntVar()
counterBuyGaren= tk.IntVar()
counterBuyJarvanIV= tk.IntVar()
counterBuyKatarina= tk.IntVar()
counterBuyNidalee= tk.IntVar()
counterBuyVi= tk.IntVar()
counterBuyXinZhao= tk.IntVar()
WarlordCountersBuy = [counterBuyAzir, counterBuyGaren, counterBuyJarvanIV, counterBuyKatarina,
                   counterBuyNidalee, counterBuyVi, counterBuyXinZhao]













counterCultist= tk.IntVar()
counterDivine= tk.IntVar()
counterDusk= tk.IntVar()
counterElderwood= tk.IntVar()
counterEnlightened= tk.IntVar()
counterExile= tk.IntVar()
counterFortune= tk.IntVar()
counterMoonlight= tk.IntVar()
counterNinja= tk.IntVar()
counterSpirit= tk.IntVar()
counterTheBoss= tk.IntVar()
counterTormented= tk.IntVar()
counterWarlord= tk.IntVar()

OriginCounters = [counterCultist, counterDivine, counterDusk, counterElderwood,
                  counterEnlightened, counterExile, counterFortune, counterMoonlight,
                  counterNinja, counterSpirit, counterTheBoss, counterTormented,
                  counterWarlord]



OriginNames = sorted(list(set(df.OriginPrimary)))



if VARIABLEPRINTMODE:
    for clas in classList:
        print("counter"+clas+" = tk.IntVar()")


counterAdept = tk.IntVar()
counterAssassin = tk.IntVar()
counterBrawler = tk.IntVar()
counterDazzler = tk.IntVar()
counterDuelist = tk.IntVar()
counterEmperor = tk.IntVar()
counterHunter = tk.IntVar()
counterKeeper = tk.IntVar()
counterMage = tk.IntVar()
counterMystic = tk.IntVar()
counterShade = tk.IntVar()
counterSharpshooter = tk.IntVar()
counterVanguard = tk.IntVar()

if VARIABLEPRINTMODE:
    for i,clas in enumerate(classList):
        print(clas+"Counters = [ ")
        for champ in classChampsFromDFList[i]:
            print("counter"+champ,end = ", ")
        print("]")
        print()
            





AdeptCounters = [counterIrelia, counterShen, counterYone]

AssassinCounters = [counterAkali, counterDiana, counterKatarina, counterPyke, counterTalon]

BrawlerCounters = [counterMaokai, counterNunu, counterSett, counterSylas,
                   counterTahmKench, counterVi, counterWarwick]

DazzlerCounters = [counterEzreal, counterLissandra, counterLux, counterMorgana]

DuelistCounters = [counterFiora, counterJax, counterKalista, counterLeeSin,
                   counterXinZhao, counterYasuo]

EmperorCounters = [counterAzir]

HunterCounters = [counterAphelios, counterAshe, counterKindred, counterWarwick]

KeeperCounters = [counterAzir, counterElise, counterJarvanIV, counterKennen, counterRiven]

MageCounters = [counterAhri, counterAnnie, counterLillia, counterLulu, counterNami,
                counterTwistedFate, counterVeigar]

MysticCounters = [counterCassiopeia, counterJanna, counterShen, counterYuumi, counterZilean]

ShadeCounters = [counterEvelynn, counterKayn, counterZed]

SharpshooterCounters = [counterJhin, counterJinx, counterNidalee, counterTeemo, counterVayne]

VanguardCounters = [counterAatrox, counterGaren, counterHecarim, counterSejuani, counterThresh, counterWukong]

if VARIABLEPRINTMODE:
    print("ClassCounters = [")
    for clas in classList:
        print("counter"+clas,end = ", ")
    print("]")

ClassCounters = [counterAdept, counterAssassin, counterBrawler, counterDazzler,
                        counterDuelist, counterEmperor, counterHunter, counterKeeper,
                        counterMage, counterMystic, counterShade, counterSharpshooter,
                        counterVanguard]

if VARIABLEPRINTMODE:
    print("ClassCountersList = [")
    for clas in classList:
        print(clas+"Counters",end = ", ")
    print("]")

ClassCountersList = [AdeptCounters, AssassinCounters, BrawlerCounters,
                            DazzlerCounters, DuelistCounters, EmperorCounters,
                            HunterCounters, KeeperCounters, MageCounters, 
                            MysticCounters, ShadeCounters, SharpshooterCounters,
                            VanguardCounters]



############# manually added secondary counters

# ClassSecondaryNames = sorted(list(set(df.ClassSecondary)))


# ClassSecondaryCounters = [counterEmperor]
# print("ClassSecondaryCounters = [")
# for clas in ClassSecondaryNames:
#     print("counter" + clas, end = ", ")
# print("]")

# for clas in ClassSecondaryNames:
#     print("counter" + clas +" = tk.IntVar()")

Origin = namedtuple("Origin", ["Name", "Counter"])


Cultist = Origin(OriginNames[0], OriginCounters[0])












OriginChampsCountersList = [CultistCounters, DivineCounters, DuskCounters, 
                          ElderwoodCounters, EnlightenedCounters, ExileCounters, 
                          FortuneCounters, MoonlightCounters, NinjaCounters,
                          SpiritCounters, TheBossCounters, TormentedCounters, WarlordCounters]



OriginChampsCountersBuyList = [CultistCountersBuy, DivineCountersBuy, DuskCountersBuy, 
                          ElderwoodCountersBuy, EnlightenedCountersBuy, ExileCountersBuy, 
                          FortuneCountersBuy, MoonlightCountersBuy, NinjaCountersBuy,
                          SpiritCountersBuy, TheBossCountersBuy, TormentedCountersBuy,
                          WarlordCountersBuy]


ChampsNames  = sum(OriginChampsFromDFList, [])

OriginChampsCountersList1d = sum(OriginChampsCountersList, [])


if VARIABLEPRINTMODE:
    print("OriginChampsCountersListUseAsButtons = [")
    for champ in ChampsNames:
        print("counter"+champ,end = ", ")
    print("]")
    print()

OriginChampsCountersListUseAsButtons = [counterAatrox, counterElise, counterEvelynn,
                                        counterJhin, counterKalista, counterPyke,
                                        counterTwistedFate, counterZilean, counterJax,
                                        counterLeeSin, counterLux, counterWarwick,
                                        counterWukong, counterCassiopeia, counterLillia,
                                        counterRiven, counterThresh, counterVayne,
                                        counterAshe, counterEzreal, counterHecarim, counterLulu,
                                        counterMaokai, counterNunu, counterVeigar,
                                        counterFiora, counterIrelia, counterJanna,
                                        counterMorgana, counterNami, counterTalon,
                                        counterYasuo, counterYone, counterAnnie,
                                        counterJinx, counterSejuani, counterTahmKench,
                                        counterAphelios, counterDiana, counterLissandra,
                                        counterSylas, counterAkali, counterKennen,
                                        counterShen, counterZed, counterAhri,
                                        counterKindred, counterTeemo, counterYuumi,
                                        counterSett, counterKayn, counterAzir,
                                        counterGaren, counterJarvanIV, counterKatarina,
                                        counterNidalee, counterVi, counterXinZhao]    


if VARIABLEPRINTMODE:
    print("OriginChampsCountersToBuy = [")
    for champ in ChampsNames:
        print("counterBuy"+champ,end = ", ")
    print("]")
    print()

OriginChampsCountersToBuy = [counterBuyAatrox, counterBuyElise, counterBuyEvelynn,
                             counterBuyJhin, counterBuyKalista, counterBuyPyke,
                             counterBuyTwistedFate, counterBuyZilean, counterBuyJax,
                             counterBuyLeeSin, counterBuyLux, counterBuyWarwick,
                             counterBuyWukong, counterBuyCassiopeia, counterBuyLillia,
                             counterBuyRiven, counterBuyThresh, counterBuyVayne,
                             counterBuyAshe, counterBuyEzreal, counterBuyHecarim,
                             counterBuyLulu, counterBuyMaokai, counterBuyNunu,
                             counterBuyVeigar, counterBuyFiora, counterBuyIrelia,
                             counterBuyJanna, counterBuyMorgana, counterBuyNami,
                             counterBuyTalon, counterBuyYasuo, counterBuyYone,
                             counterBuyAnnie, counterBuyJinx, counterBuySejuani,
                             counterBuyTahmKench, counterBuyAphelios, counterBuyDiana,
                             counterBuyLissandra, counterBuySylas, counterBuyAkali,
                             counterBuyKennen, counterBuyShen, counterBuyZed,
                             counterBuyAhri, counterBuyKindred, counterBuyTeemo,
                             counterBuyYuumi, counterBuySett, counterBuyKayn,
                             counterBuyAzir, counterBuyGaren, counterBuyJarvanIV,
                             counterBuyKatarina, counterBuyNidalee, counterBuyVi,
                             counterBuyXinZhao]



# OriginChampsCountersList1d.pop(12)
# OriginChampsCountersList1d.pop()
# OriginChampsCountersList1d.pop()


CHAMPIONFLAG =1
ORIGINFLAG =0



######### order as in GUI
df.sort_values(by=['OriginPrimary', 'Champion'], inplace = True)
df.reset_index(drop=True, inplace = True)

boldedFont = tkFont.Font(family="Arial", size=10, weight=tkFont.BOLD)

championInfo = [] 
logging.debug("Filling championInfo in purpose of creating namedtuple")
for i,champ in enumerate(df.Champion):
    championInfo.append([champ, championListForOCR[i], i,
                OriginChampsCountersListUseAsButtons[i], df.OriginPrimary[i],
                df.OriginSecondary[i], df.ClassPrimary[i], df.ClassSecondary[i]])
logging.debug("First filling championInfo has ended.")   
    


championToBuyInfo = [] 
logging.debug("Filling championToBuyInfo in purpose of creating namedtuple")
for i,champ in enumerate(df.Champion):
    championToBuyInfo.append([champ, championListForOCR[i], i,
                OriginChampsCountersToBuy[i], df.OriginPrimary[i],
                df.OriginSecondary[i], df.ClassPrimary[i], df.ClassSecondary[i]])
logging.debug("First filling championToBuyInfo has ended.")   


def filling_list_with_counter_for_namedtuple(fieldToCheck, inputList=championInfo):
    """
    

    Parameters
    ----------
    fieldToCheck : {4:"originPrim", 5:"originSec", 6:"classPrim",
                           7:"classSec"}
    inputList : List with 4,5,6,7 field == fieldToCheck. The default is championInfo.

    Returns
    -------
    listOfCounters : List of GUI counters

    """
    logging.debug("Function filling_list_with_counter_for_namedtuple() called")
    fieldToCheck2String = {4:"originPrim", 5:"originSec", 6:"classPrim",
                           7:"classSec"}
    fieldToCheck2CheckList = {4:originList, 5:originList, 6:classList, 7:classList}
    fieldToCheck2CheckListString = {4:"originList", 5:"originList", 6:"classList", 7:"classList"}
    fieldToCheck2CountersList = {4:OriginCounters, 5:OriginCounters, 6:ClassCounters, 7:ClassCounters}
    listOfCounters = [None] * len(df.Champion)
    for i,champ in enumerate(df.Champion):
        if inputList[i][fieldToCheck] == "None":
            logging.info("Champion name: {}, champion index = {}".format(champ,i))
            logging.info("Field with index {} == 'NONE' filling None as {}Counter".format(fieldToCheck, 
                                                                                            fieldToCheck2String[fieldToCheck]))
            listOfCounters[i] = None
        else:
            logging.info("{} IS NOT 'NONE'".format(fieldToCheck2String[fieldToCheck]))
            for j,classOrOrigin in enumerate(fieldToCheck2CheckList[fieldToCheck]):
                if inputList[i][fieldToCheck] == classOrOrigin:
                    logging.info("Champion name: {}, champion index = {}".format(champ,i))
                    logging.info("Found match in champion {} and {} for : {}".format(fieldToCheck2String[fieldToCheck],
                                                                                     fieldToCheck2CheckListString[fieldToCheck],
                                                                                            classOrOrigin))
                    logging.info("Filling {} counter: {}".format(fieldToCheck2String[fieldToCheck],
                                                                 fieldToCheck2CountersList[fieldToCheck][j]))
                    listOfCounters[i] = fieldToCheck2CountersList[fieldToCheck][j]
    logging.debug("Function filling_list_with_counter_for_namedtuple() end")
    return listOfCounters

def append_counters_to_input_list(inputList=championInfo):
    """
    

    Parameters
    ----------
    inputList : Appending counters to list with fields like {4:"originPrim", 
    5:"originSec", 6:"classPrim", 7:"classSec"}. The default is championInfo.

    Returns
    -------
    None.

    """
    
    logging.debug("Function filling_list_with_counter_for_namedtuple() called")

    countersToAppend = [4, 5, 6, 7]
    for j in countersToAppend:
        listOfCountersToAppend = filling_list_with_counter_for_namedtuple(j, inputList)
        for i,champ in enumerate(inputList):
            champ.append(listOfCountersToAppend[i])
    
    logging.debug("Function filling_list_with_counter_for_namedtuple() end")

    return None

append_counters_to_input_list(championInfo)

append_counters_to_input_list(championToBuyInfo)

championInfoDF = pd.DataFrame.from_records(championInfo, columns=['Champion','nameOcr',
                                                                  'indexOcr','champCounter',
                           'originPrim', "originSec", "classPrim", "classSec",
                           "originPrimCounter", "originSecCounter", "classPrimCounter",
                           "classSecCounter"])

championToBuyInfoDF = pd.DataFrame.from_records(championInfo, columns=['Champion','nameOcr',
                                                                  'indexOcr','champCounter',
                           'originPrim', "originSec", "classPrim", "classSec",
                           "originPrimCounter", "originSecCounter", "classPrimCounter",
                           "classSecCounter"])


if VARIABLEPRINTMODE:
    for i,champ in enumerate(championInfo):
        print(champ[0] + ' = Champion(*championInfo[%d])'%i)

Aatrox = Champion(*championInfo[0])
Elise = Champion(*championInfo[1])
Evelynn = Champion(*championInfo[2])
Jhin = Champion(*championInfo[3])
Kalista = Champion(*championInfo[4])
Pyke = Champion(*championInfo[5])
TwistedFate = Champion(*championInfo[6])
Zilean = Champion(*championInfo[7])
Jax = Champion(*championInfo[8])
LeeSin = Champion(*championInfo[9])
Lux = Champion(*championInfo[10])
Warwick = Champion(*championInfo[11])
Wukong = Champion(*championInfo[12])
Cassiopeia = Champion(*championInfo[13])
Lillia = Champion(*championInfo[14])
Riven = Champion(*championInfo[15])
Thresh = Champion(*championInfo[16])
Vayne = Champion(*championInfo[17])
Ashe = Champion(*championInfo[18])
Ezreal = Champion(*championInfo[19])
Hecarim = Champion(*championInfo[20])
Lulu = Champion(*championInfo[21])
Maokai = Champion(*championInfo[22])
Nunu = Champion(*championInfo[23])
Veigar = Champion(*championInfo[24])
Fiora = Champion(*championInfo[25])
Irelia = Champion(*championInfo[26])
Janna = Champion(*championInfo[27])
Morgana = Champion(*championInfo[28])
Nami = Champion(*championInfo[29])
Talon = Champion(*championInfo[30])
Yasuo = Champion(*championInfo[31])
Yone = Champion(*championInfo[32])
Annie = Champion(*championInfo[33])
Jinx = Champion(*championInfo[34])
Sejuani = Champion(*championInfo[35])
TahmKench = Champion(*championInfo[36])
Aphelios = Champion(*championInfo[37])
Diana = Champion(*championInfo[38])
Lissandra = Champion(*championInfo[39])
Sylas = Champion(*championInfo[40])
Akali = Champion(*championInfo[41])
Kennen = Champion(*championInfo[42])
Shen = Champion(*championInfo[43])
Zed = Champion(*championInfo[44])
Ahri = Champion(*championInfo[45])
Kindred = Champion(*championInfo[46])
Teemo = Champion(*championInfo[47])
Yuumi = Champion(*championInfo[48])
Sett = Champion(*championInfo[49])
Kayn = Champion(*championInfo[50])
Azir = Champion(*championInfo[51])
Garen = Champion(*championInfo[52])
JarvanIV = Champion(*championInfo[53])
Katarina = Champion(*championInfo[54])
Nidalee = Champion(*championInfo[55])
Vi = Champion(*championInfo[56])
XinZhao = Champion(*championInfo[57])


if VARIABLEPRINTMODE:
    print("championsList = [")
    for champ in championInfo:
        print(champ[0],end = ", ")
    print("]")
    print()


championsList = [Aatrox, Elise, Evelynn, Jhin, Kalista, Pyke, TwistedFate,
                 Zilean, Jax, LeeSin, Lux, Warwick, Wukong, Cassiopeia,
                 Lillia, Riven, Thresh, Vayne, Ashe, Ezreal, Hecarim,
                 Lulu, Maokai, Nunu, Veigar, Fiora, Irelia, Janna,
                 Morgana, Nami, Talon, Yasuo, Yone, Annie, Jinx, Sejuani,
                 TahmKench, Aphelios, Diana, Lissandra, Sylas, Akali,
                 Kennen, Shen, Zed, Ahri, Kindred, Teemo, Yuumi,
                 Sett, Kayn, Azir, Garen, JarvanIV, Katarina, Nidalee,
                 Vi, XinZhao]


if VARIABLEPRINTMODE:
    for i,champ in enumerate(championToBuyInfo):
        print(champ[0]+"ToBuy" + ' = Champion(*championToBuyInfo[%d])'%i)

AatroxToBuy = Champion(*championToBuyInfo[0])
EliseToBuy = Champion(*championToBuyInfo[1])
EvelynnToBuy = Champion(*championToBuyInfo[2])
JhinToBuy = Champion(*championToBuyInfo[3])
KalistaToBuy = Champion(*championToBuyInfo[4])
PykeToBuy = Champion(*championToBuyInfo[5])
TwistedFateToBuy = Champion(*championToBuyInfo[6])
ZileanToBuy = Champion(*championToBuyInfo[7])
JaxToBuy = Champion(*championToBuyInfo[8])
LeeSinToBuy = Champion(*championToBuyInfo[9])
LuxToBuy = Champion(*championToBuyInfo[10])
WarwickToBuy = Champion(*championToBuyInfo[11])
WukongToBuy = Champion(*championToBuyInfo[12])
CassiopeiaToBuy = Champion(*championToBuyInfo[13])
LilliaToBuy = Champion(*championToBuyInfo[14])
RivenToBuy = Champion(*championToBuyInfo[15])
ThreshToBuy = Champion(*championToBuyInfo[16])
VayneToBuy = Champion(*championToBuyInfo[17])
AsheToBuy = Champion(*championToBuyInfo[18])
EzrealToBuy = Champion(*championToBuyInfo[19])
HecarimToBuy = Champion(*championToBuyInfo[20])
LuluToBuy = Champion(*championToBuyInfo[21])
MaokaiToBuy = Champion(*championToBuyInfo[22])
NunuToBuy = Champion(*championToBuyInfo[23])
VeigarToBuy = Champion(*championToBuyInfo[24])
FioraToBuy = Champion(*championToBuyInfo[25])
IreliaToBuy = Champion(*championToBuyInfo[26])
JannaToBuy = Champion(*championToBuyInfo[27])
MorganaToBuy = Champion(*championToBuyInfo[28])
NamiToBuy = Champion(*championToBuyInfo[29])
TalonToBuy = Champion(*championToBuyInfo[30])
YasuoToBuy = Champion(*championToBuyInfo[31])
YoneToBuy = Champion(*championToBuyInfo[32])
AnnieToBuy = Champion(*championToBuyInfo[33])
JinxToBuy = Champion(*championToBuyInfo[34])
SejuaniToBuy = Champion(*championToBuyInfo[35])
TahmKenchToBuy = Champion(*championToBuyInfo[36])
ApheliosToBuy = Champion(*championToBuyInfo[37])
DianaToBuy = Champion(*championToBuyInfo[38])
LissandraToBuy = Champion(*championToBuyInfo[39])
SylasToBuy = Champion(*championToBuyInfo[40])
AkaliToBuy = Champion(*championToBuyInfo[41])
KennenToBuy = Champion(*championToBuyInfo[42])
ShenToBuy = Champion(*championToBuyInfo[43])
ZedToBuy = Champion(*championToBuyInfo[44])
AhriToBuy = Champion(*championToBuyInfo[45])
KindredToBuy = Champion(*championToBuyInfo[46])
TeemoToBuy = Champion(*championToBuyInfo[47])
YuumiToBuy = Champion(*championToBuyInfo[48])
SettToBuy = Champion(*championToBuyInfo[49])
KaynToBuy = Champion(*championToBuyInfo[50])
AzirToBuy = Champion(*championToBuyInfo[51])
GarenToBuy = Champion(*championToBuyInfo[52])
JarvanIVToBuy = Champion(*championToBuyInfo[53])
KatarinaToBuy = Champion(*championToBuyInfo[54])
NidaleeToBuy = Champion(*championToBuyInfo[55])
ViToBuy = Champion(*championToBuyInfo[56])
XinZhaoToBuy = Champion(*championToBuyInfo[57])


if VARIABLEPRINTMODE:
    print("championsToBuyList = [")
    for champ in championToBuyInfo:
        print(champ[0]+"ToBuy",end = ", ")
    print("]")
    print()


championsToBuyList = [AatroxToBuy, EliseToBuy, EvelynnToBuy, JhinToBuy,
                      KalistaToBuy, PykeToBuy, TwistedFateToBuy, ZileanToBuy,
                      JaxToBuy, LeeSinToBuy, LuxToBuy, WarwickToBuy, WukongToBuy,
                      CassiopeiaToBuy, LilliaToBuy, RivenToBuy, ThreshToBuy,
                      VayneToBuy, AsheToBuy, EzrealToBuy, HecarimToBuy, LuluToBuy,
                      MaokaiToBuy, NunuToBuy, VeigarToBuy, FioraToBuy, IreliaToBuy,
                      JannaToBuy, MorganaToBuy, NamiToBuy, TalonToBuy, YasuoToBuy,
                      YoneToBuy, AnnieToBuy, JinxToBuy, SejuaniToBuy, TahmKenchToBuy,
                      ApheliosToBuy, DianaToBuy, LissandraToBuy, SylasToBuy, AkaliToBuy,
                      KennenToBuy, ShenToBuy, ZedToBuy, AhriToBuy, KindredToBuy,
                      TeemoToBuy, YuumiToBuy, SettToBuy, KaynToBuy, AzirToBuy,
                      GarenToBuy, JarvanIVToBuy, KatarinaToBuy, NidaleeToBuy,
                      ViToBuy, XinZhaoToBuy]



def sort_detected_champions_to_buy_by_position(OCRResultsSorted):
    """
    
    Sorting input in order from left to right by placement on the screen
    (lowest width is first).Then filters out champion names, numbers(champions cost)
    are discarded.

    Parameters
    ----------
    OCRResultsSorted : Typical == ocr_on_cropped_img(make_cropped_ss())

    Returns
    -------
    sortedChampionsToBuy : List of champions that were found in input.

    """
    
    logging.debug("Function sort_detected_champions_to_buy_by_position() called")
    # sort from lowest width (left to right side)
    OCRResultsSorted = sorted(OCRResultsSorted, key=lambda x: x[0])
    sortedChampionsToBuy = []
    for text in OCRResultsSorted:
        for champ in championListForOCR:
            if champ in text: # filters champion names
                sortedChampionsToBuy.append(champ)
                logging.info("from for loop in sort_detected_champions_to_buy_by_position()")
                logging.info("found {}".format(champ))
    logging.info("return in sort_detected_champions_to_buy_by_position()")
    logging.info("List of sorted champions to buy: {}".format(sortedChampionsToBuy))
    
    logging.debug("Function sort_detected_champions_to_buy_by_position() end")
    return sortedChampionsToBuy 



def make_cropped_ss(loadImage=1, window=wincap, croppingX=450, croppingY=970, croppingWidth=1000, croppingHeight=30):
    """
    

    Parameters
    ----------
    loadImage : If want to open without game then change to 1. 
        The default is 0.
    window : Window to be captured, set to None if want to open without game.
        The default is wincap.
        
        Defaults to cropp screenshot from first to fifth(1-5) champion card name.
    croppingX :  The default is 450. 
    croppingY :  The default is 970.
    croppingWidth :  The default is 1000.
    croppingHeight :  The default is 30.

    Returns
    -------
    crop_img : Cropped screenshot.

    """
    logging.debug("Function make_cropped_ss() called")

    if loadImage:
        screenshot = cv.imread("ss.jpg",cv.IMREAD_UNCHANGED)
    else:
        screenshot = window.get_screenshot()
    crop_img = screenshot[croppingY:croppingY+croppingHeight, croppingX:croppingX+croppingWidth]
    
    if IMAGESDEBUGMODE:
        cv.imshow("make_cropped_ss()", crop_img)
    
    logging.debug("Function make_cropped_ss() end")
    return crop_img,screenshot


def ocr_on_cropped_img(croppedSSWithChampionCardNames):
    """
    

    Parameters
    ----------
    croppedSSWithChampionCardNames : for example if want to OCR card names then
    input there make_cropped_ss(loadImage=0, window=wincap, croppingX=450,
                                croppingY=970, croppingWidth=1000, croppingHeight=30)

    Returns
    -------
    OCRResult : 

    """
    logging.debug("Function ocr_on_cropped_img() called")


    OCRResult=reader.readtext(croppedSSWithChampionCardNames)
    logging.info("OCR results(return): {}".format(OCRResult))
    
    logging.debug("Function ocr_on_cropped_img() end")
    return OCRResult


def update_champions_to_buy_from_ocr_detection():
    """
    Add 1 to every champion to buy counter detected in OCRResults.
    champion to buy counters GLOBAL STATE CHANGE !!!!!!!!!!!!!!!!!!!!

    Returns
    -------
    None.

    """
    logging.debug("Function update_champions_to_buy_from_ocr_detection() called")

    listOfChampsToBuyThisTurn=sort_detected_champions_to_buy_by_position(ocr_on_cropped_img(make_cropped_ss()[0]))
    for champToBuy in listOfChampsToBuyThisTurn:
        for i,champ in enumerate(championListForOCR):
            if champToBuy == champ:
                logging.info("from IF inside for loop in update_champions_to_buy_from_ocr_detection()")
                logging.info("Index in championListForOCR that is detected: {}".format(i))
                logging.info("Champ name in this index: {}".format(champ))
                add(OriginChampsCountersToBuy[i])
                break
    
    logging.debug("Function update_champions_to_buy_from_ocr_detection() end")         
    return listOfChampsToBuyThisTurn



def calculate_card_position_on_screen(cardIndex):
    """
    

    Parameters
    ----------
    cardIndex : simply from 0-4(first to fifth card)

    Returns
    -------
    xCard : x Position on the screen of the top left corner for card

    """
    logging.debug("Function calculate_card_position_on_screen() called")

    xCard = xFirstChampionCard + PADDINGBETWEENCHAMPIONCARDS * cardIndex + wChampionCard * cardIndex
    logging.info("X coord of card with index= {} is: {}".format(cardIndex, xCard))
    logging.debug("Function calculate_card_position_on_screen() end")         
    return xCard

def build_list_of_champion_cards_rectangles():
    logging.debug("Function build_list_of_champion_cards_rectangles() called")

    
    cardsRectangles=[0]*CARDSTOBUYAMOUNT
    for i in range(0, CARDSTOBUYAMOUNT):
        topLeft = (calculate_card_position_on_screen(i), yFirstChampionCard)
        bottomRight = (calculate_card_position_on_screen(i) + wChampionCard, yFirstChampionCard + hChampionCard)
        center = (topLeft[0] + wChampionCard//2, topLeft[1] + hChampionCard//2)
        # print("Type" ,type(center))
        cardsRectangles[i] = [topLeft, bottomRight, center]
        
    logging.debug("Function build_list_of_champion_cards_rectangles() end")         
    return cardsRectangles



# https://stackoverflow.com/questions/6618515/sorting-list-based-on-values-from-another-list
def draw_on_champion_to_buy_cards(colors=listOfRGBColours, mode="points"):
    """
    This function is making OCR detection on champion cards, and then draws by
    input mode like default points on screenshot.

    Parameters
    ----------
    colors : ["worst", "medium3", "medium2", "medium1", "best"]. list of RGB tuples.
    The default is listOfRGBColours.
    mode :  The default is "points". Also there are cross and rectangle.

    Returns
    -------
    None.

    """
    logging.debug("Function draw_on_champion_to_buy_cards() called")

    championsToBuyInOrderAsInScreen = update_champions_to_buy_from_ocr_detection()
    championsToBuyPointsAndPosition=show_nonzero_counters_with_points()
    
    championsPositionToBuyOrderedByScreen = [championListForOCR.index(i) for i in championsToBuyInOrderAsInScreen]
    logging.info("championsPositionToBuyOrderedByScreen: {}".format(championsPositionToBuyOrderedByScreen))
    
    championsToBuyPoints = list(zip(*championsToBuyPointsAndPosition))[0]
    championsToBuyPosition = list(zip(*championsToBuyPointsAndPosition))[1]
    logging.info("Points (in alphabetical by champ name order?): {}".format(championsToBuyPoints))
    logging.info("Champions position (in alphabetical by champ name order?): {}".format(championsToBuyPosition))
    sortedChampionsToBuyPointsAndPosition = sorted(championsToBuyPointsAndPosition)
    logging.info("Points and Champions position (in alphabetical by champ name order?): {}".format(sortedChampionsToBuyPointsAndPosition))
    sortedChampionsToBuyPosition = list(zip(*sortedChampionsToBuyPointsAndPosition))[1]
    logging.info("sortedChampionsToBuyPosition in alphabetical order?: {}".format(sortedChampionsToBuyPosition))
    valuesByPointsIndexesOrderByPositionOnScreen = [sortedChampionsToBuyPosition.index(i) for i in championsPositionToBuyOrderedByScreen]
    logging.info("valuesByPointsIndexesOrderByPositionOnScreen 0 worst card 4 best card: {}".format(valuesByPointsIndexesOrderByPositionOnScreen))
    cardsRectangles=build_list_of_champion_cards_rectangles()
    screenshot = wincap.get_screenshot()
    # screenshot = cv.imread("ss.jpg",cv.IMREAD_UNCHANGED)
    
    ##### at the end
    # valuesByPointsIndexesOrderByPositionOnScreen contains champions 
    # sorted by points from lowest(0) to highest(4) 
    # and indexes represents champion placement on the screen

    if mode == "rectangle":
        for i in range(0,CARDSTOBUYAMOUNT):
            cv.rectangle(screenshot, cardsRectangles[i][0], cardsRectangles[i][1], color=colors[valuesByPointsIndexesOrderByPositionOnScreen[i]],
                          lineType=line_type, thickness=2)
        cv.imshow("draw_on_champion_to_buy_cards()", screenshot)
    elif mode == "cross":
        for i in range(0,CARDSTOBUYAMOUNT):
                    # Draw the center point
            cv.drawMarker(screenshot, cardsRectangles[i][2], color=colors[valuesByPointsIndexesOrderByPositionOnScreen[i]],
                          markerType=marker_type, markerSize=40, thickness=2)
        cv.imshow("draw_on_champion_to_buy_cards()", screenshot)
    elif mode == "points":
        for i in range(0,CARDSTOBUYAMOUNT):
                    # Draw the center point
                cv.putText(screenshot, "{:.3f}".format(sortedChampionsToBuyPointsAndPosition[valuesByPointsIndexesOrderByPositionOnScreen[i]][0]),
                           cardsRectangles[i][2], cv.FONT_HERSHEY_SIMPLEX, 0.6, colors[valuesByPointsIndexesOrderByPositionOnScreen[i]], 2)
        cv.imshow("draw_on_champion_to_buy_cards()", screenshot)
        
    logging.debug("Function draw_on_champion_to_buy_cards() end")         
    return None



######## need to fix double calculate points inside draw_on_champion_to_buy_cards
def draw_rectangles_show_points_show_buttons_reset_counters():
    logging.debug("Function draw_rectangles_show_points_show_buttons_reset_counters() called")

    update_classes_and_origins()
    try:
        reset_counters_in_list(OriginChampsCountersToBuy)
    except :
        pass
    draw_on_champion_to_buy_cards()

    logging.debug("Function draw_rectangles_show_points_show_buttons_reset_counters() end")         




            
            

def show_champions_from_origin(originPositionInOriginList, OriginChampsFromDF, OriginCounterList, shiftBetweenUpsideDownside, flag = CHAMPIONFLAG):
    """Adding buttons and text labels for single origin.
    In: originPositionInOriginList - its used to pickup origin from originlist,
    and place text on the window.
    OriginChampsFromDF  - list of champions in origin.
    OriginCounterList - list of champions counters in origin.
    shiftBetweenUpsideDownside - placing on the window, UPSIDE is upper location,
    DOWNSIDE is lower location.
    flag - if 1 then text label is above counters, for origin champions should 
    be CHAMPIONFLAG, for origins or classes should be ORIGINFLAG.
        """
    logging.debug("Function show_champions_from_origin() called")
    
    if flag == 1:
        labelTitle = tk.Label(MainWindow, text=originList[originPositionInOriginList]).grid(row=1+shiftBetweenUpsideDownside, column=OriginLabelPositionColumn*ShiftBetweenOrigins*originPositionInOriginList)

    for i,champ in enumerate(OriginChampsFromDF):
        labelTitle = tk.Label(MainWindow, text=champ).grid(row=2+i+shiftBetweenUpsideDownside, column=OriginLabelPositionColumn*ShiftBetweenOrigins*originPositionInOriginList)
        entryNum = tk.Entry(MainWindow, textvariable=OriginCounterList[i], width = 2).grid(row=2+i+shiftBetweenUpsideDownside, column=ShiftBetweenOrigins*originPositionInOriginList+1)
        buttonCal = tk.Button(MainWindow, text="+", command=lambda counter=OriginCounterList[i]:add(counter)).grid(row=2+i+shiftBetweenUpsideDownside, column=ShiftBetweenOrigins*originPositionInOriginList+2)
        buttonCal = tk.Button(MainWindow, text="-", command=lambda counter=OriginCounterList[i]:sub(counter)).grid(row=2+i+shiftBetweenUpsideDownside, column=ShiftBetweenOrigins*originPositionInOriginList+3)
   
    logging.debug("Function show_champions_from_origin() end")    
    return





def reset_counters_in_list(list1d=OriginChampsCountersToBuy):
    """Reset counters to 0, used when roll or new round starts.
    In: list1d by default its OriginChampsCountersToBuy."""
    logging.debug("Function reset_counters_in_list() called")

    for champCounter in list1d:
        champCounter.set(0)
        
    delete_all_buttons()
    
    logging.debug("Function reset_counters_in_list() end")  
    return

def check_nonzero_counters(list1d=OriginChampsCountersToBuy):
    """Check how much champion counters are nonzero.
    IF ladder to append repetitions to list.
    In: list1d by default its OriginChampsCountersToBuy.
    Out: position of counters in champions list that are nonzero"""   
    logging.debug("Function check_nonzero_counters() called")

    nonzeroCountersList = []
    nonzeroCountersNumberList = []
    for i,champCounter in enumerate(list1d):
        if champCounter.get() >= 1:
            nonzeroCountersList.append(champCounter)
            nonzeroCountersNumberList.append(i)
            if champCounter.get() >= 2:
                nonzeroCountersList.append(champCounter) 
                nonzeroCountersNumberList.append(i)
                if champCounter.get() >= 3:
                    nonzeroCountersList.append(champCounter)
                    nonzeroCountersNumberList.append(i)
                    if champCounter.get() >= 4:
                        nonzeroCountersList.append(champCounter)
                        nonzeroCountersNumberList.append(i)
    logging.info("Nonzero counters list human readable: ")
    for champIndex in nonzeroCountersNumberList:
        logging.info("{}".format(championsList[champIndex].name))
    logging.info("Nonzero counters indexes(return): {}".format(nonzeroCountersNumberList))
    logging.info("This is nonzero Counter list: {}".format(nonzeroCountersList))

    
    logging.debug("Function check_nonzero_counters() end")
    return nonzeroCountersNumberList
    





def show_nonzero_counters(rowOffset=0):
    """It shows up champions to buy that counters are nonzero, as a button.
    Created button will add one to champion pool counter, delete itself from window
    and sub one from counters champions that can be bought.
    In: rowOffset by default = 0 for buttons row placement."""
    logging.debug("Function show_nonzero_counters() called")

    global buttonCalcList
    buttonCalcList =[0] * CARDSTOBUYAMOUNT
    championPositionInListOrderedByOrigin = check_nonzero_counters()
    for i in range(0,len(championPositionInListOrderedByOrigin),1):
        buttonCalcList[i] = tk.Button(MainWindow, text=(df.Champion[championPositionInListOrderedByOrigin[i]]),
            command=lambda i = i:[add(OriginChampsCountersListUseAsButtons[championPositionInListOrderedByOrigin[i]]),
                    delete_button(i), sub(OriginChampsCountersToBuy[championPositionInListOrderedByOrigin[i]])])
        buttonCalcList[i].grid(row=12+rowOffset, column=ShiftBetweenOrigins*(i+1))
        
    
    logging.debug("Function show_nonzero_counters() end")
    return None
    




def show_points_for_nonzero_counters(rowOffset=2, showMode=1):
    """It shows up champions POINTS to buy that counters are nonzero, as a text.
    Doesnt disappear currently, should be fixed.
    In: rowOffset by default = 0 for buttons row placement."""
    logging.debug("Function show_points_for_nonzero_counters() called")

    global textLabelList
    pointsForChampionsToBuy = [0] * CARDSTOBUYAMOUNT
    textLabelList =[0] * CARDSTOBUYAMOUNT
    championPositionInListOrderedByOrigin =check_nonzero_counters()
    for i in range(0,len(championPositionInListOrderedByOrigin),1):
        pointsForChampionsToBuy[i] = (df.Points[championPositionInListOrderedByOrigin[i]] + additional_points_from_origin_combo(championPositionInListOrderedByOrigin[i]) 
                  + additional_points_from_class_combo(championPositionInListOrderedByOrigin[i]) + additional_points_from_champions_in_pool(championPositionInListOrderedByOrigin[i]))
        pointsForChampionsToBuy[i] = round(pointsForChampionsToBuy[i],3)
        if showMode:
            textLabelList[i] = tk.Label(MainWindow, text=pointsForChampionsToBuy[i]).grid(row=12+rowOffset, column=ShiftBetweenOrigins*(i+1))
    logging.info("Points and championPositionInListOrderedByOrigin: {}".format(list(zip(pointsForChampionsToBuy,championPositionInListOrderedByOrigin))))
    
    humanReadableChampions = []
    logging.info("Should be empty list: {}".format(humanReadableChampions))
    for champIndex in championPositionInListOrderedByOrigin:
        humanReadableChampions.append(championsList[champIndex].name)
    logging.info("Should be filled with nonzero champions to buy: {}".format(humanReadableChampions))
    
    logging.info("Champions that are availbable to buy with calculated points list human readable: {}".format(list(zip(pointsForChampionsToBuy,humanReadableChampions))))

    logging.debug("Function show_points_for_nonzero_counters() end")
    return list(zip(pointsForChampionsToBuy,championPositionInListOrderedByOrigin))


def show_nonzero_counters_with_points(rowOffset1= 0, rowOffset2 =2):
    """First updates classes and origins to get points updated, then shows
    champions to buy as a buttons and their points as a text.
    In: rowOffset1 by default 0 for buttons.
    rowOffset2 by default 2 for points as a text."""
    logging.debug("Function show_nonzero_counters_with_points() called")

    update_classes_and_origins()
    show_nonzero_counters(rowOffset1)
    pointsWithPositionZip = show_points_for_nonzero_counters(rowOffset2)
    
    logging.debug("Function show_nonzero_counters_with_points() end")
    return pointsWithPositionZip


def update_origins():
    """Checks nonzero counters for champions in pool and updates origins by 
    setting origin counters."""
    logging.debug("Function update_origins() called")

    originIntCounters = [0] * len(originList)
    for i,originChamp in enumerate(originList): # looping over counters for every origin
        logging.info("Current origin: {}".format(originChamp))
        for j,champ in enumerate(championsList): # for loop to assign how much champions are nonzero in origin
            if champ.champCounter.get() >= 1:
                logging.info("Current champ with counter >=1: {}".format(champ.name))
                if ((originChamp == champ.originPrim) or (originChamp == champ.originSec)):
                    logging.info("Current champ with counter >=1 match origin Prim or Sec \
                                 : {} or {}".format(champ.originPrim, champ.originSec))
                    originIntCounters[i] = originIntCounters[i] + 1
        logging.info("Number of nonzero champions in this origin: {}".format(originIntCounters[i]))
        OriginCounters[i].set(originIntCounters[i])
        
    logging.debug("Function update_origins() end")
    return None
         
            



def update_classes():
    """Checks nonzero counters for champions in pool and updates classes by 
    setting class counters."""
    logging.debug("Function update_classes() called")

    classIntCounters = [0] * len(classList)
    for i,classChamp in enumerate(classList): # looping over counters for every class
        logging.info("Current class: {}".format(classChamp))
        for j,champ in enumerate(championsList):# for loop to assign how much champions are nonzero in class
            if champ.champCounter.get() >= 1:
                logging.info("Current champ with counter >=1: {}".format(champ.name))
                if ((classChamp == champ.classPrim) or (classChamp == champ.classSec)):
                    logging.info("Current champ with counter >=1 match class Prim or Sec \
                                 : {} or {}".format(champ.classPrim, champ.classSec))
                    classIntCounters[i] = classIntCounters[i] + 1
        logging.info("Number of nonzero champions in this class = {}".format(classIntCounters[i]))
        ClassCounters[i].set(classIntCounters[i])
        
    logging.debug("Function update_classes() end")
    return None
        
def update_classes_and_origins():
    """Checks nonzero counters for champions in pool and updates classes and origins."""
    logging.debug("Function update_classes_and_origins() called")

    update_origins()
    update_classes()        
    
    logging.debug("Function update_classes_and_origins() end")
        

def additional_points_from_origin_combo(championNumber):
    """Part of sum points, bonus from origin for specific champion.
    In: championNumber its just position of champion in list by primal 
    champions to buy list.
    Out: Bonus points from origin."""
    logging.debug("Function additional_points_from_origin_combo() called")

    logging.info("Calculating origin points for champ named: {} ".format(championsList[championNumber].name))
    bonusPointsFromOriginNew = 0.2
    totalCount = championsList[championNumber].originPrimCounter.get()
    logging.info("Origin primary counter = {}".format(totalCount))
    if championsList[championNumber].originSec != "None":
        totalCount = championsList[championNumber].originSecCounter.get() + totalCount
        logging.info("Origin primary + secondary counter = {}".format(totalCount))
    
    originBonus = totalCount * bonusPointsFromOriginNew
    logging.info("Bonus(return) = {}".format(originBonus))
    logging.debug("Function additional_points_from_origin_combo() end")
    return originBonus
    

    

def additional_points_from_class_combo(championNumber):
    """Part of sum points, bonus from class for specific champion.
    In: championNumber its just position of champion in list by primal 
    champions to buy list.
    Out: Bonus points from class."""
    logging.debug("Function additional_points_from_class_combo() called")

    logging.info("Calculating class points for champ named: {} ".format(championsList[championNumber].name))
    bonusPointsFromClassNew = 0.2
    totalCount = championsList[championNumber].classPrimCounter.get()
    if championsList[championNumber].classSec != "None":
        totalCount = championsList[championNumber].classSecCounter.get() + totalCount
        logging.info("Class primary + secondary counter = {}".format(totalCount))

    classBonus = totalCount * bonusPointsFromClassNew
    logging.info("Bonus(return) = {}".format(classBonus))
    logging.debug("Function additional_points_from_class_combo() end")
    return classBonus



def additional_points_from_champions_in_pool(championNumber):
    """Part of sum points, bonus from champion in pool.
    In: championNumber its just position of champion in list by primal 
    champions to buy list.
    Out: Bonus points from champions that are already in pool."""
    logging.debug("Function additional_points_from_champions_in_pool() called")

    bonusPointsFromChampionPool = (championsList[championNumber].champCounter.get() -1) * 0.2
    logging.info("bonusPointsFromChampionPool = {} for champ named: {} ".format(bonusPointsFromChampionPool, championsList[championNumber].name))
    
    logging.debug("Function additional_points_from_champions_in_pool() end")
    return bonusPointsFromChampionPool

    
def delete_button(position):
    """Deleting buttons"""
    logging.debug("Function delete_button() called")

    buttonCalcList[position].destroy()

    logging.debug("Function delete_button() end")
    
    
    
def delete_all_buttons():
    logging.debug("Function delete_all_buttons() called")

    for button in buttonCalcList:
        button.destroy()
        
    logging.debug("Function delete_all_buttons() end")


ShiftBetweenOrigins = 6

OriginLabelPositionColumn = 1


UPSIDE = 0 ############# champion pool
DOWNSIDE = 16################ champions to buy





labelTitle = tk.Label(MainWindow, text="Champion pool", font=boldedFont).grid(row=0, column=ShiftBetweenOrigins*5)

labelTitle = tk.Label(MainWindow, text=originList[0]).grid(row=1, column=OriginLabelPositionColumn)



labelTitle = tk.Label(MainWindow, text="Champions to buy", font=boldedFont).grid(row=DOWNSIDE-1, column=ShiftBetweenOrigins*5)


###### champions
for i in range(0, len(OriginChampsFromDFList),1):
    show_champions_from_origin(i, OriginChampsFromDFList[i], OriginChampsCountersList[i], UPSIDE)

for i in range(0, len(OriginChampsFromDFList),1):
    show_champions_from_origin(i, OriginChampsFromDFList[i], OriginChampsCountersBuyList[i], DOWNSIDE)
    
####origins
show_champions_from_origin(len(OriginChampsFromDFList),OriginNames, OriginCounters, UPSIDE,ORIGINFLAG)    

#### primary class
show_champions_from_origin((len(OriginChampsFromDFList)+1), classList, ClassCounters, UPSIDE, ORIGINFLAG )
labeling = tk.Label(MainWindow, text="Left to buy", font=boldedFont).grid(row=12+0, column=0)

labeling = tk.Label(MainWindow, text="Points", font=boldedFont).grid(row=14+0, column=0)



buttonCal = tk.Button(MainWindow, text="reset", command=lambda:reset_counters_in_list(OriginChampsCountersToBuy)).grid(row=DOWNSIDE, column=6)


# buttonCal = tk.Button(MainWindow, text="nonzero", command=lambda:check_nonzero_counters(OriginChampsCountersBuyList)).grid(row=DOWNSIDE, column=12)

# buttonCal = tk.Button(MainWindow, text="Shownonzero", command=lambda:show_nonzero_counters(0)).grid(row=DOWNSIDE, column=18)

# buttonCal = tk.Button(MainWindow, text="Showpoints", command=lambda:show_points_for_nonzero_counters(2)).grid(row=DOWNSIDE, column=24)

# buttonCal = tk.Button(MainWindow, text="update", command=lambda:update_origins()).grid(row=DOWNSIDE, column=30)



# buttonCal = tk.Button(MainWindow, text="updateC", command=lambda:update_classes()).grid(row=DOWNSIDE, column=36)


buttonCal = tk.Button(MainWindow, text="update classes", command=lambda:update_classes_and_origins()).grid(row=DOWNSIDE, column=12)

buttonCal = tk.Button(MainWindow, text="show points", command=lambda:show_nonzero_counters_with_points()).grid(row=DOWNSIDE, column=18)

buttonCal = tk.Button(MainWindow, text="OCR", command=lambda:update_champions_to_buy_from_ocr_detection()).grid(row=DOWNSIDE, column=24)

buttonCal = tk.Button(MainWindow, text="draw rectangles", command=lambda:draw_on_champion_to_buy_cards()).grid(row=DOWNSIDE, column=30)

buttonCal = tk.Button(MainWindow, text="scan&go", command=lambda:draw_rectangles_show_points_show_buttons_reset_counters()).grid(row=DOWNSIDE, column=36)


MainWindow.attributes('-alpha', 0.9)
MainWindow.mainloop()
