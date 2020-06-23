# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 10:54:45 2020

@author: Janusz
"""

import pandas as pd 

from collections import namedtuple


data = pd.read_csv("championsData.csv") 



############### Need to add effective HP

#### formula for dmg reduction is: armor/(100+armor)



## from lol wiki

###physical effective health =  health  × (1 + 0.01 × armor)
###magical effective health =  health  × (1 + 0.01 × MR)


PHP = []
MHP = []
MEANHP = []
for i in range(0,len(data),1):
    PHP.append(data.HP[i] * (1 + 0.01 * data.Armor[i]))
    MHP.append(data.HP[i] * (1 + 0.01 * data.MR[i]))
    MEANHP.append((PHP[i]+MHP[i])/2)


data.insert(7,"PHP",PHP)
data.insert(8,"MHP",MHP)
data.insert(9,"MEANHP",MEANHP)



Champion = namedtuple('Champ', ['Champion', 'DPS', 'AS', 'DMG', 'Range', 'HP', 
                                'PHP', 'MHP', 'MEANHP', 'Mana', 'Armor', 'MR', 
                                'Origin', 'ClassPrimary', 'ClassSecondary', 'Cost'])

dataList = data.T.values.tolist()

for i,name in enumerate(dataList[1]): 
    print(name, end='')
    print(' = ScaledChampion(*data.loc[%d][1:])'%i)
    
    
    
    
    
 ####################### Champions   
Ahri = Champion(*data.loc[0][1:])
Annie = Champion(*data.loc[1][1:])
Ashe = Champion(*data.loc[2][1:])
AurelionSol = Champion(*data.loc[3][1:])
Bard = Champion(*data.loc[4][1:])
Blitzcrank = Champion(*data.loc[5][1:])
Caitlyn = Champion(*data.loc[6][1:])
Cassiopeia = Champion(*data.loc[7][1:])
Darius = Champion(*data.loc[8][1:])
Ekko = Champion(*data.loc[9][1:])
Ezreal = Champion(*data.loc[10][1:])
Fiora = Champion(*data.loc[11][1:])
Fizz = Champion(*data.loc[12][1:])
Gangplank = Champion(*data.loc[13][1:])
Gnar = Champion(*data.loc[14][1:])
Graves = Champion(*data.loc[15][1:])
Illaoi = Champion(*data.loc[16][1:])
Irelia = Champion(*data.loc[17][1:])
Janna = Champion(*data.loc[18][1:])
JarvanIV = Champion(*data.loc[19][1:])
Jayce = Champion(*data.loc[20][1:])
Jhin = Champion(*data.loc[21][1:])
Jinx = Champion(*data.loc[22][1:])
Karma = Champion(*data.loc[23][1:])
KogMaw = Champion(*data.loc[24][1:])
Leona = Champion(*data.loc[25][1:])
Lucian = Champion(*data.loc[26][1:])
Lulu = Champion(*data.loc[27][1:])
Malphite = Champion(*data.loc[28][1:])
MasterYi = Champion(*data.loc[29][1:])
Mordekaiser = Champion(*data.loc[30][1:])
Nautilus = Champion(*data.loc[31][1:])
Neeko = Champion(*data.loc[32][1:])
Nocturne = Champion(*data.loc[33][1:])
Poppy = Champion(*data.loc[34][1:])
Rakan = Champion(*data.loc[35][1:])
Riven = Champion(*data.loc[36][1:])
Rumble = Champion(*data.loc[37][1:])
Shaco = Champion(*data.loc[38][1:])
Shen = Champion(*data.loc[39][1:])
Soraka = Champion(*data.loc[40][1:])
Syndra = Champion(*data.loc[41][1:])
Teemo = Champion(*data.loc[42][1:])
Thresh = Champion(*data.loc[43][1:])
TwistedFate = Champion(*data.loc[44][1:])
Urgot = Champion(*data.loc[45][1:])
Vayne = Champion(*data.loc[46][1:])
Vi = Champion(*data.loc[47][1:])
Viktor = Champion(*data.loc[48][1:])
Wukong = Champion(*data.loc[49][1:])
Xayah = Champion(*data.loc[50][1:])
Xerath = Champion(*data.loc[51][1:])
XinZhao = Champion(*data.loc[52][1:])
Yasuo = Champion(*data.loc[53][1:])
Zed = Champion(*data.loc[54][1:])
Ziggs = Champion(*data.loc[55][1:])
Zoe = Champion(*data.loc[56][1:])






for i,name in enumerate(dataList[1]): ######## wasted 2 hours for searching answer how to create variable variable
    print(name, end=', ')


championList = [Ahri, Annie, Ashe, AurelionSol, Bard, Blitzcrank, Caitlyn, 
                Cassiopeia, Darius, Ekko, Ezreal, Fiora, Fizz, Gangplank, 
                Gnar, Graves, Illaoi, Irelia, Janna, JarvanIV, Jayce, Jhin, 
                Jinx, Karma, KogMaw, Leona, Lucian, Lulu, Malphite, MasterYi, 
                Mordekaiser, Nautilus, Neeko, Nocturne, Poppy, Rakan, Riven, 
                Rumble, Shaco, Shen, Soraka, Syndra, Teemo, Thresh, 
                TwistedFate, Urgot, Vayne, Vi, Viktor, Wukong, Xayah, 
                Xerath, XinZhao, Yasuo, Zed, Ziggs, Zoe]










##############################################
### Performance calculation
##############################################









#### Max stats

### misconception

# DPSMAX = max(championList, key=lambda k: k.DPS).DPS

# ASMAX = max(championList, key=lambda k: k.AS).AS

# DMGMAX = max(championList, key=lambda k: k.DMG).DMG

# RANGEMAX = max(championList, key=lambda k: k.Range).Range

# HPMAX = max(championList, key=lambda k: k.HP).HP

# MANAMAX = max(championList, key=lambda k: k.Mana).Mana

# ARMORMAX = max(championList, key=lambda k: k.Armor).Armor

# MRMAX = max(championList, key=lambda k: k.MR).MR




DPSMAX = max(data.DPS)

ASMAX = max(data.AS)

DMGMAX = max(data.DMG)

RANGEMAX = max(data.Range)

HPMAX = max(data.HP)

PHPMAX = max(data.PHP)

MHPMAX = max(data.MHP)

MEANHPMAX = max(data.MEANHP)

MANAMAX = max(data.Mana)

ARMORMAX = max(data.Armor)

MRMAX = max(data.MR)


##### Max stats list

maxStatsList = [DPSMAX, ASMAX, DMGMAX, RANGEMAX, HPMAX, PHPMAX, MHPMAX, 
                MEANHPMAX, MANAMAX, ARMORMAX, MRMAX]


############################################
#### Scaling champions stats to 0.0-1.0
############################################



for i,maxstat in enumerate(maxStatsList):
    data[data.columns[i+2]] = data[data.columns[i+2]]/maxstat
    print(data[data.columns[i+2]])
    print("The end of this stat")







ScaledChampion = namedtuple('ScaledChamp', ['Champion', 'DPS', 'AS', 'DMG', 
                                            'Range', 'HP', 'PHP', 'MHP', 'MEANHP',
                                            'Mana', 'Armor', 'MR', 'Origin', 
                                            'ClassPrimary', 'ClassSecondary', 'Cost'])




for i,name in enumerate(dataList[1]): 
    print('S'+name, end='')
    print(' = ScaledChampion(*data.loc[%d][1:])'%i)








SAhri = ScaledChampion(*data.loc[0][1:])
SAnnie = ScaledChampion(*data.loc[1][1:])
SAshe = ScaledChampion(*data.loc[2][1:])
SAurelionSol = ScaledChampion(*data.loc[3][1:])
SBard = ScaledChampion(*data.loc[4][1:])
SBlitzcrank = ScaledChampion(*data.loc[5][1:])
SCaitlyn = ScaledChampion(*data.loc[6][1:])
SCassiopeia = ScaledChampion(*data.loc[7][1:])
SDarius = ScaledChampion(*data.loc[8][1:])
SEkko = ScaledChampion(*data.loc[9][1:])
SEzreal = ScaledChampion(*data.loc[10][1:])
SFiora = ScaledChampion(*data.loc[11][1:])
SFizz = ScaledChampion(*data.loc[12][1:])
SGangplank = ScaledChampion(*data.loc[13][1:])
SGnar = ScaledChampion(*data.loc[14][1:])
SGraves = ScaledChampion(*data.loc[15][1:])
SIllaoi = ScaledChampion(*data.loc[16][1:])
SIrelia = ScaledChampion(*data.loc[17][1:])
SJanna = ScaledChampion(*data.loc[18][1:])
SJarvanIV = ScaledChampion(*data.loc[19][1:])
SJayce = ScaledChampion(*data.loc[20][1:])
SJhin = ScaledChampion(*data.loc[21][1:])
SJinx = ScaledChampion(*data.loc[22][1:])
SKarma = ScaledChampion(*data.loc[23][1:])
SKogMaw = ScaledChampion(*data.loc[24][1:])
SLeona = ScaledChampion(*data.loc[25][1:])
SLucian = ScaledChampion(*data.loc[26][1:])
SLulu = ScaledChampion(*data.loc[27][1:])
SMalphite = ScaledChampion(*data.loc[28][1:])
SMasterYi = ScaledChampion(*data.loc[29][1:])
SMordekaiser = ScaledChampion(*data.loc[30][1:])
SNautilus = ScaledChampion(*data.loc[31][1:])
SNeeko = ScaledChampion(*data.loc[32][1:])
SNocturne = ScaledChampion(*data.loc[33][1:])
SPoppy = ScaledChampion(*data.loc[34][1:])
SRakan = ScaledChampion(*data.loc[35][1:])
SRiven = ScaledChampion(*data.loc[36][1:])
SRumble = ScaledChampion(*data.loc[37][1:])
SShaco = ScaledChampion(*data.loc[38][1:])
SShen = ScaledChampion(*data.loc[39][1:])
SSoraka = ScaledChampion(*data.loc[40][1:])
SSyndra = ScaledChampion(*data.loc[41][1:])
STeemo = ScaledChampion(*data.loc[42][1:])
SThresh = ScaledChampion(*data.loc[43][1:])
STwistedFate = ScaledChampion(*data.loc[44][1:])
SUrgot = ScaledChampion(*data.loc[45][1:])
SVayne = ScaledChampion(*data.loc[46][1:])
SVi = ScaledChampion(*data.loc[47][1:])
SViktor = ScaledChampion(*data.loc[48][1:])
SWukong = ScaledChampion(*data.loc[49][1:])
SXayah = ScaledChampion(*data.loc[50][1:])
SXerath = ScaledChampion(*data.loc[51][1:])
SXinZhao = ScaledChampion(*data.loc[52][1:])
SYasuo = ScaledChampion(*data.loc[53][1:])
SZed = ScaledChampion(*data.loc[54][1:])
SZiggs = ScaledChampion(*data.loc[55][1:])
SZoe = ScaledChampion(*data.loc[56][1:])









SchampionList = [SAhri, SAnnie, SAshe, SAurelionSol, SBard, SBlitzcrank, SCaitlyn, 
                SCassiopeia, SDarius, SEkko, SEzreal, SFiora, SFizz, SGangplank, 
                SGnar, SGraves, SIllaoi, SIrelia, SJanna, SJarvanIV, SJayce, SJhin, 
                SJinx, SKarma, SKogMaw, SLeona, SLucian, SLulu, SMalphite, SMasterYi, 
                SMordekaiser, SNautilus, SNeeko, SNocturne, SPoppy, SRakan, SRiven, 
                SRumble, SShaco, SShen, SSoraka, SSyndra, STeemo, SThresh, 
                STwistedFate, SUrgot, SVayne, SVi, SViktor, SWukong, SXayah, 
                SXerath, SXinZhao, SYasuo, SZed, SZiggs, SZoe]








