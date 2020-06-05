# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 10:54:45 2020

@author: Janusz
"""

import pandas as pd 

from collections import namedtuple


data = pd.read_csv("championsData.csv") 

Champion = namedtuple('Champ', ['Champion', 'DPS', 'AS', 'DMG', 'Range', 'HP', 'Mana', 'Armor', 'MR'])

dataList = data.T.values.tolist()

for i,name in enumerate(dataList[1]): 
    print(name, end='')
    print(' = Champion(*data.loc[%d][1:])'%i)
    
    
    
    
    
 ####################### Champions   
    
Ahri = Champion(*data.loc[0][1:])
Annie = Champion(*data.loc[1][1:])
Ashe = Champion(*data.loc[2][1:])
AurelionSol = Champion(*data.loc[3][1:])
Blitzcrank = Champion(*data.loc[4][1:])
Caitlyn = Champion(*data.loc[5][1:])
Chogath = Champion(*data.loc[6][1:])
Darius = Champion(*data.loc[7][1:])
Ekko = Champion(*data.loc[8][1:])
Ezreal = Champion(*data.loc[9][1:])
Fiora = Champion(*data.loc[10][1:])
Fizz = Champion(*data.loc[11][1:])
Gangplank = Champion(*data.loc[12][1:])
Graves = Champion(*data.loc[13][1:])
Irelia = Champion(*data.loc[14][1:])
JarvanIV = Champion(*data.loc[15][1:])
Jayce = Champion(*data.loc[16][1:])
Jhin = Champion(*data.loc[17][1:])
Jinx = Champion(*data.loc[18][1:])
Kaisa = Champion(*data.loc[19][1:])
Karma = Champion(*data.loc[20][1:])
Kassadin = Champion(*data.loc[21][1:])
Kayle = Champion(*data.loc[22][1:])
Khazix = Champion(*data.loc[23][1:])
Leona = Champion(*data.loc[24][1:])
Lucian = Champion(*data.loc[25][1:])
Lulu = Champion(*data.loc[26][1:])
Lux = Champion(*data.loc[27][1:])
Malphite = Champion(*data.loc[28][1:])
MasterYi = Champion(*data.loc[29][1:])
MissFortune = Champion(*data.loc[30][1:])
Mordekaiser = Champion(*data.loc[31][1:])
Neeko = Champion(*data.loc[32][1:])
Poppy = Champion(*data.loc[33][1:])
Rakan = Champion(*data.loc[34][1:])
Rumble = Champion(*data.loc[35][1:])
Shaco = Champion(*data.loc[36][1:])
Shen = Champion(*data.loc[37][1:])
Sona = Champion(*data.loc[38][1:])
Soraka = Champion(*data.loc[39][1:])
Syndra = Champion(*data.loc[40][1:])
Thresh = Champion(*data.loc[41][1:])
TwistedFate = Champion(*data.loc[42][1:])
Velkoz = Champion(*data.loc[43][1:])
Vi = Champion(*data.loc[44][1:])
Wukong = Champion(*data.loc[45][1:])
Xayah = Champion(*data.loc[46][1:])
Xerath = Champion(*data.loc[47][1:])
XinZhao = Champion(*data.loc[48][1:])
Yasuo = Champion(*data.loc[49][1:])
Ziggs = Champion(*data.loc[50][1:])
Zoe = Champion(*data.loc[51][1:])







for i,name in enumerate(dataList[1]): ######## wasted 2 hours for searching answer how to create variable variable
    print(name, end=', ')


championList = [Ahri, Annie, Ashe, AurelionSol, Blitzcrank, Caitlyn, Chogath, 
                Darius, Ekko, Ezreal, Fiora, Fizz, Gangplank, Graves, Irelia, 
                JarvanIV, Jayce, Jhin, Jinx, Kaisa, Karma, Kassadin, Kayle, 
                Khazix, Leona, Lucian, Lulu, Lux, Malphite, MasterYi, 
                MissFortune, Mordekaiser, Neeko, Poppy, Rakan, Rumble, Shaco, 
                Shen, Sona, Soraka, Syndra, Thresh, TwistedFate, Velkoz, Vi,
                Wukong, Xayah, Xerath, XinZhao, Yasuo, Ziggs, Zoe]


