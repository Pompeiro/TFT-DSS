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

for champ in AstroChamps:
    print("counter"+champ,end = ", ")
    
for champ in BattlecastChamps:
    print("counter"+champ+"= tk.IntVar()")

for champ in BattlecastChamps:
    print("counter"+champ,end = ", ")
    

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





OriginLabelPositionColumn = 1

labelTitle = tk.Label(MainWindow, text="Champion pool").grid(row=0, column=11)

labelTitle = tk.Label(MainWindow, text=originList[0]).grid(row=1, column=OriginLabelPositionColumn)

for i,champ in enumerate(AstroChamps):
    labelTitle = tk.Label(MainWindow, text=champ).grid(row=2+i, column=0)
    entryNum = tk.Entry(MainWindow, textvariable=AstroCounters[i], width = 2).grid(row=2+i, column=1)
    buttonCal = tk.Button(MainWindow, text="+", command=lambda counter=AstroCounters[i]:add(counter)).grid(row=2+i, column=3)
    buttonCal = tk.Button(MainWindow, text="-", command=lambda counter=AstroCounters[i]:sub(counter)).grid(row=2+i, column=4)





labelTitle = tk.Label(MainWindow, text=originList[1]).grid(row=1, column=OriginLabelPositionColumn*6)

for i,champ in enumerate(BattlecastChamps):
    labelTitle = tk.Label(MainWindow, text=champ).grid(row=2+i, column=OriginLabelPositionColumn*6-1)
    entryNum = tk.Entry(MainWindow, textvariable=BattlecastCounters[i], width = 2).grid(row=2+i, column=7)
    buttonCal = tk.Button(MainWindow, text="+", command=lambda counter=BattlecastCounters[i]:add(counter)).grid(row=2+i, column=9)
    buttonCal = tk.Button(MainWindow, text="-", command=lambda counter=BattlecastCounters[i]:sub(counter)).grid(row=2+i, column=10)



labelTitle = tk.Label(MainWindow, text="Champions to buy").grid(row=15, column=11)



MainWindow.mainloop()
