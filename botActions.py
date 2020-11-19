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




wincap = WindowCapture('League of Legends (TM) Client')

# wincap = None

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




def from_OCR_champions_to_buy_list_to_counter_index_list(OCRchampionsToBuyList=update_champions_to_buy_from_ocr_detection()):
    counterIndexList = []
    for detected in OCRchampionsToBuyList:
        counterIndexList.append(championListForOCR.index(detected))
        print("Index of detected champion in OCR: ",championListForOCR.index(detected))
        
    print("Should be max 5 items there !!!!!!!!!!!!!!! if not check from_OCR_champions_to_buy_list_to_counter_index_list: ",counterIndexList)
    return counterIndexList
        
        

def show_points_for_champions_to_buy(counterIndexListLocal=from_OCR_champions_to_buy_list_to_counter_index_list()):
    """It shows up champions POINTS to buy that counters are nonzero, as a text.
    Doesnt disappear currently, should be fixed.
    In: rowOffset by default = 0 for buttons row placement."""
    update_classes_and_origins()
    pointsForChampionsToBuy = [0] * 5
    for i in range(0,len(counterIndexListLocal),1):
        pointsForChampionsToBuy[i] = (df.Points[counterIndexListLocal[i]] + additional_points_from_origin_combo(counterIndexListLocal[i]) 
                  + additional_points_from_class_combo(counterIndexListLocal[i]) + additional_points_from_champions_in_pool(counterIndexListLocal[i]))
    return pointsForChampionsToBuy



championsToBuyIndexes = from_OCR_champions_to_buy_list_to_counter_index_list()
pointsForChampionsInGameToBuy = show_points_for_champions_to_buy()
print(pointsForChampionsInGameToBuy)

posOnScreen = [0, 1, 2, 3, 4]



def create_list_sorted_champions_to_buy_points_then_indexes_then_position_on_screen():
    #### https://stackoverflow.com/questions/6422700/how-to-get-indices-of-a-sorted-array-in-python

    championsToBuyPointsThenIndexesThenPositionOnScreen = []
    for i, point in enumerate(pointsForChampionsInGameToBuy):
        championsToBuyPointsThenIndexesThenPositionOnScreen.append([point, championsToBuyIndexes[i], posOnScreen[i]])
    
    sorted_inds, sorted_items = zip(*sorted([(i,e) for i,e in enumerate(championsToBuyPointsThenIndexesThenPositionOnScreen)], key=itemgetter(1), reverse=True))

    return sorted_items

SORTEDchampionsToBuyPointsThenIndexesThenPositionOnScreen = list(create_list_sorted_champions_to_buy_points_then_indexes_then_position_on_screen())




###################################################################################
############################## POINTS END ######################################
####################################################################################

#### update counters todo


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

def buy_best_available_champions_by_points(howMuchChampions=2, mousePathDelay=0.2):
    activate_game_window()
    
    for i in range(0,howMuchChampions,1):
        # pydirectinput.moveTo(100, 150) # Move the mouse to the x, y coordinates 100, 150.
        # pydirectinput.click() # Click the mouse at its current location.
        pyautogui.moveTo(x=championToBuyPositionOnGame[SORTEDchampionsToBuyPointsThenIndexesThenPositionOnScreen[i][2]][0], y=championToBuyPositionOnGame[SORTEDchampionsToBuyPointsThenIndexesThenPositionOnScreen[i][2]][1], duration=mousePathDelay)
        pyautogui.mouseDown()
        time.sleep(0.3)
        pyautogui.mouseUp()

        
        update_champion_counter(SORTEDchampionsToBuyPointsThenIndexesThenPositionOnScreen[i])


buy_best_available_champions_by_points()



# move from x to y

# move mouse to x
# click
# move mouse to y
# mouse down



def move_champion_from_x_to_y(startingPoint,metaPoint):
    activate_game_window()
    
    pyautogui.moveTo(x=startingPoint[0], y=startingPoint[1], duration=0.5)
    pyautogui.click()
    pyautogui.moveTo(x=metaPoint[0], y=metaPoint[1], duration=0.5)
    pyautogui.mouseDown()
    time.sleep(0.3)
    pyautogui.mouseUp()
    

move_champion_from_x_to_y(benchHexes[2],playgroundHexes[9])

move_champion_from_x_to_y(benchHexes[3],playgroundHexes[10])



move_champion_from_x_to_y(playgroundHexes[21],playgroundHexes[23])





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


