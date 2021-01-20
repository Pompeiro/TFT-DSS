# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 11:39:30 2020

@author: Janusz
"""
from collections import namedtuple

import numpy as np
import pandas as pd
import skfuzzy as fuzz
from skfuzzy import control as ctrl

df = pd.read_csv("championsData.csv")

df.drop("Unnamed: 0", axis=1, inplace=True)

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
for i in range(0, len(df), 1):
    PHP.append(df.HP[i] * (1 + 0.01 * df.Armor[i]))
    MHP.append(df.HP[i] * (1 + 0.01 * df.MR[i]))
    MEANHP.append((PHP[i] + MHP[i]) / 2)


df.insert(6, "PHP", PHP)
df.insert(7, "MHP", MHP)
df.insert(8, "MEANHP", MEANHP)


Champion = namedtuple(
    "Champ",
    [
        "Champion",
        "DPS",
        "AS",
        "DMG",
        "Range",
        "HP",
        "PHP",
        "MHP",
        "MEANHP",
        "Mana",
        "Armor",
        "MR",
        "OriginPrimary",
        "OriginSecondary",
        "ClassPrimary",
        "ClassSecondary",
        "Cost",
        "Tier",
    ],
)

dfList = df.T.values.tolist()

for i, name in enumerate(dfList[0]):
    print(name, end="")
    print(" = Champion(*df.loc[%d][0:])" % i)


####################### Champions
Aatrox = Champion(*df.loc[0][0:])
Ahri = Champion(*df.loc[1][0:])
Akali = Champion(*df.loc[2][0:])
Annie = Champion(*df.loc[3][0:])
Aphelios = Champion(*df.loc[4][0:])
Ashe = Champion(*df.loc[5][0:])
Azir = Champion(*df.loc[6][0:])
Cassiopeia = Champion(*df.loc[7][0:])
Diana = Champion(*df.loc[8][0:])
Elise = Champion(*df.loc[9][0:])
Evelynn = Champion(*df.loc[10][0:])
Ezreal = Champion(*df.loc[11][0:])
Fiora = Champion(*df.loc[12][0:])
Garen = Champion(*df.loc[13][0:])
Hecarim = Champion(*df.loc[14][0:])
Irelia = Champion(*df.loc[15][0:])
Janna = Champion(*df.loc[16][0:])
JarvanIV = Champion(*df.loc[17][0:])
Jax = Champion(*df.loc[18][0:])
Jhin = Champion(*df.loc[19][0:])
Jinx = Champion(*df.loc[20][0:])
Kalista = Champion(*df.loc[21][0:])
Katarina = Champion(*df.loc[22][0:])
Kayn = Champion(*df.loc[23][0:])
Kennen = Champion(*df.loc[24][0:])
Kindred = Champion(*df.loc[25][0:])
LeeSin = Champion(*df.loc[26][0:])
Lillia = Champion(*df.loc[27][0:])
Lissandra = Champion(*df.loc[28][0:])
Lulu = Champion(*df.loc[29][0:])
Lux = Champion(*df.loc[30][0:])
Maokai = Champion(*df.loc[31][0:])
Morgana = Champion(*df.loc[32][0:])
Nami = Champion(*df.loc[33][0:])
Nidalee = Champion(*df.loc[34][0:])
Nunu = Champion(*df.loc[35][0:])
Pyke = Champion(*df.loc[36][0:])
Riven = Champion(*df.loc[37][0:])
Sejuani = Champion(*df.loc[38][0:])
Sett = Champion(*df.loc[39][0:])
Shen = Champion(*df.loc[40][0:])
Sylas = Champion(*df.loc[41][0:])
TahmKench = Champion(*df.loc[42][0:])
Talon = Champion(*df.loc[43][0:])
Teemo = Champion(*df.loc[44][0:])
Thresh = Champion(*df.loc[45][0:])
TwistedFate = Champion(*df.loc[46][0:])
Vayne = Champion(*df.loc[47][0:])
Veigar = Champion(*df.loc[48][0:])
Vi = Champion(*df.loc[49][0:])
Warwick = Champion(*df.loc[50][0:])
Wukong = Champion(*df.loc[51][0:])
XinZhao = Champion(*df.loc[52][0:])
Yasuo = Champion(*df.loc[53][0:])
Yone = Champion(*df.loc[54][0:])
Yuumi = Champion(*df.loc[55][0:])
Zed = Champion(*df.loc[56][0:])
Zilean = Champion(*df.loc[57][0:])


for i, name in enumerate(
    dfList[0]
):  ######## wasted 2 hours for searching answer how to create variable variable
    print(name, end=", ")


championList = [
    Aatrox,
    Ahri,
    Akali,
    Annie,
    Aphelios,
    Ashe,
    Azir,
    Cassiopeia,
    Diana,
    Elise,
    Evelynn,
    Ezreal,
    Fiora,
    Garen,
    Hecarim,
    Irelia,
    Janna,
    JarvanIV,
    Jax,
    Jhin,
    Jinx,
    Kalista,
    Katarina,
    Kayn,
    Kennen,
    Kindred,
    LeeSin,
    Lillia,
    Lissandra,
    Lulu,
    Lux,
    Maokai,
    Morgana,
    Nami,
    Nidalee,
    Nunu,
    Pyke,
    Riven,
    Sejuani,
    Sett,
    Shen,
    Sylas,
    TahmKench,
    Talon,
    Teemo,
    Thresh,
    TwistedFate,
    Vayne,
    Veigar,
    Vi,
    Warwick,
    Wukong,
    XinZhao,
    Yasuo,
    Yone,
    Yuumi,
    Zed,
    Zilean,
]


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

maxStatsList = [
    DPSMAX,
    ASMAX,
    DMGMAX,
    RANGEMAX,
    HPMAX,
    PHPMAX,
    MHPMAX,
    MEANHPMAX,
    MANAMAX,
    ARMORMAX,
    MRMAX,
]


############################################
#### Scaling champions stats to 0.0-1.0
############################################


for i, maxstat in enumerate(maxStatsList):
    df[df.columns[i + 1]] = df[df.columns[i + 1]] / maxstat
    print(df[df.columns[i + 1]])
    print("The end of this stat")


fHP = ctrl.Antecedent(np.arange(0, 1.01, 0.01), "fHP")


fMEANHP = ctrl.Antecedent(np.arange(0, 1.01, 0.01), "fMEANHP")


fPoints = ctrl.Consequent(np.arange(0, 1.01, 0.01), "fPoints")


fHP["poor"] = fuzz.gbellmf(fHP.universe, 0.025, 0.95, 0.2)
fHP["mediocre"] = fuzz.gbellmf(fHP.universe, 0.025, 0.95, 0.4)
fHP["average"] = fuzz.gbellmf(fHP.universe, 0.025, 0.95, 0.6)
fHP["decent"] = fuzz.gbellmf(fHP.universe, 0.025, 0.95, 0.8)
fHP["good"] = fuzz.gbellmf(fHP.universe, 0.025, 0.95, 1.0)


fMEANHP["poor"] = fuzz.gbellmf(fMEANHP.universe, 0.025, 0.95, 0.2)
fMEANHP["mediocre"] = fuzz.gbellmf(fMEANHP.universe, 0.025, 0.95, 0.4)
fMEANHP["average"] = fuzz.gbellmf(fMEANHP.universe, 0.025, 0.95, 0.6)
fMEANHP["decent"] = fuzz.gbellmf(fMEANHP.universe, 0.025, 0.95, 0.8)
fMEANHP["good"] = fuzz.gbellmf(fMEANHP.universe, 0.025, 0.95, 1.0)

# fSuits['hearts'] = fuzz.gbellmf(fSuits.universe, 0.025, 0.95, float(counterPreferencesHearts.get()))
# fSuits['tiles'] = fuzz.gbellmf(fSuits.universe, 0.025, 0.95, float(counterPreferencesTiles.get()))
# fSuits['clovers'] = fuzz.gbellmf(fSuits.universe, 0.025, 0.95, float(counterPreferencesClovers.get()))
# fSuits['pikes'] = fuzz.gbellmf(fSuits.universe, 0.025, 0.95, float(counterPreferencesPikes.get()))
# fSuits['xd'] = fuzz.gbellmf(fSuits.universe, 0.025, 0.95, 4.3)


fPoints["poor"] = fuzz.gbellmf(fPoints.universe, 0.025, 0.95, 0.2)
fPoints["mediocre"] = fuzz.gbellmf(fPoints.universe, 0.025, 0.95, 0.4)
fPoints["average"] = fuzz.gbellmf(fPoints.universe, 0.025, 0.95, 0.6)
fPoints["decent"] = fuzz.gbellmf(fPoints.universe, 0.025, 0.95, 0.8)
fPoints["good"] = fuzz.gbellmf(fPoints.universe, 0.025, 0.95, 1.0)


# fPoints.view()


# fPoints.automf(5)


rule1 = ctrl.Rule(fMEANHP["good"] & fHP["good"], fPoints["good"])
rule2 = ctrl.Rule(fMEANHP["good"] & fHP["decent"], fPoints["good"])
rule3 = ctrl.Rule(fMEANHP["good"] & fHP["average"], fPoints["decent"])
rule4 = ctrl.Rule(fMEANHP["good"] & fHP["mediocre"], fPoints["decent"])
rule5 = ctrl.Rule(fMEANHP["good"] & fHP["poor"], fPoints["average"])


rule6 = ctrl.Rule(fMEANHP["decent"] & fHP["good"], fPoints["good"])
rule7 = ctrl.Rule(fMEANHP["decent"] & fHP["decent"], fPoints["decent"])
rule8 = ctrl.Rule(fMEANHP["decent"] & fHP["average"], fPoints["decent"])
rule9 = ctrl.Rule(fMEANHP["decent"] & fHP["mediocre"], fPoints["average"])
rule10 = ctrl.Rule(fMEANHP["decent"] & fHP["poor"], fPoints["mediocre"])


rule11 = ctrl.Rule(fMEANHP["average"] & fHP["good"], fPoints["decent"])
rule12 = ctrl.Rule(fMEANHP["average"] & fHP["decent"], fPoints["average"])
rule13 = ctrl.Rule(fMEANHP["average"] & fHP["average"], fPoints["average"])
rule14 = ctrl.Rule(fMEANHP["average"] & fHP["mediocre"], fPoints["average"])
rule15 = ctrl.Rule(fMEANHP["average"] & fHP["poor"], fPoints["poor"])

rule16 = ctrl.Rule(fMEANHP["mediocre"] & fHP["good"], fPoints["decent"])
rule17 = ctrl.Rule(fMEANHP["mediocre"] & fHP["decent"], fPoints["average"])
rule18 = ctrl.Rule(fMEANHP["mediocre"] & fHP["average"], fPoints["mediocre"])
rule19 = ctrl.Rule(fMEANHP["mediocre"] & fHP["mediocre"], fPoints["mediocre"])
rule20 = ctrl.Rule(fMEANHP["mediocre"] & fHP["poor"], fPoints["poor"])

rule21 = ctrl.Rule(fMEANHP["poor"] & fHP["good"], fPoints["average"])
rule22 = ctrl.Rule(fMEANHP["poor"] & fHP["decent"], fPoints["mediocre"])
rule23 = ctrl.Rule(fMEANHP["poor"] & fHP["average"], fPoints["mediocre"])
rule24 = ctrl.Rule(fMEANHP["poor"] & fHP["mediocre"], fPoints["poor"])
rule25 = ctrl.Rule(fMEANHP["poor"] & fHP["poor"], fPoints["poor"])

rules = [
    rule1,
    rule2,
    rule3,
    rule4,
    rule5,
    rule6,
    rule7,
    rule8,
    rule9,
    rule10,
    rule11,
    rule12,
    rule13,
    rule14,
    rule15,
    rule16,
    rule17,
    rule18,
    rule19,
    rule20,
    rule21,
    rule22,
    rule23,
    rule24,
    rule25,
]


# for i in range(1,26,1):
#     print("rule"+"%d"%i, end= ", ")


tanksPreferencesRulebase = ctrl.ControlSystem(rules)


tanksPreferences = ctrl.ControlSystemSimulation(tanksPreferencesRulebase)


tanksPreferencePoints = [0] * len(df)


for i in range(0, len(df)):

    tanksPreferences.input["fMEANHP"] = df.MEANHP[i]
    tanksPreferences.input["fHP"] = df.HP[i]
    tanksPreferences.compute()

    tanksPreferencePoints[i] = tanksPreferences.output["fPoints"]


totalPointsList = [0] * len(df)
for i, champ in enumerate(tanksPreferencePoints):
    totalPointsList[i] = (
        champ + df.DPS[i] + df.Tier[i] / 5 - df.Cost[i] / 20
    )  # where champ is points for MEANHP>HP preference


##### 18 mean end of the list should be automated
df.insert(18, "Points", totalPointsList)

df.to_csv("scaledChampionsdf.csv", encoding="utf-8")


ScaledChampion = namedtuple(
    "ScaledChamp",
    [
        "Champion",
        "DPS",
        "AS",
        "DMG",
        "Range",
        "HP",
        "PHP",
        "MHP",
        "MEANHP",
        "Mana",
        "Armor",
        "MR",
        "OriginPrimary",
        "OriginSecondary",
        "ClassPrimary",
        "ClassSecondary",
        "Cost",
        "Tier",
        "Points",
    ],
)


for i, name in enumerate(dfList[0]):
    print("S" + name, end="")
    print(" = ScaledChampion(*df.loc[%d][0:])" % i)


SAatrox = ScaledChampion(*df.loc[0][0:])
SAhri = ScaledChampion(*df.loc[1][0:])
SAkali = ScaledChampion(*df.loc[2][0:])
SAnnie = ScaledChampion(*df.loc[3][0:])
SAphelios = ScaledChampion(*df.loc[4][0:])
SAshe = ScaledChampion(*df.loc[5][0:])
SAzir = ScaledChampion(*df.loc[6][0:])
SCassiopeia = ScaledChampion(*df.loc[7][0:])
SDiana = ScaledChampion(*df.loc[8][0:])
SElise = ScaledChampion(*df.loc[9][0:])
SEvelynn = ScaledChampion(*df.loc[10][0:])
SEzreal = ScaledChampion(*df.loc[11][0:])
SFiora = ScaledChampion(*df.loc[12][0:])
SGaren = ScaledChampion(*df.loc[13][0:])
SHecarim = ScaledChampion(*df.loc[14][0:])
SIrelia = ScaledChampion(*df.loc[15][0:])
SJanna = ScaledChampion(*df.loc[16][0:])
SJarvanIV = ScaledChampion(*df.loc[17][0:])
SJax = ScaledChampion(*df.loc[18][0:])
SJhin = ScaledChampion(*df.loc[19][0:])
SJinx = ScaledChampion(*df.loc[20][0:])
SKalista = ScaledChampion(*df.loc[21][0:])
SKatarina = ScaledChampion(*df.loc[22][0:])
SKayn = ScaledChampion(*df.loc[23][0:])
SKennen = ScaledChampion(*df.loc[24][0:])
SKindred = ScaledChampion(*df.loc[25][0:])
SLeeSin = ScaledChampion(*df.loc[26][0:])
SLillia = ScaledChampion(*df.loc[27][0:])
SLissandra = ScaledChampion(*df.loc[28][0:])
SLulu = ScaledChampion(*df.loc[29][0:])
SLux = ScaledChampion(*df.loc[30][0:])
SMaokai = ScaledChampion(*df.loc[31][0:])
SMorgana = ScaledChampion(*df.loc[32][0:])
SNami = ScaledChampion(*df.loc[33][0:])
SNidalee = ScaledChampion(*df.loc[34][0:])
SNunu = ScaledChampion(*df.loc[35][0:])
SPyke = ScaledChampion(*df.loc[36][0:])
SRiven = ScaledChampion(*df.loc[37][0:])
SSejuani = ScaledChampion(*df.loc[38][0:])
SSett = ScaledChampion(*df.loc[39][0:])
SShen = ScaledChampion(*df.loc[40][0:])
SSylas = ScaledChampion(*df.loc[41][0:])
STahmKench = ScaledChampion(*df.loc[42][0:])
STalon = ScaledChampion(*df.loc[43][0:])
STeemo = ScaledChampion(*df.loc[44][0:])
SThresh = ScaledChampion(*df.loc[45][0:])
STwistedFate = ScaledChampion(*df.loc[46][0:])
SVayne = ScaledChampion(*df.loc[47][0:])
SVeigar = ScaledChampion(*df.loc[48][0:])
SVi = ScaledChampion(*df.loc[49][0:])
SWarwick = ScaledChampion(*df.loc[50][0:])
SWukong = ScaledChampion(*df.loc[51][0:])
SXinZhao = ScaledChampion(*df.loc[52][0:])
SYasuo = ScaledChampion(*df.loc[53][0:])
SYone = ScaledChampion(*df.loc[54][0:])
SYuumi = ScaledChampion(*df.loc[55][0:])
SZed = ScaledChampion(*df.loc[56][0:])
SZilean = ScaledChampion(*df.loc[57][0:])


for i, name in enumerate(
    dfList[0]
):  ######## wasted 2 hours for searching answer how to create variable variable
    print("S" + name, end=", ")


SchampionList = [
    SAatrox,
    SAhri,
    SAkali,
    SAnnie,
    SAphelios,
    SAshe,
    SAzir,
    SCassiopeia,
    SDiana,
    SElise,
    SEvelynn,
    SEzreal,
    SFiora,
    SGaren,
    SHecarim,
    SIrelia,
    SJanna,
    SJarvanIV,
    SJax,
    SJhin,
    SJinx,
    SKalista,
    SKatarina,
    SKayn,
    SKennen,
    SKindred,
    SLeeSin,
    SLillia,
    SLissandra,
    SLulu,
    SLux,
    SMaokai,
    SMorgana,
    SNami,
    SNidalee,
    SNunu,
    SPyke,
    SRiven,
    SSejuani,
    SSett,
    SShen,
    SSylas,
    STahmKench,
    STalon,
    STeemo,
    SThresh,
    STwistedFate,
    SVayne,
    SVeigar,
    SVi,
    SWarwick,
    SWukong,
    SXinZhao,
    SYasuo,
    SYone,
    SYuumi,
    SZed,
    SZilean,
]


# df.sort_values(by=['Points'])
