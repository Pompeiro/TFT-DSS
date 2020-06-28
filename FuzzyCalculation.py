# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 11:39:30 2020

@author: Janusz
"""
import pandas as pd

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


from collections import namedtuple


df = pd.read_csv("championsData.csv") 

df.drop('Unnamed: 0', axis=1, inplace=True)

############### Need to add effective HP

#### formula for dmg reduction is: armor/(100+armor)



## from lol wiki

###physical effective health =  health  × (1 + 0.01 × armor)
###magical effective health =  health  × (1 + 0.01 × MR)


### formula for updated PHP after picking up bonus armor for combo or item
### Wukong.PHP/Wukong.HP+BonusArmor/100 


PHP = []
MHP = []
MEANHP = []
for i in range(0,len(df),1):
    PHP.append(df.HP[i] * (1 + 0.01 * df.Armor[i]))
    MHP.append(df.HP[i] * (1 + 0.01 * df.MR[i]))
    MEANHP.append((PHP[i]+MHP[i])/2)


df.insert(6,"PHP",PHP)
df.insert(7,"MHP",MHP)
df.insert(8,"MEANHP",MEANHP)



Champion = namedtuple('Champ', ['Champion', 'DPS', 'AS', 'DMG', 'Range', 'HP', 
                                'PHP', 'MHP', 'MEANHP', 'Mana', 'Armor', 'MR', 
                                'Origin', 'ClassPrimary', 'ClassSecondary', 'Cost',
                                'Tier'])

dfList = df.T.values.tolist()

for i,name in enumerate(dfList[1]): 
    print(name, end='')
    print(' = ScaledChampion(*df.loc[%d][0:])'%i)
    
    
    
    
    
 ####################### Champions   
Ahri = Champion(*df.loc[0][0:])
Annie = Champion(*df.loc[1][0:])
Ashe = Champion(*df.loc[2][0:])
AurelionSol = Champion(*df.loc[3][0:])
Bard = Champion(*df.loc[4][0:])
Blitzcrank = Champion(*df.loc[5][0:])
Caitlyn = Champion(*df.loc[6][0:])
Cassiopeia = Champion(*df.loc[7][0:])
Darius = Champion(*df.loc[8][0:])
Ekko = Champion(*df.loc[9][0:])
Ezreal = Champion(*df.loc[10][0:])
Fiora = Champion(*df.loc[11][0:])
Fizz = Champion(*df.loc[12][0:])
Gangplank = Champion(*df.loc[13][0:])
Gnar = Champion(*df.loc[14][0:])
Graves = Champion(*df.loc[15][0:])
Illaoi = Champion(*df.loc[16][0:])
Irelia = Champion(*df.loc[17][0:])
Janna = Champion(*df.loc[18][0:])
JarvanIV = Champion(*df.loc[19][0:])
Jayce = Champion(*df.loc[20][0:])
Jhin = Champion(*df.loc[21][0:])
Jinx = Champion(*df.loc[22][0:])
Karma = Champion(*df.loc[23][0:])
KogMaw = Champion(*df.loc[24][0:])
Leona = Champion(*df.loc[25][0:])
Lucian = Champion(*df.loc[26][0:])
Lulu = Champion(*df.loc[27][0:])
Malphite = Champion(*df.loc[28][0:])
MasterYi = Champion(*df.loc[29][0:])
Mordekaiser = Champion(*df.loc[30][0:])
Nautilus = Champion(*df.loc[31][0:])
Neeko = Champion(*df.loc[32][0:])
Nocturne = Champion(*df.loc[33][0:])
Poppy = Champion(*df.loc[34][0:])
Rakan = Champion(*df.loc[35][0:])
Riven = Champion(*df.loc[36][0:])
Rumble = Champion(*df.loc[37][0:])
Shaco = Champion(*df.loc[38][0:])
Shen = Champion(*df.loc[39][0:])
Soraka = Champion(*df.loc[40][0:])
Syndra = Champion(*df.loc[41][0:])
Teemo = Champion(*df.loc[42][0:])
Thresh = Champion(*df.loc[43][0:])
TwistedFate = Champion(*df.loc[44][0:])
Urgot = Champion(*df.loc[45][0:])
Vayne = Champion(*df.loc[46][0:])
Vi = Champion(*df.loc[47][0:])
Viktor = Champion(*df.loc[48][0:])
Wukong = Champion(*df.loc[49][0:])
Xayah = Champion(*df.loc[50][0:])
Xerath = Champion(*df.loc[51][0:])
XinZhao = Champion(*df.loc[52][0:])
Yasuo = Champion(*df.loc[53][0:])
Zed = Champion(*df.loc[54][0:])
Ziggs = Champion(*df.loc[55][0:])
Zoe = Champion(*df.loc[56][0:])






for i,name in enumerate(dfList[0]): ######## wasted 2 hours for searching answer how to create variable variable
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




DPSMAX = max(df.DPS)

ASMAX = max(df.AS)

DMGMAX = max(df.DMG)

RANGEMAX = max(df.Range)

HPMAX = max(df.HP)

PHPMAX = max(df.PHP)

MHPMAX = max(df.MHP)

MEANHPMAX = max(df.MEANHP)

MANAMAX = max(df.Mana)

ARMORMAX = max(df.Armor)

MRMAX = max(df.MR)


##### Max stats list

maxStatsList = [DPSMAX, ASMAX, DMGMAX, RANGEMAX, HPMAX, PHPMAX, MHPMAX, 
                MEANHPMAX, MANAMAX, ARMORMAX, MRMAX]


############################################
#### Scaling champions stats to 0.0-1.0
############################################



for i,maxstat in enumerate(maxStatsList):
    df[df.columns[i+1]] = df[df.columns[i+1]]/maxstat
    print(df[df.columns[i+1]])
    print("The end of this stat")



















fHP = ctrl.Antecedent(np.arange(0, 1.01, 0.01), 'fHP')


fMEANHP = ctrl.Antecedent(np.arange(0, 1.01, 0.01), 'fMEANHP')



fPoints = ctrl.Consequent(np.arange(0, 1.01, 0.01), 'fPoints')



fHP['poor'] = fuzz.gbellmf(fHP.universe, 0.025, 0.95, 0.2)
fHP['mediocre'] = fuzz.gbellmf(fHP.universe, 0.025, 0.95, 0.4)
fHP['average'] = fuzz.gbellmf(fHP.universe, 0.025, 0.95, 0.6)
fHP['decent'] = fuzz.gbellmf(fHP.universe, 0.025, 0.95, 0.8)
fHP['good'] = fuzz.gbellmf(fHP.universe, 0.025, 0.95, 1.0)




fMEANHP['poor'] = fuzz.gbellmf(fMEANHP.universe, 0.025, 0.95, 0.2)
fMEANHP['mediocre'] = fuzz.gbellmf(fMEANHP.universe, 0.025, 0.95, 0.4)
fMEANHP['average'] = fuzz.gbellmf(fMEANHP.universe, 0.025, 0.95, 0.6)
fMEANHP['decent'] = fuzz.gbellmf(fMEANHP.universe, 0.025, 0.95, 0.8)
fMEANHP['good'] = fuzz.gbellmf(fMEANHP.universe, 0.025, 0.95, 1.0)

# fSuits['hearts'] = fuzz.gbellmf(fSuits.universe, 0.025, 0.95, float(counterPreferencesHearts.get()))
# fSuits['tiles'] = fuzz.gbellmf(fSuits.universe, 0.025, 0.95, float(counterPreferencesTiles.get()))
# fSuits['clovers'] = fuzz.gbellmf(fSuits.universe, 0.025, 0.95, float(counterPreferencesClovers.get()))
# fSuits['pikes'] = fuzz.gbellmf(fSuits.universe, 0.025, 0.95, float(counterPreferencesPikes.get()))
# fSuits['xd'] = fuzz.gbellmf(fSuits.universe, 0.025, 0.95, 4.3)


fPoints['poor'] = fuzz.gbellmf(fPoints.universe, 0.025, 0.95, 0.2)
fPoints['mediocre'] = fuzz.gbellmf(fPoints.universe, 0.025, 0.95, 0.4)
fPoints['average'] = fuzz.gbellmf(fPoints.universe, 0.025, 0.95, 0.6)
fPoints['decent'] = fuzz.gbellmf(fPoints.universe, 0.025, 0.95, 0.8)
fPoints['good'] = fuzz.gbellmf(fPoints.universe, 0.025, 0.95, 1.0)



# fPoints.view()



# fPoints.automf(5)












rule1 = ctrl.Rule(fMEANHP['good'] & fHP['good'], fPoints['good'])
rule2 = ctrl.Rule(fMEANHP['good'] & fHP['decent'], fPoints['good'])
rule3 = ctrl.Rule(fMEANHP['good'] & fHP['average'], fPoints['decent'])
rule4 = ctrl.Rule(fMEANHP['good'] & fHP['mediocre'], fPoints['decent'])
rule5 = ctrl.Rule(fMEANHP['good'] & fHP['poor'], fPoints['average'])


rule6 = ctrl.Rule(fMEANHP['decent'] & fHP['good'], fPoints['good'])
rule7 = ctrl.Rule(fMEANHP['decent'] & fHP['decent'], fPoints['decent'])
rule8 = ctrl.Rule(fMEANHP['decent'] & fHP['average'], fPoints['decent'])
rule9 = ctrl.Rule(fMEANHP['decent'] & fHP['mediocre'], fPoints['average'])
rule10 = ctrl.Rule(fMEANHP['decent'] & fHP['poor'], fPoints['mediocre'])


rule11 = ctrl.Rule(fMEANHP['average'] & fHP['good'], fPoints['decent'])
rule12 = ctrl.Rule(fMEANHP['average'] & fHP['decent'], fPoints['average'])
rule13 = ctrl.Rule(fMEANHP['average'] & fHP['average'], fPoints['average'])
rule14 = ctrl.Rule(fMEANHP['average'] & fHP['mediocre'], fPoints['average'])
rule15 = ctrl.Rule(fMEANHP['average'] & fHP['poor'], fPoints['poor'])

rule16 = ctrl.Rule(fMEANHP['mediocre'] & fHP['good'], fPoints['decent'])
rule17 = ctrl.Rule(fMEANHP['mediocre'] & fHP['decent'], fPoints['average'])
rule18 = ctrl.Rule(fMEANHP['mediocre'] & fHP['average'], fPoints['mediocre'])
rule19 = ctrl.Rule(fMEANHP['mediocre'] & fHP['mediocre'], fPoints['mediocre'])
rule20 = ctrl.Rule(fMEANHP['mediocre'] & fHP['poor'], fPoints['poor'])

rule21 = ctrl.Rule(fMEANHP['poor'] & fHP['good'], fPoints['average'])
rule22 = ctrl.Rule(fMEANHP['poor'] & fHP['decent'], fPoints['mediocre'])
rule23 = ctrl.Rule(fMEANHP['poor'] & fHP['average'], fPoints['mediocre'])
rule24 = ctrl.Rule(fMEANHP['poor'] & fHP['mediocre'], fPoints['poor'])
rule25 = ctrl.Rule(fMEANHP['poor'] & fHP['poor'], fPoints['poor'])

rules = [rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10,
         rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18, rule19,
         rule20, rule21, rule22, rule23, rule24, rule25]


# for i in range(1,26,1):
#     print("rule"+"%d"%i, end= ", ")


tanksPreferencesRulebase = ctrl.ControlSystem(rules)


    

    
    
    
    

    
tanksPreferences = ctrl.ControlSystemSimulation(tanksPreferencesRulebase)



tanksPreferencePoints = [0] * len(df)



for i in range(0,len(df)):

    
    
    
    tanksPreferences.input['fMEANHP'] = df.MEANHP[i]
    tanksPreferences.input['fHP'] = df.HP[i]
    tanksPreferences.compute()
    
    tanksPreferencePoints[i] = tanksPreferences.output['fPoints']


totalPointsList = [0] * len(df)
for i,champ in enumerate(tanksPreferencePoints):
    totalPointsList[i] = champ + df.DPS[i] + df.Tier[i]/5 -df.Cost[i]/20
    
    
df.insert(17,"Points",totalPointsList)

df.to_csv('scaledChampionsdf.csv', encoding='utf-8')




















ScaledChampion = namedtuple('ScaledChamp', ['Champion', 'DPS', 'AS', 'DMG', 
                                            'Range', 'HP', 'PHP', 'MHP', 'MEANHP',
                                            'Mana', 'Armor', 'MR', 'Origin', 
                                            'ClassPrimary', 'ClassSecondary', 'Cost',
                                            'Tier', 'Points'])




for i,name in enumerate(dfList[0]): 
    print('S'+name, end='')
    print(' = ScaledChampion(*df.loc[%d][0:])'%i)








SAhri = ScaledChampion(*df.loc[0][0:])
SAnnie = ScaledChampion(*df.loc[1][0:])
SAshe = ScaledChampion(*df.loc[2][0:])
SAurelionSol = ScaledChampion(*df.loc[3][0:])
SBard = ScaledChampion(*df.loc[4][0:])
SBlitzcrank = ScaledChampion(*df.loc[5][0:])
SCaitlyn = ScaledChampion(*df.loc[6][0:])
SCassiopeia = ScaledChampion(*df.loc[7][0:])
SDarius = ScaledChampion(*df.loc[8][0:])
SEkko = ScaledChampion(*df.loc[9][0:])
SEzreal = ScaledChampion(*df.loc[10][0:])
SFiora = ScaledChampion(*df.loc[11][0:])
SFizz = ScaledChampion(*df.loc[12][0:])
SGangplank = ScaledChampion(*df.loc[13][0:])
SGnar = ScaledChampion(*df.loc[14][0:])
SGraves = ScaledChampion(*df.loc[15][0:])
SIllaoi = ScaledChampion(*df.loc[16][0:])
SIrelia = ScaledChampion(*df.loc[17][0:])
SJanna = ScaledChampion(*df.loc[18][0:])
SJarvanIV = ScaledChampion(*df.loc[19][0:])
SJayce = ScaledChampion(*df.loc[20][0:])
SJhin = ScaledChampion(*df.loc[21][0:])
SJinx = ScaledChampion(*df.loc[22][0:])
SKarma = ScaledChampion(*df.loc[23][0:])
SKogMaw = ScaledChampion(*df.loc[24][0:])
SLeona = ScaledChampion(*df.loc[25][0:])
SLucian = ScaledChampion(*df.loc[26][0:])
SLulu = ScaledChampion(*df.loc[27][0:])
SMalphite = ScaledChampion(*df.loc[28][0:])
SMasterYi = ScaledChampion(*df.loc[29][0:])
SMordekaiser = ScaledChampion(*df.loc[30][0:])
SNautilus = ScaledChampion(*df.loc[31][0:])
SNeeko = ScaledChampion(*df.loc[32][0:])
SNocturne = ScaledChampion(*df.loc[33][0:])
SPoppy = ScaledChampion(*df.loc[34][0:])
SRakan = ScaledChampion(*df.loc[35][0:])
SRiven = ScaledChampion(*df.loc[36][0:])
SRumble = ScaledChampion(*df.loc[37][0:])
SShaco = ScaledChampion(*df.loc[38][0:])
SShen = ScaledChampion(*df.loc[39][0:])
SSoraka = ScaledChampion(*df.loc[40][0:])
SSyndra = ScaledChampion(*df.loc[41][0:])
STeemo = ScaledChampion(*df.loc[42][0:])
SThresh = ScaledChampion(*df.loc[43][0:])
STwistedFate = ScaledChampion(*df.loc[44][0:])
SUrgot = ScaledChampion(*df.loc[45][0:])
SVayne = ScaledChampion(*df.loc[46][0:])
SVi = ScaledChampion(*df.loc[47][0:])
SViktor = ScaledChampion(*df.loc[48][0:])
SWukong = ScaledChampion(*df.loc[49][0:])
SXayah = ScaledChampion(*df.loc[50][0:])
SXerath = ScaledChampion(*df.loc[51][0:])
SXinZhao = ScaledChampion(*df.loc[52][0:])
SYasuo = ScaledChampion(*df.loc[53][0:])
SZed = ScaledChampion(*df.loc[54][0:])
SZiggs = ScaledChampion(*df.loc[55][0:])
SZoe = ScaledChampion(*df.loc[56][0:])









SchampionList = [SAhri, SAnnie, SAshe, SAurelionSol, SBard, SBlitzcrank, SCaitlyn, 
                SCassiopeia, SDarius, SEkko, SEzreal, SFiora, SFizz, SGangplank, 
                SGnar, SGraves, SIllaoi, SIrelia, SJanna, SJarvanIV, SJayce, SJhin, 
                SJinx, SKarma, SKogMaw, SLeona, SLucian, SLulu, SMalphite, SMasterYi, 
                SMordekaiser, SNautilus, SNeeko, SNocturne, SPoppy, SRakan, SRiven, 
                SRumble, SShaco, SShen, SSoraka, SSyndra, STeemo, SThresh, 
                STwistedFate, SUrgot, SVayne, SVi, SViktor, SWukong, SXayah, 
                SXerath, SXinZhao, SYasuo, SZed, SZiggs, SZoe]





# df.sort_values(by=['Points'])
