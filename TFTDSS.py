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

for origin in originList:
    print(origin+"Champs = list(df.query("+"'Origin == "+'"'+"%s"%origin+'"'+"').Champion)")

print("OriginChampsFromDFList = [", end = ' ')
for origin in originList:
    print(origin+"Champs", end = ', ')
print("]")  

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












############### WINDOW THINGS


MainWindow = tk.Tk()
MainWindow.geometry('1600x800')
MainWindow.title('TFTDSS')



############### COUNTERS FOR HEARTS CARDS $$$$$$$$$$$$$$$$$$

for champ in AstroChamps:
    print("counter"+champ+"= tk.IntVar()")

print("AstroCounters = [")
for champ in AstroChamps:
    print("counter"+champ,end = ", ")
print("]")
print()
    
for champ in BattlecastChamps:
    print("counter"+champ+"= tk.IntVar()")

print("BattlecastCounters = [")
for champ in BattlecastChamps:
    print("counter"+champ,end = ", ")
print("]")
print()

    
for champ in CelestialChamps:
    print("counter"+champ+"= tk.IntVar()")

print("CelestialCounters = [")
for champ in CelestialChamps:
    print("counter"+champ,end = ", ")
print("]")
print()

    
for champ in ChronoChamps:
    print("counter"+champ+"= tk.IntVar()")

print("ChronoCounters = [")
for champ in ChronoChamps:
    print("counter"+champ,end = ", ")
print("]")
print()

    
for champ in CyberneticChamps:
    print("counter"+champ+"= tk.IntVar()")

print("CyberneticCounters = [")
for champ in CyberneticChamps:
    print("counter"+champ,end = ", ")
print("]")
print()

    
for champ in DarkStarChamps:
    print("counter"+champ+"= tk.IntVar()")

print("DarkStarCounters = [")
for champ in DarkStarChamps:
    print("counter"+champ,end = ", ")
print("]")
print()

    
for champ in MechPilotChamps:
    print("counter"+champ+"= tk.IntVar()")

print("MechPilotCounters = [")
for champ in MechPilotChamps:
    print("counter"+champ,end = ", ")
print("]")
print()

    
for champ in RebelChamps:
    print("counter"+champ+"= tk.IntVar()")

print("RebelCounters = [")
for champ in RebelChamps:
    print("counter"+champ,end = ", ")
print("]")
print()

    
for champ in SpacePirateChamps:
    print("counter"+champ+"= tk.IntVar()")

print("SpacePirateCounters = [")
for champ in SpacePirateChamps:
    print("counter"+champ,end = ", ")
print("]")
print()

    
for champ in StarGuardianChamps:
    print("counter"+champ+"= tk.IntVar()")

print("StarGuardianCounters = [")
for champ in StarGuardianChamps:
    print("counter"+champ,end = ", ")
print("]")
print()

    

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


def show_champions_from_origin(originPositionInOriginList, OriginChampsFromDF, OriginCounterList, shiftBetweenUpsideDownside):
    labelTitle = tk.Label(MainWindow, text=originList[originPositionInOriginList]).grid(row=1+shiftBetweenUpsideDownside, column=OriginLabelPositionColumn*ShiftBetweenOrigins*originPositionInOriginList)

    for i,champ in enumerate(OriginChampsFromDF):
        labelTitle = tk.Label(MainWindow, text=champ).grid(row=2+i+shiftBetweenUpsideDownside, column=OriginLabelPositionColumn*ShiftBetweenOrigins*originPositionInOriginList)
        entryNum = tk.Entry(MainWindow, textvariable=OriginCounterList[i], width = 2).grid(row=2+i+shiftBetweenUpsideDownside, column=ShiftBetweenOrigins*originPositionInOriginList+1)
        buttonCal = tk.Button(MainWindow, text="+", command=lambda counter=OriginCounterList[i]:add(counter)).grid(row=2+i+shiftBetweenUpsideDownside, column=ShiftBetweenOrigins*originPositionInOriginList+2)
        buttonCal = tk.Button(MainWindow, text="-", command=lambda counter=OriginCounterList[i]:sub(counter)).grid(row=2+i+shiftBetweenUpsideDownside, column=ShiftBetweenOrigins*originPositionInOriginList+3)
    return



ShiftBetweenOrigins = 6

OriginLabelPositionColumn = 1


UPSIDE = 0 ############# champion pool
DOWNSIDE = 15################ champions to buy







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


labelTitle = tk.Label(MainWindow, text="Champions to buy").grid(row=DOWNSIDE, column=ShiftBetweenOrigins*5)



for i in range(0, len(OriginChampsFromDFList),1):
    show_champions_from_origin(i, OriginChampsFromDFList[i], OriginChampsCountersList[i], UPSIDE)

for i in range(0, len(OriginChampsFromDFList),1):
    show_champions_from_origin(i, OriginChampsFromDFList[i], OriginChampsCountersBuyList[i], DOWNSIDE)


MainWindow.mainloop()
