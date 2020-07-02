# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 10:54:45 2020

@author: Janusz
"""

import tkinter as tk
import random
from functools import partial


import collections
from enum import IntEnum
import operator



import pandas as pd


import skfuzzy as fuzz
from skfuzzy import control as ctrl
import numpy as np

from collections import namedtuple



def add(intVariable):
    intVariable.set(intVariable.get() + 1)
    return

def sub(intVariable):
    if intVariable.get() >0:
        intVariable.set(intVariable.get() - 1)









df = pd.read_csv("scaledChampionsdf.csv") 

df.drop('Unnamed: 0', axis=1, inplace=True)

originList = list(set(df.Origin))
originList.sort()

# for origin in originList:
#     print(origin+"Champs = list(df.query("+"'Origin == "+'"'+"%s"%origin+'"'+"').Champion)")

# print("OriginChampsFromDFList = [", end = ' ')
# for origin in originList:
#     print(origin+"Champs", end = ', ')
# print("]")  

AstroChamps = list(df.query('Origin == "Astro"').Champion)
BattlecastChamps = list(df.query('Origin == "Battlecast"').Champion)
CelestialChamps = list(df.query('Origin == "Celestial"').Champion)
ChronoChamps = list(df.query('Origin == "Chrono"').Champion)
CyberneticChamps = list(df.query('Origin == "Cybernetic"').Champion)
DarkStarChamps = list(df.query('Origin == "DarkStar"').Champion)
MechPilotChamps = list(df.query('Origin == "MechPilot"').Champion)
RebelChamps = list(df.query('Origin == "Rebel"').Champion)
SpacePirateChamps = list(df.query('Origin == "SpacePirate"').Champion)
StarGuardianChamps = list(df.query('Origin == "StarGuardian"').Champion)


classList = list(set(df.ClassPrimary))
classList.sort()

# for clas in classList:
#     print(clas+"Champs = list(df.query("+"'class == "+'"'+"%s"%clas+'"'+"').Champion)")

# print("classChampsFromDFList = [", end = ' ')
# for clas in classList:
#     print(clas+"Champs", end = ', ')
# print("]")  




BlademasterChamps = list(df.query('ClassPrimary == "Blademaster"').Champion)
BlasterChamps = list(df.query('ClassPrimary == "Blaster"').Champion)
BrawlerChamps = list(df.query('ClassPrimary == "Brawler"').Champion)
DemolitionistChamps = list(df.query('ClassPrimary == "Demolitionist"').Champion)
InfiltratorChamps = list(df.query('ClassPrimary == "Infiltrator"').Champion)
ManaReaverChamps = list(df.query('ClassPrimary == "Mana-Reaver"').Champion)
MercenaryChamps = list(df.query('ClassPrimary == "Mercenary"').Champion)
MysticChamps = list(df.query('ClassPrimary == "Mystic"').Champion)
ParagonChamps = list(df.query('ClassPrimary == "Paragon"').Champion)
ProtectorChamps = list(df.query('ClassPrimary == "Protector"').Champion)
SniperChamps = list(df.query('ClassPrimary == "Sniper"').Champion)
SorcererChamps = list(df.query('ClassPrimary == "Sorcerer"').Champion)
StarshipChamps = list(df.query('ClassPrimary == "Starship"').Champion)
VanguardChamps = list(df.query('ClassPrimary == "Vanguard"').Champion)
classChampsFromDFList = [BlademasterChamps, BlasterChamps, BrawlerChamps, 
                         DemolitionistChamps, InfiltratorChamps, ManaReaverChamps,
                         MercenaryChamps, MysticChamps, ParagonChamps, ProtectorChamps, 
                         SniperChamps, SorcererChamps, StarshipChamps, VanguardChamps ]





############### WINDOW THINGS


MainWindow = tk.Tk()
MainWindow.geometry('1600x800')
MainWindow.title('TFTDSS')



############### COUNTERS FOR HEARTS CARDS $$$$$$$$$$$$$$$$$$

# for champ in AstroChamps:
#     print("counter"+champ+"= tk.IntVar()")

# print("AstroCounters = [")
# for champ in AstroChamps:
#     print("counter"+champ,end = ", ")
# print("]")
# print()
    
# for champ in BattlecastChamps:
#     print("counter"+champ+"= tk.IntVar()")

# print("BattlecastCounters = [")
# for champ in BattlecastChamps:
#     print("counter"+champ,end = ", ")
# print("]")
# print()

    
# for champ in CelestialChamps:
#     print("counter"+champ+"= tk.IntVar()")

# print("CelestialCounters = [")
# for champ in CelestialChamps:
#     print("counter"+champ,end = ", ")
# print("]")
# print()

    
# for champ in ChronoChamps:
#     print("counter"+champ+"= tk.IntVar()")

# print("ChronoCounters = [")
# for champ in ChronoChamps:
#     print("counter"+champ,end = ", ")
# print("]")
# print()

    
# for champ in CyberneticChamps:
#     print("counter"+champ+"= tk.IntVar()")

# print("CyberneticCounters = [")
# for champ in CyberneticChamps:
#     print("counter"+champ,end = ", ")
# print("]")
# print()

    
# for champ in DarkStarChamps:
#     print("counter"+champ+"= tk.IntVar()")

# print("DarkStarCounters = [")
# for champ in DarkStarChamps:
#     print("counter"+champ,end = ", ")
# print("]")
# print()

    
# for champ in MechPilotChamps:
#     print("counter"+champ+"= tk.IntVar()")

# print("MechPilotCounters = [")
# for champ in MechPilotChamps:
#     print("counter"+champ,end = ", ")
# print("]")
# print()

    
# for champ in RebelChamps:
#     print("counter"+champ+"= tk.IntVar()")

# print("RebelCounters = [")
# for champ in RebelChamps:
#     print("counter"+champ,end = ", ")
# print("]")
# print()

    
# for champ in SpacePirateChamps:
#     print("counter"+champ+"= tk.IntVar()")

# print("SpacePirateCounters = [")
# for champ in SpacePirateChamps:
#     print("counter"+champ,end = ", ")
# print("]")
# print()

    
# for champ in StarGuardianChamps:
#     print("counter"+champ+"= tk.IntVar()")

# print("StarGuardianCounters = [")
# for champ in StarGuardianChamps:
#     print("counter"+champ,end = ", ")
# print("]")
# print()

    

counterBard= tk.IntVar()
counterGnar= tk.IntVar()
counterNautilus= tk.IntVar()
counterTeemo= tk.IntVar()

AstroCounters = [counterBard, counterGnar, counterNautilus, counterTeemo] 


counterCassiopeia= tk.IntVar()
counterIllaoi= tk.IntVar()
counterKogMaw= tk.IntVar()
counterNocturne= tk.IntVar()
counterUrgot= tk.IntVar()
counterViktor= tk.IntVar()

BattlecastCounters = [counterCassiopeia, counterIllaoi, counterKogMaw, 
                      counterNocturne, counterUrgot, counterViktor]



counterAshe= tk.IntVar()
counterLulu= tk.IntVar()
counterRakan= tk.IntVar()
counterXayah= tk.IntVar()
counterXinZhao= tk.IntVar()

CelestialCounters = [counterAshe, counterLulu, counterRakan, counterXayah, counterXinZhao ]



counterBlitzcrank= tk.IntVar()
counterCaitlyn= tk.IntVar()
counterEzreal= tk.IntVar()
counterRiven= tk.IntVar()
counterShen= tk.IntVar()
counterThresh= tk.IntVar()
counterTwistedFate= tk.IntVar()
counterWukong= tk.IntVar()

ChronoCounters = [counterBlitzcrank, counterCaitlyn, counterEzreal, counterRiven,
                  counterShen, counterThresh, counterTwistedFate, counterWukong ]




counterEkko= tk.IntVar()
counterFiora= tk.IntVar()
counterIrelia= tk.IntVar()
counterLeona= tk.IntVar()
counterLucian= tk.IntVar()
counterVayne= tk.IntVar()
counterVi= tk.IntVar()

CyberneticCounters = [counterEkko, counterFiora, counterIrelia, counterLeona,
                      counterLucian, counterVayne, counterVi ]



counterJarvanIV= tk.IntVar()
counterJhin= tk.IntVar()
counterKarma= tk.IntVar()
counterMordekaiser= tk.IntVar()
counterShaco= tk.IntVar()
counterXerath= tk.IntVar()

DarkStarCounters = [counterJarvanIV, counterJhin, counterKarma, counterMordekaiser,
                    counterShaco, counterXerath ]



counterAnnie= tk.IntVar()
counterFizz= tk.IntVar()
counterRumble= tk.IntVar()

MechPilotCounters = [counterAnnie, counterFizz, counterRumble ]



counterAurelionSol= tk.IntVar()
counterJinx= tk.IntVar()
counterMalphite= tk.IntVar()
counterMasterYi= tk.IntVar()
counterYasuo= tk.IntVar()
counterZed= tk.IntVar()
counterZiggs= tk.IntVar()

RebelCounters = [counterAurelionSol, counterJinx, counterMalphite, counterMasterYi,
                 counterYasuo, counterZed, counterZiggs ]




counterDarius= tk.IntVar()
counterGangplank= tk.IntVar()
counterGraves= tk.IntVar()
counterJayce= tk.IntVar()

SpacePirateCounters = [counterDarius, counterGangplank, counterGraves, counterJayce ]





counterAhri= tk.IntVar()
counterJanna= tk.IntVar()
counterNeeko= tk.IntVar()
counterPoppy= tk.IntVar()
counterSoraka= tk.IntVar()
counterSyndra= tk.IntVar()
counterZoe= tk.IntVar()

StarGuardianCounters = [counterAhri, counterJanna, counterNeeko, counterPoppy,
                        counterSoraka, counterSyndra, counterZoe ]




####################### COUNTERS for champions to buy


counterBuyBard= tk.IntVar()
counterBuyGnar= tk.IntVar()
counterBuyNautilus= tk.IntVar()
counterBuyTeemo= tk.IntVar()

AstroCountersBuy = [counterBuyBard, counterBuyGnar, counterBuyNautilus, counterBuyTeemo] 


counterBuyCassiopeia= tk.IntVar()
counterBuyIllaoi= tk.IntVar()
counterBuyKogMaw= tk.IntVar()
counterBuyNocturne= tk.IntVar()
counterBuyUrgot= tk.IntVar()
counterBuyViktor= tk.IntVar()

BattlecastCountersBuy = [counterBuyCassiopeia, counterBuyIllaoi, counterBuyKogMaw, 
                      counterBuyNocturne, counterBuyUrgot, counterBuyViktor]



counterBuyAshe= tk.IntVar()
counterBuyLulu= tk.IntVar()
counterBuyRakan= tk.IntVar()
counterBuyXayah= tk.IntVar()
counterBuyXinZhao= tk.IntVar()

CelestialCountersBuy = [counterBuyAshe, counterBuyLulu, counterBuyRakan, counterBuyXayah, counterBuyXinZhao ]



counterBuyBlitzcrank= tk.IntVar()
counterBuyCaitlyn= tk.IntVar()
counterBuyEzreal= tk.IntVar()
counterBuyRiven= tk.IntVar()
counterBuyShen= tk.IntVar()
counterBuyThresh= tk.IntVar()
counterBuyTwistedFate= tk.IntVar()
counterBuyWukong= tk.IntVar()

ChronoCountersBuy = [counterBuyBlitzcrank, counterBuyCaitlyn, counterBuyEzreal, counterBuyRiven,
                  counterBuyShen, counterBuyThresh, counterBuyTwistedFate, counterBuyWukong ]




counterBuyEkko= tk.IntVar()
counterBuyFiora= tk.IntVar()
counterBuyIrelia= tk.IntVar()
counterBuyLeona= tk.IntVar()
counterBuyLucian= tk.IntVar()
counterBuyVayne= tk.IntVar()
counterBuyVi= tk.IntVar()

CyberneticCountersBuy = [counterBuyEkko, counterBuyFiora, counterBuyIrelia, counterBuyLeona,
                      counterBuyLucian, counterBuyVayne, counterBuyVi ]



counterBuyJarvanIV= tk.IntVar()
counterBuyJhin= tk.IntVar()
counterBuyKarma= tk.IntVar()
counterBuyMordekaiser= tk.IntVar()
counterBuyShaco= tk.IntVar()
counterBuyXerath= tk.IntVar()

DarkStarCountersBuy = [counterBuyJarvanIV, counterBuyJhin, counterBuyKarma, counterBuyMordekaiser,
                    counterBuyShaco, counterBuyXerath ]



counterBuyAnnie= tk.IntVar()
counterBuyFizz= tk.IntVar()
counterBuyRumble= tk.IntVar()

MechPilotCountersBuy = [counterBuyAnnie, counterBuyFizz, counterBuyRumble ]



counterBuyAurelionSol= tk.IntVar()
counterBuyJinx= tk.IntVar()
counterBuyMalphite= tk.IntVar()
counterBuyMasterYi= tk.IntVar()
counterBuyYasuo= tk.IntVar()
counterBuyZed= tk.IntVar()
counterBuyZiggs= tk.IntVar()

RebelCountersBuy = [counterBuyAurelionSol, counterBuyJinx, counterBuyMalphite, counterBuyMasterYi,
                 counterBuyYasuo, counterBuyZed, counterBuyZiggs ]




counterBuyDarius= tk.IntVar()
counterBuyGangplank= tk.IntVar()
counterBuyGraves= tk.IntVar()
counterBuyJayce= tk.IntVar()

SpacePirateCountersBuy = [counterBuyDarius, counterBuyGangplank, counterBuyGraves, counterBuyJayce ]





counterBuyAhri= tk.IntVar()
counterBuyJanna= tk.IntVar()
counterBuyNeeko= tk.IntVar()
counterBuyPoppy= tk.IntVar()
counterBuySoraka= tk.IntVar()
counterBuySyndra= tk.IntVar()
counterBuyZoe= tk.IntVar()

StarGuardianCountersBuy = [counterBuyAhri, counterBuyJanna, counterBuyNeeko, counterBuyPoppy,
                        counterBuySoraka, counterBuySyndra, counterBuyZoe ]
















counterAstro= tk.IntVar()
counterBattlecast= tk.IntVar()
counterCelestial= tk.IntVar()
counterChrono= tk.IntVar()
counterCybernetic= tk.IntVar()
counterDarkStar= tk.IntVar()
counterMechPilot= tk.IntVar()
counterRebel= tk.IntVar()
counterSpacePirate= tk.IntVar()
counterStarGuardian= tk.IntVar()

OriginCounters = [counterAstro, counterBattlecast, counterCelestial, counterChrono,
                  counterCybernetic, counterDarkStar, counterMechPilot, counterRebel,
                  counterSpacePirate, counterStarGuardian]



OriginNames = sorted(list(set(df.Origin)))

ClassPrimaryNames = sorted(list(set(df.ClassPrimary)))


counterBlademaster = tk.IntVar()
counterBlaster = tk.IntVar()
counterBrawler = tk.IntVar()
counterDemolitionist = tk.IntVar()
counterInfiltrator = tk.IntVar()
counterManaReaver = tk.IntVar()
counterMercenary = tk.IntVar()
counterMystic = tk.IntVar()
counterParagon = tk.IntVar()
counterProtector = tk.IntVar()
counterSniper = tk.IntVar()
counterSorcerer = tk.IntVar()
counterStarship = tk.IntVar()
counterVanguard = tk.IntVar()





############# manually added secondary counters

BlademasterCounters = [counterFiora, counterMasterYi, counterRiven, counterShen, 
                      counterXayah, counterYasuo ]

BlasterCounters = [counterEzreal, counterGraves, counterJinx, counterKogMaw, counterLucian ]

BrawlerCounters = [counterBlitzcrank, counterGnar, counterIllaoi, counterMalphite, 
                  counterVi ]

DemolitionistCounters = [counterRumble, counterZiggs, counterGangplank ]

InfiltratorCounters = [counterEkko, counterFizz, counterNocturne, counterShaco,
                      counterZed ]

ManaReaverCounters = [counterDarius, counterIrelia, counterThresh ]

MercenaryCounters = [counterGangplank ]

MysticCounters = [counterBard, counterCassiopeia, counterKarma, counterLulu,
                 counterSoraka ]

ParagonCounters = [counterJanna ]

ProtectorCounters = [counterJarvanIV, counterNeeko, counterRakan, counterUrgot,
                    counterXinZhao ]

SniperCounters = [counterAshe, counterCaitlyn, counterJhin, counterTeemo,
                 counterVayne ]

SorcererCounters = [counterAhri, counterAnnie, counterSyndra, counterTwistedFate,
                   counterViktor, counterXerath, counterZoe ]

StarshipCounters = [counterAurelionSol ]

VanguardCounters = [counterJayce, counterLeona, counterMordekaiser, 
                   counterNautilus, counterPoppy, counterWukong ]



ClassPrimaryCounters = [counterBlademaster, counterBlaster, counterBrawler, 
                        counterDemolitionist, counterInfiltrator, counterManaReaver, 
                        counterMercenary, counterMystic, counterParagon, counterProtector, 
                        counterSniper, counterSorcerer, counterStarship, counterVanguard ]


ClassPrimaryCountersList = [BlademasterCounters, BlasterCounters, BrawlerCounters, 
                        DemolitionistCounters, InfiltratorCounters, ManaReaverCounters, 
                        MercenaryCounters, MysticCounters, ParagonCounters, ProtectorCounters, 
                        SniperCounters, SorcererCounters, StarshipCounters, VanguardCounters ]
# for i,championlist in enumerate(classChampsFromDFList):
#     print(ClassPrimaryNames[i]+"Counters" + " = [")
#     for champ in championlist:
#         print("counter"+champ,end = ", ")
#     print("]")
#     print()



# print("ClassPrimaryCounters = [")
# for clas in ClassPrimaryNames:
#     print("counter" + clas, end = ", ")
# print("]")

# for clas in ClassPrimaryNames:
#     print("counter" + clas +" = tk.IntVar()")


# ClassSecondaryNames = sorted(list(set(df.ClassSecondary)))


# ClassSecondaryCounters = [counterBlademaster, counterDemolitionist]
# print("ClassSecondaryCounters = [")
# for clas in ClassSecondaryNames:
#     print("counter" + clas, end = ", ")
# print("]")

# for clas in ClassSecondaryNames:
#     print("counter" + clas +" = tk.IntVar()")

Origin = namedtuple("Origin", ["Name", "Counter"])


Astro = Origin(OriginNames[0], OriginCounters[0])








OriginChampsFromDFList = [AstroChamps, BattlecastChamps, CelestialChamps, 
                          ChronoChamps, CyberneticChamps, DarkStarChamps, 
                          MechPilotChamps, RebelChamps, SpacePirateChamps,
                          StarGuardianChamps ]



OriginChampsCountersList = [AstroCounters, BattlecastCounters, CelestialCounters, 
                          ChronoCounters, CyberneticCounters, DarkStarCounters, 
                          MechPilotCounters, RebelCounters, SpacePirateCounters,
                          StarGuardianCounters ]



OriginChampsCountersBuyList = [AstroCountersBuy, BattlecastCountersBuy, CelestialCountersBuy, 
                          ChronoCountersBuy, CyberneticCountersBuy, DarkStarCountersBuy, 
                          MechPilotCountersBuy, RebelCountersBuy, SpacePirateCountersBuy,
                          StarGuardianCountersBuy ]


ChampsNames  = sum(OriginChampsFromDFList, [])

OriginChampsCountersList1d = sum(OriginChampsCountersList, [])

OriginChampsCountersBuyList1d = sum(OriginChampsCountersBuyList, [])


CHAMPIONFLAG =1
ORIGINFLAG =0

bonusPointsFromOrigin =[0] * 10

bonusPointsFromClass = [0] * 14

######### order as in GUI
df.sort_values(by=['Origin', 'Champion'], inplace = True)
df.reset_index(drop=True, inplace = True)

def show_champions_from_origin(originPositionInOriginList, OriginChampsFromDF, OriginCounterList, shiftBetweenUpsideDownside, flag = CHAMPIONFLAG):
    """Adding buttons and text labels for single Origin."""
    if flag == 1:
        labelTitle = tk.Label(MainWindow, text=originList[originPositionInOriginList]).grid(row=1+shiftBetweenUpsideDownside, column=OriginLabelPositionColumn*ShiftBetweenOrigins*originPositionInOriginList)

    for i,champ in enumerate(OriginChampsFromDF):
        labelTitle = tk.Label(MainWindow, text=champ).grid(row=2+i+shiftBetweenUpsideDownside, column=OriginLabelPositionColumn*ShiftBetweenOrigins*originPositionInOriginList)
        entryNum = tk.Entry(MainWindow, textvariable=OriginCounterList[i], width = 2).grid(row=2+i+shiftBetweenUpsideDownside, column=ShiftBetweenOrigins*originPositionInOriginList+1)
        buttonCal = tk.Button(MainWindow, text="+", command=lambda counter=OriginCounterList[i]:add(counter)).grid(row=2+i+shiftBetweenUpsideDownside, column=ShiftBetweenOrigins*originPositionInOriginList+2)
        buttonCal = tk.Button(MainWindow, text="-", command=lambda counter=OriginCounterList[i]:sub(counter)).grid(row=2+i+shiftBetweenUpsideDownside, column=ShiftBetweenOrigins*originPositionInOriginList+3)
    return







def reset_counters_2dlist(list2d=OriginChampsCountersBuyList):
    """Reset counters, used when roll or new round starts."""
    list1d = sum(list2d, [])
    for champCounter in list1d:
        champCounter.set(0)
        
    delete_all_buttons()
    return

def check_nonzero_counters(list2d=OriginChampsCountersBuyList):
    nonzeroCountersList = []
    nonzeroCountersNumberList = []
    list1d = sum(list2d, [])
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
    print("This is nonzero Counter list:")
    print(nonzeroCountersList)
    print(nonzeroCountersNumberList)
    return nonzeroCountersNumberList
    





def show_nonzero_counters(rowOffset=0):
    global buttonCalcList
    buttonCalcList =[0] *5
    u =check_nonzero_counters()
    print("THIS IS U ", u)
    for i in range(0,len(u),1):
        # print("Thats the input to add",select_counter(cardsLeft[i]))
        buttonCalcList[i] = tk.Button(MainWindow, text=(df.Champion[u[i]]), command=lambda i = i:[add(OriginChampsCountersList1d[u[i]]), delete_button(i), sub(OriginChampsCountersBuyList1d[u[i]])])
        buttonCalcList[i].grid(row=12+rowOffset, column=ShiftBetweenOrigins*(i+1))
        
    # print(pd.DataFrame(cardsToBeButtons, columns=Card._fields))
    return    
    




def show_points_for_nonzero_counters(rowOffset=2):
    global textLabelList
    textLabelList =[0] *5
    u =check_nonzero_counters()
    for i in range(0,len(u),1):
        points = (df.Points[u[i]] + additional_points_from_origin_combo(u[i]) 
                  + additional_points_from_class_combo(u[i]) + additional_points_from_champions_in_pool(u[i]))
        # if u
        textLabelList[i] = tk.Label(MainWindow, text=points).grid(row=12+rowOffset, column=ShiftBetweenOrigins*(i+1))



def show_nonzero_counters_with_points(rowOffset1= 0, rowOffset2 =2):
    update_classes_and_origins()
    show_nonzero_counters(rowOffset1)
    show_points_for_nonzero_counters(rowOffset2)



def update_origins():
    for i,origin in enumerate(OriginChampsCountersList):
        count = 0
        for champ in origin:
            if champ.get() >= 1:
                count = count + 1
        OriginCounters[i].set(count)
        bonusPointsFromOrigin[i] = count * 0.2        
            
        
# def update_classes():
#     for i,champ in enumerate(OriginChampsCountersList1d):
#         count = 0
#         pos = ClassPrimaryNames.index(df.ClassPrimary[i])
#         print(pos)

#         if champ.get() >= 1:
#             count = count + 1
#         ClassPrimaryCounters[pos].set(count)
#         #bonusPointsFromOrigin[i] = count * 0.2  


ClassPrimaryCounters

def update_classes():
    for i,origin in enumerate(ClassPrimaryCountersList):
        count = 0
        for champ in origin:
            if champ.get() >= 1:
                count = count + 1
        ClassPrimaryCounters[i].set(count)
        bonusPointsFromClass[i] = count * 0.2 

        
def update_classes_and_origins():
    update_origins()
    update_classes()        
        

def additional_points_from_origin_combo(championNumber):
    pos = OriginNames.index(df.Origin[championNumber])
    print("bonusPointsFromOrigin[pos] ",bonusPointsFromOrigin[pos])
    return bonusPointsFromOrigin[pos]

def additional_points_from_class_combo(championNumber):
    pos = ClassPrimaryNames.index(df.ClassPrimary[championNumber])
    if df.ClassSecondary[championNumber] == ("Demolitionist" or "Blademaster"):
        pos2 = ClassPrimaryNames.index(df.ClassSecondary[championNumber])
        return bonusPointsFromClass[pos]  + bonusPointsFromClass[pos2]  
    #print("bonusPointsFromClass[pos] ",bonusPointsFromClass[pos])
    else:
        return bonusPointsFromClass[pos]  



def additional_points_from_champions_in_pool(championNumber):
    bonusPointsFromChampionPool = (OriginChampsCountersList1d[championNumber].get() -1) * 0.2
    print("bonusPointsFromChampionPool[pos] ",bonusPointsFromChampionPool)
    return bonusPointsFromChampionPool

    
def delete_button(position):
    buttonCalcList[position].destroy()

def delete_all_buttons():
    for button in buttonCalcList:
        button.destroy()

ShiftBetweenOrigins = 6

OriginLabelPositionColumn = 1


UPSIDE = 0 ############# champion pool
DOWNSIDE = 16################ champions to buy





labelTitle = tk.Label(MainWindow, text="Champion pool").grid(row=0, column=ShiftBetweenOrigins*5)

labelTitle = tk.Label(MainWindow, text=originList[0]).grid(row=1, column=OriginLabelPositionColumn)

# for i,champ in enumerate(AstroChamps):
#     labelTitle = tk.Label(MainWindow, text=champ).grid(row=2+i, column=0)
#     entryNum = tk.Entry(MainWindow, textvariable=AstroCounters[i], width = 2).grid(row=2+i, column=1)
#     buttonCal = tk.Button(MainWindow, text="+", command=lambda counter=AstroCounters[i]:add(counter)).grid(row=2+i, column=3)
#     buttonCal = tk.Button(MainWindow, text="-", command=lambda counter=AstroCounters[i]:sub(counter)).grid(row=2+i, column=4)

 # show_champions_from_origin(4, OriginChampsFromDFList[4], OriginChampsCountersList[4], positionInList)



# labelTitle = tk.Label(MainWindow, text=originList[1]).grid(row=1, column=OriginLabelPositionColumn*ShiftBetweenOrigins)

# for i,champ in enumerate(BattlecastChamps):
#     labelTitle = tk.Label(MainWindow, text=champ).grid(row=2+i, column=OriginLabelPositionColumn*ShiftBetweenOrigins-1)
#     entryNum = tk.Entry(MainWindow, textvariable=BattlecastCounters[i], width = 2).grid(row=2+i, column=ShiftBetweenOrigins+1)
#     buttonCal = tk.Button(MainWindow, text="+", command=lambda counter=BattlecastCounters[i]:add(counter)).grid(row=2+i, column=ShiftBetweenOrigins+2)
#     buttonCal = tk.Button(MainWindow, text="-", command=lambda counter=BattlecastCounters[i]:sub(counter)).grid(row=2+i, column=ShiftBetweenOrigins+3)




# labelTitle = tk.Label(MainWindow, text=originList[2]).grid(row=1, column=OriginLabelPositionColumn*ShiftBetweenOrigins*2)

# for i,champ in enumerate(CelestialChamps):
#     labelTitle = tk.Label(MainWindow, text=champ).grid(row=2+i, column=OriginLabelPositionColumn*ShiftBetweenOrigins*2-1)
#     entryNum = tk.Entry(MainWindow, textvariable=CelestialCounters[i], width = 2).grid(row=2+i, column=ShiftBetweenOrigins*2+1)
#     buttonCal = tk.Button(MainWindow, text="+", command=lambda counter=CelestialCounters[i]:add(counter)).grid(row=2+i, column=ShiftBetweenOrigins*2+2)
#     buttonCal = tk.Button(MainWindow, text="-", command=lambda counter=CelestialCounters[i]:sub(counter)).grid(row=2+i, column=ShiftBetweenOrigins*2+3)


labelTitle = tk.Label(MainWindow, text="Champions to buy").grid(row=DOWNSIDE-1, column=ShiftBetweenOrigins*5)


###### champions
for i in range(0, len(OriginChampsFromDFList),1):
    show_champions_from_origin(i, OriginChampsFromDFList[i], OriginChampsCountersList[i], UPSIDE)

for i in range(0, len(OriginChampsFromDFList),1):
    show_champions_from_origin(i, OriginChampsFromDFList[i], OriginChampsCountersBuyList[i], DOWNSIDE)
    
####origins
show_champions_from_origin(11,OriginNames, OriginCounters, UPSIDE,ORIGINFLAG)    

#### primary class
show_champions_from_origin(12, ClassPrimaryNames, ClassPrimaryCounters, UPSIDE, ORIGINFLAG )
labeling = tk.Label(MainWindow, text="Left to buy").grid(row=12+0, column=0)

labeling = tk.Label(MainWindow, text="Points").grid(row=14+0, column=0)



buttonCal = tk.Button(MainWindow, text="reset", command=lambda:reset_counters_2dlist(OriginChampsCountersBuyList)).grid(row=DOWNSIDE, column=6)


# buttonCal = tk.Button(MainWindow, text="nonzero", command=lambda:check_nonzero_counters(OriginChampsCountersBuyList)).grid(row=DOWNSIDE, column=12)

# buttonCal = tk.Button(MainWindow, text="Shownonzero", command=lambda:show_nonzero_counters(0)).grid(row=DOWNSIDE, column=18)

# buttonCal = tk.Button(MainWindow, text="Showpoints", command=lambda:show_points_for_nonzero_counters(2)).grid(row=DOWNSIDE, column=24)

# buttonCal = tk.Button(MainWindow, text="update", command=lambda:update_origins()).grid(row=DOWNSIDE, column=30)



# buttonCal = tk.Button(MainWindow, text="updateC", command=lambda:update_classes()).grid(row=DOWNSIDE, column=36)


buttonCal = tk.Button(MainWindow, text="update classes", command=lambda:update_classes_and_origins()).grid(row=DOWNSIDE, column=12)

buttonCal = tk.Button(MainWindow, text="show points", command=lambda:show_nonzero_counters_with_points()).grid(row=DOWNSIDE, column=18)



MainWindow.attributes('-alpha', 0.9)
MainWindow.mainloop()
