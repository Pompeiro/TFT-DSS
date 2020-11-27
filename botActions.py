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
import pydirectinput

import time

import mouseinfo



import pandas as pd


import easyocr
import cv2 as cv
from windowcapture import WindowCapture


from operator import itemgetter

import numpy as np

from win32gui import GetWindowText, GetForegroundWindow


inGameWindow = pyautogui.getWindowsWithTitle('League of Legends')[0]
inGameWindow.minimize()
time.sleep(0.5)
inGameWindow.restore()
inGameWindow.activate()
time.sleep(0.5)

playOrPartyButtonInClient = [440,200]

confirmButtonInClient = [850,850]

findMatchButtonInClient = [850,840]

acceptButtonInClient = [960,720]



pyautogui.click(playOrPartyButtonInClient)
time.sleep(5)


pyautogui.click(confirmButtonInClient)
time.sleep(5)


pyautogui.click(findMatchButtonInClient)
time.sleep(2)

u=1
while GetWindowText(GetForegroundWindow()) == 'League of Legends':
    pyautogui.click(acceptButtonInClient)
    time.sleep(1)
    u=0

print("Game should be accepted")

time.sleep(10)







###################################################################################
############################## OCR START ######################################
####################################################################################


championListForOCR = ['Aatrox', 'Ahri', 'Akali', 'Annie', 'Aphelios',
                        'Ashe', 'Azir', 'Cassiopeia', 'Diana', 'Elise', 
                        'Evelynn', 'Ezreal', 'Fiora', 'Garen', 'Hecarim',
                        'Irelia', 'Janna', 'Jarvan IV', 'Jax', 'Jhin', 
                        'Jinx', 'Kalista', 'Katarina', 'Kayn', 'Kennen',
                        'Kindred', 'Lee Sin', 'Lillia', 'Lissandra', 'Lulu',
                        'Lux', 'Maokai', 'Morgana', 'Nami', 'Nidalee',
                        'Nunu', 'Pyke', 'Riven', 'Sejuani', 'Sett',
                        'Shen', 'Sylas', 'Tahm Kench', 'Talon', 'Teemo', 
                        'Thresh', 'Twisted Fate', 'Vayne', 'Veigar', 'Vi', 
                        'Warwick', 'Wukong', 'Xin Zhao', 'Yasuo', 'Yone',
                        'Yuumi', 'Zed', 'Zilean']


reader = easyocr.Reader(['en'])

screenshot = cv.imread("ss.jpg",cv.IMREAD_UNCHANGED)

###################################### 
######################################
###### IF U WANT TEST WITHOUT GAME THEN COMMENT HERE
######################################
######################################





# wincap = None

wincap = WindowCapture('League of Legends (TM) Client')


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



def make_cropped_ss_and_get_champions_to_buy(loadImage=0, window=wincap, croppingY=970, croppingX=450, croppingHeight=30, croppingWidth=1000):
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

###################################################################################
############################## POINTS END ######################################
####################################################################################




###################################################################################
############################## POINTS START ######################################
####################################################################################

df = pd.read_csv("scaledChampionsdf.csv") 

df.drop('Unnamed: 0', axis=1, inplace=True)

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



list(df.query('Champion == "Pyke"').Points)

OriginNames = sorted(list(set(df.OriginPrimary)))

ClassPrimaryNames = list(set(df.ClassPrimary))
ClassSecondaryNames = list(set(df.query('ClassSecondary != "None"').ClassSecondary))
for secondary in ClassSecondaryNames:
    ClassPrimaryNames.append(secondary)
ClassNames = sorted(list(set(ClassPrimaryNames)))


championNamesList=list(df.Champion)





# for champ in championNamesList:
#     print("counter"+champ+" = 0")
    
# for champ in championNamesList:
#     print("counter"+champ, end = ', ')
    
    
####### champions counters
    
    
counterAatrox = 0
counterAhri = 0
counterAkali = 0
counterAnnie = 0
counterAphelios = 0
counterAshe = 0
counterAzir = 0
counterCassiopeia = 0
counterDiana = 0
counterElise = 0
counterEvelynn = 0
counterEzreal = 0
counterFiora = 0
counterGaren = 0
counterHecarim = 0
counterIrelia = 0
counterJanna = 0
counterJarvanIV = 0
counterJax = 0
counterJhin = 0
counterJinx = 0
counterKalista = 0
counterKatarina = 0
counterKayn = 0
counterKennen = 0
counterKindred = 0
counterLeeSin = 0
counterLillia = 0
counterLissandra = 0
counterLulu = 0
counterLux = 0
counterMaokai = 0
counterMorgana = 0
counterNami = 0
counterNidalee = 0
counterNunu = 0
counterPyke = 0
counterRiven = 0
counterSejuani = 0
counterSett = 0
counterShen = 0
counterSylas = 0
counterTahmKench = 0
counterTalon = 0
counterTeemo = 0
counterThresh = 0
counterTwistedFate = 0
counterVayne = 0
counterVeigar = 0
counterVi = 0
counterWarwick = 0
counterWukong = 0
counterXinZhao = 0
counterYasuo = 0
counterYone = 0
counterYuumi = 0
counterZed = 0
counterZilean = 0

championsCounterList = [counterAatrox, counterAhri, counterAkali, counterAnnie,
                        counterAphelios, counterAshe, counterAzir, counterCassiopeia,
                        counterDiana, counterElise, counterEvelynn, counterEzreal,
                        counterFiora, counterGaren, counterHecarim, counterIrelia,
                        counterJanna, counterJarvanIV, counterJax, counterJhin,
                        counterJinx, counterKalista, counterKatarina, counterKayn,
                        counterKennen, counterKindred, counterLeeSin, counterLillia,
                        counterLissandra, counterLulu, counterLux, counterMaokai,
                        counterMorgana, counterNami, counterNidalee, counterNunu,
                        counterPyke, counterRiven, counterSejuani, counterSett,
                        counterShen, counterSylas, counterTahmKench, counterTalon,
                        counterTeemo, counterThresh, counterTwistedFate, counterVayne,
                        counterVeigar, counterVi, counterWarwick, counterWukong,
                        counterXinZhao, counterYasuo, counterYone, counterYuumi,
                        counterZed, counterZilean]




# print("CultistCounters = [")
# for champ in CultistChamps:
#     print("counter"+champ,end = ", ")
# print("]")
# print()
    


# print("DivineCounters = [")
# for champ in DivineChamps:
#     print("counter"+champ,end = ", ")
# print("]")
# print()

    

# print("DuskCounters = [")
# for champ in DuskChamps:
#     print("counter"+champ,end = ", ")
# print("]")
# print()

    

# print("ElderwoodCounters = [")
# for champ in ElderwoodChamps:
#     print("counter"+champ,end = ", ")
# print("]")
# print()


# print("EnlightenedCounters = [")
# for champ in EnlightenedChamps:
#     print("counter"+champ,end = ", ")
# print("]")
# print()



# print("ExileCounters = [")
# for champ in ExileChamps:
#     print("counter"+champ,end = ", ")
# print("]")
# print()



# print("FortuneCounters = [")
# for champ in FortuneChamps:
#     print("counter"+champ,end = ", ")
# print("]")
# print()



# print("MoonlightCounters = [")
# for champ in MoonlightChamps:
#     print("counter"+champ,end = ", ")
# print("]")
# print()



# print("NinjaCounters = [")
# for champ in NinjaChamps:
#     print("counter"+champ,end = ", ")
# print("]")
# print()



# print("SpiritCounters = [")
# for champ in SpiritChamps:
#     print("counter"+champ,end = ", ")
# print("]")
# print()


# print("TheBossCounters = [")
# for champ in TheBossChamps:
#     print("counter"+champ,end = ", ")
# print("]")
# print()


# print("TormentedCounters = [")
# for champ in TormentedChamps:
#     print("counter"+champ,end = ", ")
# print("]")
# print()


# print("WarlordCounters = [")
# for champ in WarlordChamps:
#     print("counter"+champ,end = ", ")
# print("]")
# print()


########################## class counters


CultistCounters = [counterAatrox, counterElise, counterEvelynn, counterJhin,
                   counterKalista, counterPyke, counterTwistedFate, counterZilean]

DivineCounters = [counterJax, counterLeeSin, counterLux, counterWarwick,
                  counterWukong, counterIrelia]

DuskCounters = [counterCassiopeia, counterLillia, counterRiven, counterThresh, counterVayne]

ElderwoodCounters = [counterAshe, counterEzreal, counterHecarim, counterLulu,
                     counterMaokai, counterNunu, counterVeigar]

EnlightenedCounters = [counterFiora, counterIrelia, counterJanna, counterMorgana,
                       counterNami, counterTalon]

ExileCounters = [counterYasuo, counterYone]

FortuneCounters = [counterAnnie, counterJinx, counterSejuani, counterTahmKench,
                   counterKatarina]

MoonlightCounters = [counterAphelios, counterDiana, counterLissandra, counterSylas]

NinjaCounters = [counterAkali, counterKennen, counterShen, counterZed]

SpiritCounters = [counterAhri, counterKindred, counterTeemo, counterYuumi]

TheBossCounters = [counterSett]

TormentedCounters = [counterKayn]

WarlordCounters = [counterAzir, counterGaren, counterJarvanIV, counterKatarina,
                   counterNidalee, counterVi, counterXinZhao]


counterCultist= 0
counterDivine= 0
counterDusk= 0
counterElderwood= 0
counterEnlightened= 0
counterExile= 0
counterFortune= 0
counterMoonlight= 0
counterNinja= 0
counterSpirit= 0
counterTheBoss= 0
counterTormented= 0
counterWarlord= 0

OriginCounters = [counterCultist, counterDivine, counterDusk, counterElderwood,
                  counterEnlightened, counterExile, counterFortune, counterMoonlight,
                  counterNinja, counterSpirit, counterTheBoss, counterTormented,
                  counterWarlord]

OriginChampsCountersList = [CultistCounters, DivineCounters, DuskCounters, 
                          ElderwoodCounters, EnlightenedCounters, ExileCounters, 
                          FortuneCounters, MoonlightCounters, NinjaCounters,
                          SpiritCounters, TheBossCounters, TormentedCounters, WarlordCounters]



counterAdept = 0
counterAssassin = 0
counterBrawler = 0
counterDazzler = 0
counterDuelist = 0
counterEmperor = 0
counterHunter = 0
counterKeeper = 0
counterMage = 0
counterMystic = 0
counterShade = 0
counterSharpshooter = 0
counterVanguard = 0


AdeptCounters = [counterIrelia, counterShen, counterYone]

AssassinCounters = [counterAkali, counterDiana, counterKatarina, counterPyke,
                    counterTalon]

BrawlerCounters = [counterMaokai, counterNunu, counterSett, counterSylas,
                   counterTahmKench, counterVi, counterWarwick]

DazzlerCounters = [counterEzreal, counterLissandra, counterLux, counterMorgana]

DuelistCounters = [counterFiora, counterJax, counterKalista, counterLeeSin,
                   counterXinZhao, counterYasuo]

EmperorCounters = [counterAzir]

HunterCounters = [counterAphelios, counterAshe, counterKindred, counterWarwick]

KeeperCounters = [counterAzir, counterElise, counterJarvanIV, counterKennen,
                  counterRiven]

MageCounters = [counterAhri, counterAnnie, counterLillia, counterLulu, counterNami,
                counterTwistedFate, counterVeigar]

MysticCounters = [counterCassiopeia, counterJanna, counterShen, counterYuumi,
                  counterZilean]

ShadeCounters = [counterEvelynn, counterKayn, counterZed]

SharpshooterCounters = [counterJhin, counterJinx, counterNidalee, counterTeemo,
                        counterVayne]

VanguardCounters = [counterAatrox, counterGaren, counterHecarim, counterSejuani,
                    counterThresh, counterWukong]


ClassPrimaryCounters = [counterAdept, counterAssassin, counterBrawler, counterDazzler,
                        counterDuelist, counterEmperor, counterHunter, counterKeeper,
                        counterMage, counterMystic, counterShade, counterSharpshooter,
                        counterVanguard]

ClassPrimaryCountersList = [AdeptCounters, AssassinCounters, BrawlerCounters,
                            DazzlerCounters, DuelistCounters, EmperorCounters,
                            HunterCounters, KeeperCounters, MageCounters, 
                            MysticCounters, ShadeCounters, SharpshooterCounters,
                            VanguardCounters]

bonusPointsFromOrigin =[0] * len(OriginChampsCountersList)

bonusPointsFromClass = [0] * len(ClassPrimaryCountersList)



def update_origins():
    """Checks nonzero counters for champions in pool and updates origins.
    Also sets bonus points from origin."""
    for i,origin in enumerate(OriginChampsCountersList):
        count = 0
        for champ in origin:
            if champ >= 1:
                count = count + 1
        OriginCounters[i] = count
        bonusPointsFromOrigin[i] = count * 0.2  
        
        
def update_classes():
    """Checks nonzero counters for champions in pool and updates classes.
    Also sets bonus points from class."""
    for i,origin in enumerate(ClassPrimaryCountersList):
        count = 0
        for champ in origin:
            if champ >= 1:
                count = count + 1
        ClassPrimaryCounters[i] = count
        bonusPointsFromClass[i] = count * 0.2 
        
def update_classes_and_origins():
    """Checks nonzero counters for champions in pool and updates classes and origins.
    Also sets bonus points from class and origins."""
    update_origins()
    update_classes()        
        

def additional_points_from_origin_combo(counterIndex):
    """Part of sum points, bonus from origin for specific champion.
    In: counterIndex its just position of champion in list by primal 
    champions to buy list.
    Out: Bonus points from origin."""
    pos = OriginNames.index(df.OriginPrimary[counterIndex])
    if df.OriginSecondary[counterIndex] != "None":
        pos2 = OriginNames.index(df.OriginSecondary[counterIndex])
        print("bonusPointsFromOrigin[pos] + bonusPointsFromOrigin[pos2] ",
              bonusPointsFromOrigin[pos] + bonusPointsFromOrigin[pos2] )
        return bonusPointsFromOrigin[pos]  + bonusPointsFromOrigin[pos2]  
    else:
        print("bonusPointsFromOrigin[pos] ",bonusPointsFromOrigin[pos])
        return bonusPointsFromOrigin[pos]

def additional_points_from_class_combo(counterIndex):
    """Part of sum points, bonus from class for specific champion.
    In: counterIndex its just position of champion in list by primal 
    champions to buy list.
    Out: Bonus points from class."""
    pos = ClassNames.index(df.ClassPrimary[counterIndex])
    if df.ClassSecondary[counterIndex] != "None":
        pos2 = ClassNames.index(df.ClassSecondary[counterIndex])
        print("bonusPointsFromClass[pos] + bonusPointsFromClass[pos2] ",
              bonusPointsFromClass[pos] + bonusPointsFromClass[pos2] )
        return bonusPointsFromClass[pos]  + bonusPointsFromClass[pos2]  
    else:
        print("bonusPointsFromClass[pos] ",bonusPointsFromClass[pos])
        return bonusPointsFromClass[pos]  
        
        
def additional_points_from_champions_in_pool(counterIndex):
    """Part of sum points, bonus from champion in pool.
    In: championNumber its just position of champion in list by primal 
    champions to buy list.
    Out: Bonus points from champions that are already in pool."""
    bonusPointsFromChampionPool = (championsCounterList[counterIndex] -1) * 0.2
    print("bonusPointsFromChampionPool[pos] ",bonusPointsFromChampionPool)
    return bonusPointsFromChampionPool




def from_OCR_champions_to_buy_list_to_counter_index_list():
    OCRchampionsToBuyList=update_champions_to_buy_from_ocr_detection()
    counterIndexList = []
    for detected in OCRchampionsToBuyList:
        counterIndexList.append(championListForOCR.index(detected))
        print("Index of detected champion in OCR: ",championListForOCR.index(detected))
        
    print("Should be max 5 items there !!!!!!!!!!!!!!! if not check from_OCR_champions_to_buy_list_to_counter_index_list: ",counterIndexList)
    return counterIndexList
        
        

def show_points_for_champions_to_buy():
    """It shows up champions POINTS to buy that counters are nonzero, as a text.
    Doesnt disappear currently, should be fixed.
    In: rowOffset by default = 0 for buttons row placement."""
    counterIndexListLocal=from_OCR_champions_to_buy_list_to_counter_index_list()
    update_classes_and_origins()
    pointsForChampionsToBuy = [0] * 5
    for i in range(0,len(counterIndexListLocal),1):
        pointsForChampionsToBuy[i] = (df.Points[counterIndexListLocal[i]] + additional_points_from_origin_combo(counterIndexListLocal[i]) 
                  + additional_points_from_class_combo(counterIndexListLocal[i]) + additional_points_from_champions_in_pool(counterIndexListLocal[i]))
    return pointsForChampionsToBuy





pointsForChampionsInGameToBuyINITIAL=[0,0,0,0,0]
champsToBuyIndexesINITIAL=[1, 2, 3, 4, 5]

posOnScreenINITIAL = [0, 1, 2, 3, 4]

def create_list_sorted_champions_to_buy_points_then_indexes_then_position_on_screen(pointsForChamp=pointsForChampionsInGameToBuyINITIAL, champsTOBUYINDEXES=champsToBuyIndexesINITIAL, posONSCREEN=posOnScreenINITIAL):
    #### https://stackoverflow.com/questions/6422700/how-to-get-indices-of-a-sorted-array-in-python
    print("inputs to create_list_sorted_champions_to_buy_points_then_indexes_then_position_on_screen()")
    print("pointsForChamp, champsTOBUYINDEXES, posONSCREEN")
    print(pointsForChamp, champsTOBUYINDEXES, posONSCREEN)

    championsToBuyPointsThenIndexesThenPositionOnScreen = []
    for i, point in enumerate(pointsForChamp):
        championsToBuyPointsThenIndexesThenPositionOnScreen.append([point, champsTOBUYINDEXES[i], posONSCREEN[i]])
    
    sorted_inds, sorted_items = zip(*sorted([(i,e) for i,e in enumerate(championsToBuyPointsThenIndexesThenPositionOnScreen)], key=itemgetter(1), reverse=True))
    print("Output create_list_sorted_champions_to_buy_points_then_indexes_then_position_on_screen")
    print("sorted_items")
    print(sorted_items)
    print("and sorted inds")
    print(sorted_inds)
    return sorted_items

SORTEDchampionsToBuyPointsThenIndexesThenPositionOnScreen = [[1.2645505077078336, 36, 0], ### hardcoded only for give this initial value
                                                             [1.2407485721719331, 16, 4],
                                                             [1.1604445548925015, 51, 2],
                                                             [1.06933241627392, 42, 1],
                                                             [1.0686296243238476, 31, 3]]




###################################################################################
############################## POINTS END ######################################
####################################################################################








#############################################################################
################ CHECK HEX OCCUPANCY WITH template matching ##################]
################################################################################
jpgwithunits = "C:\\Users\\janusz\\Pictures\\tft\\testingimages\\graDziesiecDefaultArena\\name00000012.jpg"
jpgwithunits = "playground.jpg"
jpgwithunits = "playgroundwithunits.jpg"

def make_cropped_ss(loadImage=0, window=wincap, croppingY=0, croppingX=0, croppingHeight=1080, croppingWidth=1920, saveMode=0, savingName="sss.jpg"):
    if loadImage:
        screenshot = cv.imread(jpgwithunits,cv.IMREAD_UNCHANGED)
    else:
        screenshot = window.get_screenshot()
    #print(screenshot)
    crop_img = screenshot[croppingY:croppingY+croppingHeight, croppingX:croppingX+croppingWidth]
    cv.imshow("ss", crop_img)
    if saveMode:
        cv.imwrite(savingName, crop_img)    
    return crop_img




# img = make_cropped_ss_and_get_champions_to_buy()

img = cv.imread("playground.jpg",cv.IMREAD_UNCHANGED)
# img=cv.imread("playgroundwithunits.jpg", cv.IMREAD_UNCHANGED)
playgroundHexes = [ [584,410], [677,413], [798,405], [915,400], [1020,415], [1128,409],
                   [1227,402], [622,466], [731,468], [855,476], [954,484], [1077,480],
                   [1189,477], [1306,474], [535,515], [670,515], [783,515], [902,515],
                   [1018,515], [1142,515], [1248,515], [599,618], [720,627], [847,626],
                   [974,625], [1100,627], [1207,627], [1327,630] ]


benchHexes = [ [454,720], [567,720], [671,720], [789,720], [900,720], [1011,720],
              [1120,720], [1233,720], [1328,720] ]

hexToTemplateMatchWidth = 50
hextoTemlpateMatchHeight = 50

playgroundHexesWithOffsetToCropp = []

for hexi in playgroundHexes:
    playgroundHexesWithOffsetToCropp.append([hexi[0]-25,hexi[1]-25])
    
    
benchHexesWithOffsetToCropp = []

for hexi in benchHexes:
    benchHexesWithOffsetToCropp.append([hexi[0]-25,hexi[1]-25])    
    
    
# for i,hexi in enumerate(playgroundHexesWithOffsetToCropp):
#     saveName = "C:\\Users\\janusz\\Documents\\TFT-DSS\\hexJPG\\playground\\playgroundHex" + "{}".format(i) + ".jpg"
#     make_cropped_ss_and_get_champions_to_buy(croppingY=hexi[1], croppingX=hexi[0], croppingHeight=hextoTemlpateMatchHeight,croppingWidth=hexToTemplateMatchWidth,saveMode=1,savingName=saveName)


# for i,hexi in enumerate(benchHexesWithOffsetToCropp):
#     saveName = "C:\\Users\\janusz\\Documents\\TFT-DSS\\hexJPG\\bench\\benchHex" + "{}".format(i) + ".jpg"
#     make_cropped_ss_and_get_champions_to_buy(croppingY=hexi[1], croppingX=hexi[0], croppingHeight=hextoTemlpateMatchHeight,croppingWidth=hexToTemplateMatchWidth,saveMode=1,savingName=saveName)







HEXES_WITHOUT_CHAMPIONS_JPG_LIST = ['hexJPG\\playground\\playgroundHex0.jpg',
                                     'hexJPG\\playground\\playgroundHex1.jpg',
                                     'hexJPG\\playground\\playgroundHex2.jpg',
                                     'hexJPG\\playground\\playgroundHex3.jpg',
                                     'hexJPG\\playground\\playgroundHex4.jpg',
                                     'hexJPG\\playground\\playgroundHex5.jpg',
                                     'hexJPG\\playground\\playgroundHex6.jpg',
                                     'hexJPG\\playground\\playgroundHex7.jpg',
                                     'hexJPG\\playground\\playgroundHex8.jpg',
                                     'hexJPG\\playground\\playgroundHex9.jpg',
                                     'hexJPG\\playground\\playgroundHex10.jpg',
                                     'hexJPG\\playground\\playgroundHex11.jpg',
                                     'hexJPG\\playground\\playgroundHex12.jpg',
                                     'hexJPG\\playground\\playgroundHex13.jpg',
                                     'hexJPG\\playground\\playgroundHex14.jpg',
                                     'hexJPG\\playground\\playgroundHex15.jpg',
                                     'hexJPG\\playground\\playgroundHex16.jpg',
                                     'hexJPG\\playground\\playgroundHex17.jpg',
                                     'hexJPG\\playground\\playgroundHex18.jpg',
                                     'hexJPG\\playground\\playgroundHex19.jpg',
                                     'hexJPG\\playground\\playgroundHex20.jpg',
                                     'hexJPG\\playground\\playgroundHex21.jpg',
                                     'hexJPG\\playground\\playgroundHex22.jpg',
                                     'hexJPG\\playground\\playgroundHex23.jpg',
                                     'hexJPG\\playground\\playgroundHex24.jpg',
                                     'hexJPG\\playground\\playgroundHex25.jpg',
                                     'hexJPG\\playground\\playgroundHex26.jpg',
                                     'hexJPG\\playground\\playgroundHex27.jpg']


BENCH_WITHOUT_CHAMPIONS_JPG_LIST = ['hexJPG\\bench\\benchHex0.jpg',
                                     'hexJPG\\bench\\benchHex1.jpg',
                                     'hexJPG\\bench\\benchHex2.jpg',
                                     'hexJPG\\bench\\benchHex3.jpg',
                                     'hexJPG\\bench\\benchHex4.jpg',
                                     'hexJPG\\bench\\benchHex5.jpg',
                                     'hexJPG\\bench\\benchHex6.jpg',
                                     'hexJPG\\bench\\benchHex7.jpg',
                                     'hexJPG\\bench\\benchHex8.jpg']

# u = cv.imread("C:\\Users\\janusz\\pictures\\tft\\testingimages\\graBack\\name00000000.jpg",cv.IMREAD_UNCHANGED)
# cv.imshow("okno", u)




# for i,hexi in enumerate(playgroundHexes):
#     print("playgroudHex{}Occupancy = 0".format(i))
playgroudHex0Occupancy = 0
playgroudHex1Occupancy = 0
playgroudHex2Occupancy = 0
playgroudHex3Occupancy = 0
playgroudHex4Occupancy = 0
playgroudHex5Occupancy = 0
playgroudHex6Occupancy = 0
playgroudHex7Occupancy = 0
playgroudHex8Occupancy = 0
playgroudHex9Occupancy = 0
playgroudHex10Occupancy = 0
playgroudHex11Occupancy = 0
playgroudHex12Occupancy = 0
playgroudHex13Occupancy = 0
playgroudHex14Occupancy = 0
playgroudHex15Occupancy = 0
playgroudHex16Occupancy = 0
playgroudHex17Occupancy = 0
playgroudHex18Occupancy = 0
playgroudHex19Occupancy = 0
playgroudHex20Occupancy = 0
playgroudHex21Occupancy = 0
playgroudHex22Occupancy = 0
playgroudHex23Occupancy = 0
playgroudHex24Occupancy = 0
playgroudHex25Occupancy = 0
playgroudHex26Occupancy = 0
playgroudHex27Occupancy = 0



# for i,hexi in enumerate(playgroundHexes):
#     print("playgroudHex{}Occupancy, ".format(i), end="")
    
playgroundHexesOccupancyList = [ playgroudHex0Occupancy, playgroudHex1Occupancy,
                                playgroudHex2Occupancy, playgroudHex3Occupancy,
                                playgroudHex4Occupancy, playgroudHex5Occupancy,
                                playgroudHex6Occupancy, playgroudHex7Occupancy,
                                playgroudHex8Occupancy, playgroudHex9Occupancy,
                                playgroudHex10Occupancy, playgroudHex11Occupancy,
                                playgroudHex12Occupancy, playgroudHex13Occupancy,
                                playgroudHex14Occupancy, playgroudHex15Occupancy,
                                playgroudHex16Occupancy, playgroudHex17Occupancy,
                                playgroudHex18Occupancy, playgroudHex19Occupancy,
                                playgroudHex20Occupancy, playgroudHex21Occupancy,
                                playgroudHex22Occupancy, playgroudHex23Occupancy,
                                playgroudHex24Occupancy, playgroudHex25Occupancy,
                                playgroudHex26Occupancy, playgroudHex27Occupancy ]

# for i,hexi in enumerate(benchHexes):
#     print("benchHex{}Occupancy = 0".format(i))
    
    
    
    
benchHex0Occupancy = 0
benchHex1Occupancy = 0
benchHex2Occupancy = 0
benchHex3Occupancy = 0
benchHex4Occupancy = 0
benchHex5Occupancy = 0
benchHex6Occupancy = 0
benchHex7Occupancy = 0
benchHex8Occupancy = 0   

# for i,hexi in enumerate(benchHexes):
#     print("benchHex{}Occupancy, ".format(i), end="")
    
    
benchHexesOccupancyList = [ benchHex0Occupancy, benchHex1Occupancy, benchHex2Occupancy,
                           benchHex3Occupancy, benchHex4Occupancy, benchHex5Occupancy,
                           benchHex6Occupancy, benchHex7Occupancy, benchHex8Occupancy]



def check_hexes_list_occupancy(hexesToCheckListJPG=HEXES_WITHOUT_CHAMPIONS_JPG_LIST, hexesLocationWithOffset = playgroundHexesWithOffsetToCropp, occupancyList=playgroundHexesOccupancyList):
    img_main = make_cropped_ss()
    for i,jpg in enumerate(hexesToCheckListJPG):
        img_rgb = make_cropped_ss(croppingY=hexesLocationWithOffset[i][1], croppingX=hexesLocationWithOffset[i][0], croppingHeight=hextoTemlpateMatchHeight,croppingWidth=hexToTemplateMatchWidth,saveMode=0,savingName="saveName")
        img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
        template = cv.imread(jpg,0)
        w, h = template.shape[::-1]
        res = cv.matchTemplate(img_gray,template,cv.TM_CCORR_NORMED)
        threshold = 0.95
        loc = np.where( res >= threshold)
        if loc[0].size>0:
            print("not occupied  hex number {}".format(i))
            occupancyList[i]=0
        else:
            print("Hex is occupied {}".format(i))
            occupancyList[i]=1
            
        for pt in zip(*loc[::-1]):
            cv.rectangle(img_main, tuple(hexesLocationWithOffset[i]), (hexesLocationWithOffset[i][0] + w, hexesLocationWithOffset[i][1] + h), (0,0,255), 2)
    cv.imshow("ss5", img_main)
    

# check_hexes_list_occupancy(BENCH_WITHOUT_CHAMPIONS_JPG_LIST,benchHexesWithOffsetToCropp,benchHexesOccupancyList)




##############################################################################
########################## template matching END #############################
##############################################################################








##############################################################################
############################# Simulating user actions ########################
##############################################################################



# Screenshotwindow = pyautogui.getWindowsWithTitle("ss.jpg - Paint")[0]

Screenshotwindow = pyautogui.getWindowsWithTitle('League of Legends (TM) Client')[0]



def update_champion_counter(champWithPointsThenIndexThenPosition=SORTEDchampionsToBuyPointsThenIndexesThenPositionOnScreen[0]):
    # print("champWithPointsThenIndexThenPosition",champWithPointsThenIndexThenPosition)
    # print("champWithPointsThenIndexThenPosition[1]",champWithPointsThenIndexThenPosition[1])
    championsCounterList[champWithPointsThenIndexThenPosition[1]] = championsCounterList[champWithPointsThenIndexThenPosition[1]] + 1
    print("Bought champion: ",championListForOCR[champWithPointsThenIndexThenPosition[1]], "counter current value",championsCounterList[champWithPointsThenIndexThenPosition[1]])



# champions card that you can buy
championToBuyPositionOnGame = [ (600,975), (794,975), (984,975), (1173,975), (1363,975) ]


## hexes from top left to bottom right
playgroundHexes = [ [584,410], [677,413], [798,405], [915,400], [1020,415], [1128,409],
                   [1227,402], [622,466], [731,468], [855,476], [954,484], [1077,480],
                   [1189,477], [1306,474], [535,557], [670,557], [783,549], [902,551],
                   [1018,545], [1142,551], [1248,550], [599,618], [720,627], [847,626],
                   [974,625], [1100,627], [1207,627], [1327,630] ]


# hexes on bench from left to right side

benchHexes = [ [454,734], [567,738], [671,736], [789,735], [900,738], [1011,737],
              [1120,741], [1233,738], [1348,742] ]



def activate_game_window(inGameWindow=Screenshotwindow,sleepDelay = 0.5):
    inGameWindow.minimize()
    time.sleep(sleepDelay)
    inGameWindow.restore()
    inGameWindow.activate()
    time.sleep(sleepDelay)

def buy_best_available_champions_by_points(howMuchChampions=2, mousePathDelay=0.2,inGameWindow=Screenshotwindow, sortedChampionsToBuyPoints=SORTEDchampionsToBuyPointsThenIndexesThenPositionOnScreen):
    activate_game_window(inGameWindow=Screenshotwindow)
    
    for i in range(0,howMuchChampions,1):
        # pydirectinput.moveTo(100, 150) # Move the mouse to the x, y coordinates 100, 150.
        # pydirectinput.click() # Click the mouse at its current location.
        pyautogui.moveTo(x=championToBuyPositionOnGame[sortedChampionsToBuyPoints[i][2]][0], y=championToBuyPositionOnGame[sortedChampionsToBuyPoints[i][2]][1], duration=mousePathDelay)
        pyautogui.mouseDown()
        time.sleep(0.3)
        pyautogui.mouseUp()

        
        update_champion_counter(sortedChampionsToBuyPoints[i])


# buy_best_available_champions_by_points()






def move_champion_from_x_to_y(startingPoint,metaPoint):
    activate_game_window()
    
    pyautogui.moveTo(x=startingPoint[0], y=startingPoint[1], duration=0.1)
    pyautogui.click()
    pyautogui.moveTo(x=metaPoint[0], y=metaPoint[1], duration=0.1)
    pyautogui.mouseDown()
    time.sleep(0.15)
    pyautogui.mouseUp()
    


def move_champion_from_x_to_y_without_game_activation(startingPoint,metaPoint):
    
    pyautogui.moveTo(x=startingPoint[0], y=startingPoint[1], duration=0.1)
    pyautogui.click()
    pyautogui.moveTo(x=metaPoint[0], y=metaPoint[1], duration=0.1)
    pyautogui.mouseDown()
    time.sleep(0.15)
    pyautogui.mouseUp()
    

# move_champion_from_x_to_y(benchHexes[2],playgroundHexes[9])

# move_champion_from_x_to_y(benchHexes[3],playgroundHexes[10])



# move_champion_from_x_to_y(playgroundHexes[21],playgroundHexes[23])




def shuffle_champions_on_first_and_third_row_of_hexes_and_subsitute_bench():
    occupiedHexesLocation = []
    
    check_hexes_list_occupancy(BENCH_WITHOUT_CHAMPIONS_JPG_LIST,benchHexesWithOffsetToCropp,benchHexesOccupancyList)
    check_hexes_list_occupancy()
    i=0
    while i < (len(playgroundHexesOccupancyList)-7):
        if playgroundHexesOccupancyList[i]:
            print("i is {}".format(i))
            occupiedHexesLocation.append(playgroundHexes[i])
            print("Added {} {} to occupiedHexesLocation list in shuffle_champions_on_first_and_third_row_of_hexes function".format(playgroundHexes[i], i))
        if i==6:
            i=i+7 ### to avoid checking second row of playground hexes
            print("changed i: {}".format(i))
        i=i+1
    
    for i in range(0,len(benchHexesOccupancyList),1):
        if benchHexesOccupancyList[i]:
            occupiedHexesLocation.append(benchHexes[i])
            print("Added {} {} to occupiedHexesLocation list in shuffle_champions_on_first_and_third_row_of_hexes function".format(benchHexes[i], i))


    print("occupiedHexesLocation before shuffle {}".format(occupiedHexesLocation))
    np.random.shuffle(occupiedHexesLocation)
    
    print("occupiedHexesLocation after shuffle {}".format(occupiedHexesLocation))
    
    print("There will be {} shufling".format(len(occupiedHexesLocation)//2))

    activate_game_window()
    if (len(occupiedHexesLocation) % 2 == 0):
        for i in range(0,len(occupiedHexesLocation),2):
            move_champion_from_x_to_y_without_game_activation(occupiedHexesLocation[i],occupiedHexesLocation[i+1])
            
            
    if (len(occupiedHexesLocation) % 2 == 1):
        for i in range(0,len(occupiedHexesLocation)-1,2):
            move_champion_from_x_to_y_without_game_activation(occupiedHexesLocation[i],occupiedHexesLocation[i+1])







# playOrPartyButtonInClient = [440,200]

# confirmButtonInClient = [850,850]

# findMatchButtonInClient = [850,840]

# acceptButtonInClient = [960,720]



# activate_game_window()
# pyautogui.click(playOrPartyButtonInClient)
# time.sleep(5)


# pyautogui.click(confirmButtonInClient)
# time.sleep(5)


# pyautogui.click(findMatchButtonInClient)
# time.sleep(2)

# u=1
# while GetWindowText(GetForegroundWindow()) == 'League of Legends':
#     pyautogui.click(acceptButtonInClient)
#     time.sleep(1)
#     u=0


# time.sleep(30)



# def make_cropped_ss_and_get_champions_to_buy(loadImage=0, window=wincap, croppingY=970, croppingX=450, croppingHeight=30, croppingWidth=1000):
#     if loadImage:
#         screenshot = cv.imread("ss.jpg",cv.IMREAD_UNCHANGED)
#     else:
#         screenshot = window.get_screenshot()
#     #print(screenshot)
#     crop_img = screenshot[croppingY:croppingY+croppingHeight, croppingX:croppingX+croppingWidth]
#     cv.imshow("ss", crop_img)
#     OCRResult=reader.readtext(crop_img)
#     print(OCRResult)
#     listOfChampsToBuyThisTurn=sort_detected_champions_to_buy_by_position(OCRResult)
#     return listOfChampsToBuyThisTurn








Screenshotwindow = pyautogui.getWindowsWithTitle('League of Legends (TM) Client')[0]


# update current champions to buy with ocr

try:
    championsToBuyIndexes = from_OCR_champions_to_buy_list_to_counter_index_list()
    pointsForChampionsInGameToBuy = show_points_for_champions_to_buy()
    print(pointsForChampionsInGameToBuy)
    
    posOnScreen = [0, 1, 2, 3, 4]
    
    SORTEDchampionsToBuyPointsThenIndexesThenPositionOnScreen = list(create_list_sorted_champions_to_buy_points_then_indexes_then_position_on_screen(pointsForChamp=pointsForChampionsInGameToBuy, champsTOBUYINDEXES=championsToBuyIndexes, posONSCREEN=posOnScreen))
    
    
    buy_best_available_champions_by_points(howMuchChampions=1, inGameWindow=Screenshotwindow, sortedChampionsToBuyPoints=SORTEDchampionsToBuyPointsThenIndexesThenPositionOnScreen)
except(IndexError):
    pass


# first hex on substitues bench
# 479,727
######################### buy 2 champions with most points


# Points list sorted by apperance on screen





# pyautogui.getWindowsWithTitle("Spyder (Python 3.8)")[0].minimize()

# pyautogui.getWindowsWithTitle("Discord")[0].restore()

# time.sleep(2)

# pyautogui.getWindowsWithTitle("TFTDSS")[0].maximize()

# TFTDSSwindow = pyautogui.getWindowsWithTitle("wind")[0]
# TFTDSSwindow.minimize()
# time.sleep(1)
# TFTDSSwindow.restore()
# TFTDSSwindow.activate()

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

# pyautogui.click(x=850, y=450) ### first iteration with gui


# pyautogui.click(x=1010, y=450) ### after first iteration with gui

# 862,347 last champion on gui
# 699,347
# 535,346
# 376,346
# 211,346 first champion on gui



# championToBuyPositionOnGUI = [ (210,345), (375,345), (535, 346), (700, 345), (860,345)]

# championToBuyPositionOnGame = [ (600,975), (794,975), (984,975), (1173,975), (1363,975) ]

# time.sleep(2)

# try:
#     TFTDSSwindow.restore()
#     TFTDSSwindow.activate()
# except:
#     TFTDSSwindow.restore()


# gameWindow = pyautogui.getWindowsWithTitle("wind")[0]

# # for i in range(2,5,1):
#     time.sleep(1)
#     TFTDSSwindow.activate()
#     pyautogui.click(x=championToBuyPositionOnGUI[i][0], y=championToBuyPositionOnGUI[i][1])
#     time.sleep(1)
#     gameWindow.activate()
#     pyautogui.click(x=championToBuyPositionOnGame[i][0], y=championToBuyPositionOnGame[i][1])
    
    
    
# def click_on_champion_to_buy_on_GUI_then_click_on_champion_in_game(positionOnGUI=0,positionInGame=0,GUIwindow=TFTDSSwindow,inGameWindow=gameWindow):
#     time.sleep(1)
#     GUIwindow.activate()
#     pyautogui.click(x=championToBuyPositionOnGUI[positionOnGUI][0], y=championToBuyPositionOnGUI[positionOnGUI][1])
#     time.sleep(1)
#     inGameWindow.activate()
#     pyautogui.click(x=championToBuyPositionOnGame[positionInGame][0], y=championToBuyPositionOnGame[positionInGame][1])

# 600,975 ## first champion to buy in game
# 794,975
# 984,975
# 1173,975
# 1363,975 ## last champion to buy in game

