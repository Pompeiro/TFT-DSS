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

df = pd.read_csv("champions_data.csv")

df.drop("Unnamed: 0", axis=1, inplace=True)

# effective hp formula for dmg reduction is: armor/(100+armor)


# from lol wiki

# physical effective health =  health  × (1 + 0.01 × armor)
# magical effective health =  health  × (1 + 0.01 × mr)


# formula for updated php after picking up bonus armor for combo or item
# Wukong.php/Wukong.hp+BonusArmor/100


php = []
mhp = []
mean_hp = []
for i in range(0, len(df), 1):
    php.append(df.hp[i] * (1 + 0.01 * df.armor[i]))
    mhp.append(df.hp[i] * (1 + 0.01 * df.mr[i]))
    mean_hp.append((php[i] + mhp[i]) / 2)


df.insert(6, "php", php)
df.insert(7, "mhp", mhp)
df.insert(8, "mean_hp", mean_hp)


Champion = namedtuple(
    "Champion",
    [
        "champion",
        "dps",
        "as_",
        "dmg",
        "range",
        "hp",
        "php",
        "mhp",
        "mean_hp",
        "mana",
        "armor",
        "mr",
        "origin_prim",
        "origin_sec",
        "class_prim",
        "class_sec",
        "cost",
        "tier",
    ],
)

champion_stats_list = df.T.values.tolist()

for i, name in enumerate(champion_stats_list[0]):
    print(name.replace(" ", ""), end="")
    print(" = Champion(*df.loc[%d][0:])" % i)


# Champions
Aatrox = Champion(*df.loc[0][0:])
Akshan = Champion(*df.loc[1][0:])
Aphelios = Champion(*df.loc[2][0:])
Ashe = Champion(*df.loc[3][0:])
Brand = Champion(*df.loc[4][0:])
Diana = Champion(*df.loc[5][0:])
Draven = Champion(*df.loc[6][0:])
Fiddlesticks = Champion(*df.loc[7][0:])
Galio = Champion(*df.loc[8][0:])
Garen = Champion(*df.loc[9][0:])
Gragas = Champion(*df.loc[10][0:])
Gwen = Champion(*df.loc[11][0:])
Hecarim = Champion(*df.loc[12][0:])
Heimerdinger = Champion(*df.loc[13][0:])
Irelia = Champion(*df.loc[14][0:])
Ivern = Champion(*df.loc[15][0:])
Jax = Champion(*df.loc[16][0:])
Kalista = Champion(*df.loc[17][0:])
Karma = Champion(*df.loc[18][0:])
Kayle = Champion(*df.loc[19][0:])
Kennen = Champion(*df.loc[20][0:])
Khazix = Champion(*df.loc[21][0:])
Kled = Champion(*df.loc[22][0:])
LeeSin = Champion(*df.loc[23][0:])
Leona = Champion(*df.loc[24][0:])
Lucian = Champion(*df.loc[25][0:])
Lulu = Champion(*df.loc[26][0:])
Lux = Champion(*df.loc[27][0:])
MissFortune = Champion(*df.loc[28][0:])
Nautilus = Champion(*df.loc[29][0:])
Nidalee = Champion(*df.loc[30][0:])
Nocturne = Champion(*df.loc[31][0:])
Nunu = Champion(*df.loc[32][0:])
Olaf = Champion(*df.loc[33][0:])
Poppy = Champion(*df.loc[34][0:])
Pyke = Champion(*df.loc[35][0:])
Rakan = Champion(*df.loc[36][0:])
Rell = Champion(*df.loc[37][0:])
Riven = Champion(*df.loc[38][0:])
Sejuani = Champion(*df.loc[39][0:])
Senna = Champion(*df.loc[40][0:])
Sett = Champion(*df.loc[41][0:])
Soraka = Champion(*df.loc[42][0:])
Syndra = Champion(*df.loc[43][0:])
Teemo = Champion(*df.loc[44][0:])
Thresh = Champion(*df.loc[45][0:])
Tristana = Champion(*df.loc[46][0:])
Udyr = Champion(*df.loc[47][0:])
Varus = Champion(*df.loc[48][0:])
Vayne = Champion(*df.loc[49][0:])
Velkoz = Champion(*df.loc[50][0:])
Viego = Champion(*df.loc[51][0:])
Vladimir = Champion(*df.loc[52][0:])
Volibear = Champion(*df.loc[53][0:])
Yasuo = Champion(*df.loc[54][0:])
Ziggs = Champion(*df.loc[55][0:])
Zyra = Champion(*df.loc[56][0:])


for i, name in enumerate(champion_stats_list[0]):
    print(name.replace(" ", ""), end=", ")


# Performance calculation


# Max stats


DPS_MAX = max(df.dps)

AS_MAX = max(df.as_)

DMG_MAX = max(df.dmg)

RANGE_MAX = max(df.range)

HP_MAX = max(df.hp)

PHP_MAX = max(df.php)

MHP_MAX = max(df.mhp)

MEANHP_MAX = max(df.mean_hp)

MANA_MAX = max(df.mana)

ARMOR_MAX = max(df.armor)

MR_MAX = max(df.mr)


# Max stats list

max_stats_list = [
    DPS_MAX,
    AS_MAX,
    DMG_MAX,
    RANGE_MAX,
    HP_MAX,
    PHP_MAX,
    MHP_MAX,
    MEANHP_MAX,
    MANA_MAX,
    ARMOR_MAX,
    MR_MAX,
]


# Scaling champions stats to 0.0-1.0


for i, max_stat in enumerate(max_stats_list):
    df[df.columns[i + 1]] = df[df.columns[i + 1]] / max_stat
    print(df[df.columns[i + 1]])
    print("The end of this stat")


hp_fuzzy = ctrl.Antecedent(np.arange(0, 1.01, 0.01), "hp_fuzzy")


mean_hp_fuzzy = ctrl.Antecedent(np.arange(0, 1.01, 0.01), "mean_hp_fuzzy")


points_fuzzy = ctrl.Consequent(np.arange(0, 1.01, 0.01), "points_fuzzy")


hp_fuzzy["poor"] = fuzz.gbellmf(hp_fuzzy.universe, 0.025, 0.95, 0.2)
hp_fuzzy["mediocre"] = fuzz.gbellmf(hp_fuzzy.universe, 0.025, 0.95, 0.4)
hp_fuzzy["average"] = fuzz.gbellmf(hp_fuzzy.universe, 0.025, 0.95, 0.6)
hp_fuzzy["decent"] = fuzz.gbellmf(hp_fuzzy.universe, 0.025, 0.95, 0.8)
hp_fuzzy["good"] = fuzz.gbellmf(hp_fuzzy.universe, 0.025, 0.95, 1.0)


mean_hp_fuzzy["poor"] = fuzz.gbellmf(mean_hp_fuzzy.universe, 0.025, 0.95, 0.2)
mean_hp_fuzzy["mediocre"] = fuzz.gbellmf(mean_hp_fuzzy.universe, 0.025, 0.95, 0.4)
mean_hp_fuzzy["average"] = fuzz.gbellmf(mean_hp_fuzzy.universe, 0.025, 0.95, 0.6)
mean_hp_fuzzy["decent"] = fuzz.gbellmf(mean_hp_fuzzy.universe, 0.025, 0.95, 0.8)
mean_hp_fuzzy["good"] = fuzz.gbellmf(mean_hp_fuzzy.universe, 0.025, 0.95, 1.0)


points_fuzzy["poor"] = fuzz.gbellmf(points_fuzzy.universe, 0.025, 0.95, 0.2)
points_fuzzy["mediocre"] = fuzz.gbellmf(points_fuzzy.universe, 0.025, 0.95, 0.4)
points_fuzzy["average"] = fuzz.gbellmf(points_fuzzy.universe, 0.025, 0.95, 0.6)
points_fuzzy["decent"] = fuzz.gbellmf(points_fuzzy.universe, 0.025, 0.95, 0.8)
points_fuzzy["good"] = fuzz.gbellmf(points_fuzzy.universe, 0.025, 0.95, 1.0)


# points_fuzzy.view()


# points_fuzzy.automf(5)


rule1 = ctrl.Rule(mean_hp_fuzzy["good"] & hp_fuzzy["good"], points_fuzzy["good"])
rule2 = ctrl.Rule(mean_hp_fuzzy["good"] & hp_fuzzy["decent"], points_fuzzy["good"])
rule3 = ctrl.Rule(mean_hp_fuzzy["good"] & hp_fuzzy["average"], points_fuzzy["decent"])
rule4 = ctrl.Rule(mean_hp_fuzzy["good"] & hp_fuzzy["mediocre"], points_fuzzy["decent"])
rule5 = ctrl.Rule(mean_hp_fuzzy["good"] & hp_fuzzy["poor"], points_fuzzy["average"])


rule6 = ctrl.Rule(mean_hp_fuzzy["decent"] & hp_fuzzy["good"], points_fuzzy["good"])
rule7 = ctrl.Rule(mean_hp_fuzzy["decent"] & hp_fuzzy["decent"], points_fuzzy["decent"])
rule8 = ctrl.Rule(mean_hp_fuzzy["decent"] & hp_fuzzy["average"], points_fuzzy["decent"])
rule9 = ctrl.Rule(
    mean_hp_fuzzy["decent"] & hp_fuzzy["mediocre"], points_fuzzy["average"]
)
rule10 = ctrl.Rule(mean_hp_fuzzy["decent"] & hp_fuzzy["poor"], points_fuzzy["mediocre"])


rule11 = ctrl.Rule(mean_hp_fuzzy["average"] & hp_fuzzy["good"], points_fuzzy["decent"])
rule12 = ctrl.Rule(
    mean_hp_fuzzy["average"] & hp_fuzzy["decent"], points_fuzzy["average"]
)
rule13 = ctrl.Rule(
    mean_hp_fuzzy["average"] & hp_fuzzy["average"], points_fuzzy["average"]
)
rule14 = ctrl.Rule(
    mean_hp_fuzzy["average"] & hp_fuzzy["mediocre"], points_fuzzy["average"]
)
rule15 = ctrl.Rule(mean_hp_fuzzy["average"] & hp_fuzzy["poor"], points_fuzzy["poor"])

rule16 = ctrl.Rule(mean_hp_fuzzy["mediocre"] & hp_fuzzy["good"], points_fuzzy["decent"])
rule17 = ctrl.Rule(
    mean_hp_fuzzy["mediocre"] & hp_fuzzy["decent"], points_fuzzy["average"]
)
rule18 = ctrl.Rule(
    mean_hp_fuzzy["mediocre"] & hp_fuzzy["average"], points_fuzzy["mediocre"]
)
rule19 = ctrl.Rule(
    mean_hp_fuzzy["mediocre"] & hp_fuzzy["mediocre"], points_fuzzy["mediocre"]
)
rule20 = ctrl.Rule(mean_hp_fuzzy["mediocre"] & hp_fuzzy["poor"], points_fuzzy["poor"])

rule21 = ctrl.Rule(mean_hp_fuzzy["poor"] & hp_fuzzy["good"], points_fuzzy["average"])
rule22 = ctrl.Rule(mean_hp_fuzzy["poor"] & hp_fuzzy["decent"], points_fuzzy["mediocre"])
rule23 = ctrl.Rule(
    mean_hp_fuzzy["poor"] & hp_fuzzy["average"], points_fuzzy["mediocre"]
)
rule24 = ctrl.Rule(mean_hp_fuzzy["poor"] & hp_fuzzy["mediocre"], points_fuzzy["poor"])
rule25 = ctrl.Rule(mean_hp_fuzzy["poor"] & hp_fuzzy["poor"], points_fuzzy["poor"])

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


tanks_preferences_rulebase = ctrl.ControlSystem(rules)


tanks_preferences = ctrl.ControlSystemSimulation(tanks_preferences_rulebase)


tanks_preference_points = [0] * len(df)


for i in range(0, len(df)):

    tanks_preferences.input["mean_hp_fuzzy"] = df.mean_hp[i]
    tanks_preferences.input["hp_fuzzy"] = df.hp[i]
    tanks_preferences.compute()

    tanks_preference_points[i] = tanks_preferences.output["points_fuzzy"]


total_points_list = [0] * len(df)
for i, champ in enumerate(tanks_preference_points):
    total_points_list[i] = (
        champ + df.dps[i] + df.tier[i] / 5 - df.cost[i] / 20
    )  # where champ is points for mean_hp>hp preference


df.insert(18, "points", total_points_list)

df.to_csv("champions_data_scaled.csv", encoding="utf-8")


ScaledChampion = namedtuple(
    "ScaledChamp",
    [
        "champion",
        "dps",
        "as_",
        "dmg",
        "range",
        "hp",
        "php",
        "mhp",
        "mean_hp",
        "mana",
        "armor",
        "mr",
        "origin_prim",
        "origin_sec",
        "class_prim",
        "class_sec",
        "cost",
        "tier",
        "points",
    ],
)


for i, name in enumerate(champion_stats_list[0]):
    print("S" + name.replace(" ", ""), end="")
    print(" = ScaledChampion(*df.loc[%d][0:])" % i)


SAatrox = ScaledChampion(*df.loc[0][0:])
SAkshan = ScaledChampion(*df.loc[1][0:])
SAphelios = ScaledChampion(*df.loc[2][0:])
SAshe = ScaledChampion(*df.loc[3][0:])
SBrand = ScaledChampion(*df.loc[4][0:])
SDiana = ScaledChampion(*df.loc[5][0:])
SDraven = ScaledChampion(*df.loc[6][0:])
SFiddlesticks = ScaledChampion(*df.loc[7][0:])
SGalio = ScaledChampion(*df.loc[8][0:])
SGaren = ScaledChampion(*df.loc[9][0:])
SGragas = ScaledChampion(*df.loc[10][0:])
SGwen = ScaledChampion(*df.loc[11][0:])
SHecarim = ScaledChampion(*df.loc[12][0:])
SHeimerdinger = ScaledChampion(*df.loc[13][0:])
SIrelia = ScaledChampion(*df.loc[14][0:])
SIvern = ScaledChampion(*df.loc[15][0:])
SJax = ScaledChampion(*df.loc[16][0:])
SKalista = ScaledChampion(*df.loc[17][0:])
SKarma = ScaledChampion(*df.loc[18][0:])
SKayle = ScaledChampion(*df.loc[19][0:])
SKennen = ScaledChampion(*df.loc[20][0:])
SKhazix = ScaledChampion(*df.loc[21][0:])
SKled = ScaledChampion(*df.loc[22][0:])
SLeeSin = ScaledChampion(*df.loc[23][0:])
SLeona = ScaledChampion(*df.loc[24][0:])
SLucian = ScaledChampion(*df.loc[25][0:])
SLulu = ScaledChampion(*df.loc[26][0:])
SLux = ScaledChampion(*df.loc[27][0:])
SMissFortune = ScaledChampion(*df.loc[28][0:])
SNautilus = ScaledChampion(*df.loc[29][0:])
SNidalee = ScaledChampion(*df.loc[30][0:])
SNocturne = ScaledChampion(*df.loc[31][0:])
SNunu = ScaledChampion(*df.loc[32][0:])
SOlaf = ScaledChampion(*df.loc[33][0:])
SPoppy = ScaledChampion(*df.loc[34][0:])
SPyke = ScaledChampion(*df.loc[35][0:])
SRakan = ScaledChampion(*df.loc[36][0:])
SRell = ScaledChampion(*df.loc[37][0:])
SRiven = ScaledChampion(*df.loc[38][0:])
SSejuani = ScaledChampion(*df.loc[39][0:])
SSenna = ScaledChampion(*df.loc[40][0:])
SSett = ScaledChampion(*df.loc[41][0:])
SSoraka = ScaledChampion(*df.loc[42][0:])
SSyndra = ScaledChampion(*df.loc[43][0:])
STeemo = ScaledChampion(*df.loc[44][0:])
SThresh = ScaledChampion(*df.loc[45][0:])
STristana = ScaledChampion(*df.loc[46][0:])
SUdyr = ScaledChampion(*df.loc[47][0:])
SVarus = ScaledChampion(*df.loc[48][0:])
SVayne = ScaledChampion(*df.loc[49][0:])
SVelkoz = ScaledChampion(*df.loc[50][0:])
SViego = ScaledChampion(*df.loc[51][0:])
SVladimir = ScaledChampion(*df.loc[52][0:])
SVolibear = ScaledChampion(*df.loc[53][0:])
SYasuo = ScaledChampion(*df.loc[54][0:])
SZiggs = ScaledChampion(*df.loc[55][0:])
SZyra = ScaledChampion(*df.loc[56][0:])


for i, name in enumerate(champion_stats_list[0]):
    print("S" + name.replace(" ", ""), end=", ")


scaled_champions_list = [
    SAatrox,
    SAkshan,
    SAphelios,
    SAshe,
    SBrand,
    SDiana,
    SDraven,
    SFiddlesticks,
    SGalio,
    SGaren,
    SGragas,
    SGwen,
    SHecarim,
    SHeimerdinger,
    SIrelia,
    SIvern,
    SJax,
    SKalista,
    SKarma,
    SKayle,
    SKennen,
    SKhazix,
    SKled,
    SLeeSin,
    SLeona,
    SLucian,
    SLulu,
    SLux,
    SMissFortune,
    SNautilus,
    SNidalee,
    SNocturne,
    SNunu,
    SOlaf,
    SPoppy,
    SPyke,
    SRakan,
    SRell,
    SRiven,
    SSejuani,
    SSenna,
    SSett,
    SSoraka,
    SSyndra,
    STeemo,
    SThresh,
    STristana,
    SUdyr,
    SVarus,
    SVayne,
    SVelkoz,
    SViego,
    SVladimir,
    SVolibear,
    SYasuo,
    SZiggs,
    SZyra,
]


# df.sort_values(by=['points'])
