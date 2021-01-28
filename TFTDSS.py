# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 10:54:45 2020

@author: Janusz
"""

import logging
import tkinter as tk
import tkinter.font as tkFont
from collections import namedtuple

import easyocr
import pandas as pd
from cv2 import cv2 as cv

import dss
from windowcapture import WindowCapture

# REMEMBER TO SET GAME TO WINDOW MODE!!!!!!!!!!!!!!!!!!!!
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# IF you want to test GUI without game then change LOAD_IMAGE in dss.py file
logging.basicConfig(level=logging.DEBUG)

VARIABLE_PRINT_MODE = 0
# VARIABLE_PRINT_MODE = 1

reader = easyocr.Reader(["en"])

# drawing rectangles

line_color = (255, 0, 255)
marker_color = (255, 0, 255)


rgb_colours_list = [
    (255, 0, 255),
    (0, 255, 255),
    (0, 255, 255),
    (0, 255, 255),
    (0, 255, 0),
]

# GUI
UPSIDE = 0  # champion pool
DOWNSIDE = 16  # champions to buy
SHIFT_BETWEEN_ORIGINS = 6
ORIGIN_LABEL_POSITION_COLUMN = 1

Champion = namedtuple(
    "Champion",
    [
        "name",
        "name_ocr",
        "index_ocr",
        "ChampCounter",
        "origin_prim",
        "origin_sec",
        "class_prim",
        "class_sec",
        "OriginPrimCounter",
        "OriginSecCounter",
        "ClassPrimCounter",
        "ClassSecCounter",
    ],
)


# WINDOW THINGS


MainWindow = tk.Tk()
MainWindow.geometry("1900x800+0+0")
MainWindow.title("TFTDSS")


BOLDED_FONT = tkFont.Font(family="Arial", size=10, weight=tkFont.BOLD)


df = pd.read_csv("champions_data_scaled.csv")

df.drop("Unnamed: 0", axis=1, inplace=True)
df.points = df["points"].round(3)

# order as in GUI
df.sort_values(by=["origin_prim", "champion"], inplace=True)
df.reset_index(drop=True, inplace=True)

# OCR things

if VARIABLE_PRINT_MODE:
    print("champions_list_for_ocr = [", end=" ")
    for champ in df.champion:
        print("'" + champ + "'", end=", ")
    print("]")


champions_list_for_ocr = [
    "Aatrox",
    "Elise",
    "Kalista",
    "Pyke",
    "Sivir",
    "Twisted Fate",
    "Vladimir",
    "Zilean",
    "Samira",
    "Jax",
    "Kayle",
    "Lee Sin",
    "Nasus",
    "Wukong",
    "Aurelion Sol",
    "Brand",
    "Braum",
    "Olaf",
    "Shyvana",
    "Swain",
    "Tristana",
    "Lulu",
    "Maokai",
    "Nunu & Willump",
    "Ornn",
    "Rakan",
    "Veigar",
    "Xayah",
    "Fiora",
    "Irelia",
    "Janna",
    "Morgana",
    "Talon",
    "Yasuo",
    "Yone",
    "Chogath",
    "Nautilus",
    "Neeko",
    "Annie",
    "Darius",
    "Sejuani",
    "Tahm Kench",
    "Akali",
    "Kennen",
    "Shen",
    "Zed",
    "Diana",
    "Kindred",
    "Teemo",
    "Yuumi",
    "Sett",
    "Azir",
    "Garen",
    "Jarvan IV",
    "Katarina",
    "Nidalee",
    "Tryndamere",
    "Vi",
]

df.champion = df.champion.str.replace(" ", "")


origin_list = list(set(df.origin_prim)) + list(set(df.origin_sec))
origin_list = list(set(origin_list))
origin_list.remove("None")
origin_list.sort()

if VARIABLE_PRINT_MODE:
    for origin in origin_list:
        print(
            origin.lower()
            + "_champs = list(df.query("
            + "'origin_prim == "
            + '"'
            + "%s" % origin
            + '"'
            + "').champion)"
        )

if VARIABLE_PRINT_MODE:
    print("origin_champs_from_df_list = [", end=" ")
    for origin in origin_list:
        print(origin.lower() + "_champs", end=", ")
    print("]")

cultist_champs = list(df.query('origin_prim == "Cultist"').champion)
daredevil_champs = list(df.query('origin_prim == "Daredevil"').champion)
divine_champs = list(df.query('origin_prim == "Divine"').champion)
dragonsoul_champs = list(df.query('origin_prim == "Dragonsoul"').champion)
elderwood_champs = list(df.query('origin_prim == "Elderwood"').champion)
enlightened_champs = list(df.query('origin_prim == "Enlightened"').champion)
exile_champs = list(df.query('origin_prim == "Exile"').champion)
fabled_champs = list(df.query('origin_prim == "Fabled"').champion)
fortune_champs = list(df.query('origin_prim == "Fortune"').champion)
ninja_champs = list(df.query('origin_prim == "Ninja"').champion)
spirit_champs = list(df.query('origin_prim == "Spirit"').champion)
the_boss_champs = list(df.query('origin_prim == "The Boss"').champion)
warlord_champs = list(df.query('origin_prim == "Warlord"').champion)

origin_champs_from_df_list = [
    cultist_champs,
    daredevil_champs,
    divine_champs,
    dragonsoul_champs,
    elderwood_champs,
    enlightened_champs,
    exile_champs,
    fabled_champs,
    fortune_champs,
    ninja_champs,
    spirit_champs,
    the_boss_champs,
    warlord_champs,
]


class_list = list(set(df.class_prim)) + list(set(df.class_sec))
class_list = list(set(class_list))
class_list.remove("None")
class_list.sort()


# COUNTERS FOR CHAMPIONS IN POOL

if VARIABLE_PRINT_MODE:
    for champ in df.champion:
        print("Counter" + champ + " = tk.IntVar()")


CounterAatrox = tk.IntVar()
CounterElise = tk.IntVar()
CounterKalista = tk.IntVar()
CounterPyke = tk.IntVar()
CounterSivir = tk.IntVar()
CounterTwistedFate = tk.IntVar()
CounterVladimir = tk.IntVar()
CounterZilean = tk.IntVar()
CounterSamira = tk.IntVar()
CounterJax = tk.IntVar()
CounterKayle = tk.IntVar()
CounterLeeSin = tk.IntVar()
CounterNasus = tk.IntVar()
CounterWukong = tk.IntVar()
CounterAurelionSol = tk.IntVar()
CounterBrand = tk.IntVar()
CounterBraum = tk.IntVar()
CounterOlaf = tk.IntVar()
CounterShyvana = tk.IntVar()
CounterSwain = tk.IntVar()
CounterTristana = tk.IntVar()
CounterLulu = tk.IntVar()
CounterMaokai = tk.IntVar()
CounterNunu = tk.IntVar()
CounterOrnn = tk.IntVar()
CounterRakan = tk.IntVar()
CounterVeigar = tk.IntVar()
CounterXayah = tk.IntVar()
CounterFiora = tk.IntVar()
CounterIrelia = tk.IntVar()
CounterJanna = tk.IntVar()
CounterMorgana = tk.IntVar()
CounterTalon = tk.IntVar()
CounterYasuo = tk.IntVar()
CounterYone = tk.IntVar()
CounterChogath = tk.IntVar()
CounterNautilus = tk.IntVar()
CounterNeeko = tk.IntVar()
CounterAnnie = tk.IntVar()
CounterDarius = tk.IntVar()
CounterSejuani = tk.IntVar()
CounterTahmKench = tk.IntVar()
CounterAkali = tk.IntVar()
CounterKennen = tk.IntVar()
CounterShen = tk.IntVar()
CounterZed = tk.IntVar()
CounterDiana = tk.IntVar()
CounterKindred = tk.IntVar()
CounterTeemo = tk.IntVar()
CounterYuumi = tk.IntVar()
CounterSett = tk.IntVar()
CounterAzir = tk.IntVar()
CounterGaren = tk.IntVar()
CounterJarvanIV = tk.IntVar()
CounterKatarina = tk.IntVar()
CounterNidalee = tk.IntVar()
CounterTryndamere = tk.IntVar()
CounterVi = tk.IntVar()

if VARIABLE_PRINT_MODE:
    print("origin_champs_counters = [")
    for champ in df.champion:
        print("Counter" + champ, end=", ")
    print("]")
    print()

origin_champs_counters = [
    CounterAatrox,
    CounterElise,
    CounterKalista,
    CounterPyke,
    CounterSivir,
    CounterTwistedFate,
    CounterVladimir,
    CounterZilean,
    CounterSamira,
    CounterJax,
    CounterKayle,
    CounterLeeSin,
    CounterNasus,
    CounterWukong,
    CounterAurelionSol,
    CounterBrand,
    CounterBraum,
    CounterOlaf,
    CounterShyvana,
    CounterSwain,
    CounterTristana,
    CounterLulu,
    CounterMaokai,
    CounterNunu,
    CounterOrnn,
    CounterRakan,
    CounterVeigar,
    CounterXayah,
    CounterFiora,
    CounterIrelia,
    CounterJanna,
    CounterMorgana,
    CounterTalon,
    CounterYasuo,
    CounterYone,
    CounterChogath,
    CounterNautilus,
    CounterNeeko,
    CounterAnnie,
    CounterDarius,
    CounterSejuani,
    CounterTahmKench,
    CounterAkali,
    CounterKennen,
    CounterShen,
    CounterZed,
    CounterDiana,
    CounterKindred,
    CounterTeemo,
    CounterYuumi,
    CounterSett,
    CounterAzir,
    CounterGaren,
    CounterJarvanIV,
    CounterKatarina,
    CounterNidalee,
    CounterTryndamere,
    CounterVi,
]

# COUNTERS for champions to buy

if VARIABLE_PRINT_MODE:
    for champ in df.champion:
        print("CounterBuy" + champ + " = tk.IntVar()")


CounterBuyAatrox = tk.IntVar()
CounterBuyElise = tk.IntVar()
CounterBuyKalista = tk.IntVar()
CounterBuyPyke = tk.IntVar()
CounterBuySivir = tk.IntVar()
CounterBuyTwistedFate = tk.IntVar()
CounterBuyVladimir = tk.IntVar()
CounterBuyZilean = tk.IntVar()
CounterBuySamira = tk.IntVar()
CounterBuyJax = tk.IntVar()
CounterBuyKayle = tk.IntVar()
CounterBuyLeeSin = tk.IntVar()
CounterBuyNasus = tk.IntVar()
CounterBuyWukong = tk.IntVar()
CounterBuyAurelionSol = tk.IntVar()
CounterBuyBrand = tk.IntVar()
CounterBuyBraum = tk.IntVar()
CounterBuyOlaf = tk.IntVar()
CounterBuyShyvana = tk.IntVar()
CounterBuySwain = tk.IntVar()
CounterBuyTristana = tk.IntVar()
CounterBuyLulu = tk.IntVar()
CounterBuyMaokai = tk.IntVar()
CounterBuyNunu = tk.IntVar()
CounterBuyOrnn = tk.IntVar()
CounterBuyRakan = tk.IntVar()
CounterBuyVeigar = tk.IntVar()
CounterBuyXayah = tk.IntVar()
CounterBuyFiora = tk.IntVar()
CounterBuyIrelia = tk.IntVar()
CounterBuyJanna = tk.IntVar()
CounterBuyMorgana = tk.IntVar()
CounterBuyTalon = tk.IntVar()
CounterBuyYasuo = tk.IntVar()
CounterBuyYone = tk.IntVar()
CounterBuyChogath = tk.IntVar()
CounterBuyNautilus = tk.IntVar()
CounterBuyNeeko = tk.IntVar()
CounterBuyAnnie = tk.IntVar()
CounterBuyDarius = tk.IntVar()
CounterBuySejuani = tk.IntVar()
CounterBuyTahmKench = tk.IntVar()
CounterBuyAkali = tk.IntVar()
CounterBuyKennen = tk.IntVar()
CounterBuyShen = tk.IntVar()
CounterBuyZed = tk.IntVar()
CounterBuyDiana = tk.IntVar()
CounterBuyKindred = tk.IntVar()
CounterBuyTeemo = tk.IntVar()
CounterBuyYuumi = tk.IntVar()
CounterBuySett = tk.IntVar()
CounterBuyAzir = tk.IntVar()
CounterBuyGaren = tk.IntVar()
CounterBuyJarvanIV = tk.IntVar()
CounterBuyKatarina = tk.IntVar()
CounterBuyNidalee = tk.IntVar()
CounterBuyTryndamere = tk.IntVar()
CounterBuyVi = tk.IntVar()


if VARIABLE_PRINT_MODE:
    print("origin_champs_counters_to_buy = [")
    for champ in df.champion:
        print("CounterBuy" + champ, end=", ")
    print("]")
    print()

origin_champs_counters_to_buy = [
    CounterBuyAatrox,
    CounterBuyElise,
    CounterBuyKalista,
    CounterBuyPyke,
    CounterBuySivir,
    CounterBuyTwistedFate,
    CounterBuyVladimir,
    CounterBuyZilean,
    CounterBuySamira,
    CounterBuyJax,
    CounterBuyKayle,
    CounterBuyLeeSin,
    CounterBuyNasus,
    CounterBuyWukong,
    CounterBuyAurelionSol,
    CounterBuyBrand,
    CounterBuyBraum,
    CounterBuyOlaf,
    CounterBuyShyvana,
    CounterBuySwain,
    CounterBuyTristana,
    CounterBuyLulu,
    CounterBuyMaokai,
    CounterBuyNunu,
    CounterBuyOrnn,
    CounterBuyRakan,
    CounterBuyVeigar,
    CounterBuyXayah,
    CounterBuyFiora,
    CounterBuyIrelia,
    CounterBuyJanna,
    CounterBuyMorgana,
    CounterBuyTalon,
    CounterBuyYasuo,
    CounterBuyYone,
    CounterBuyChogath,
    CounterBuyNautilus,
    CounterBuyNeeko,
    CounterBuyAnnie,
    CounterBuyDarius,
    CounterBuySejuani,
    CounterBuyTahmKench,
    CounterBuyAkali,
    CounterBuyKennen,
    CounterBuyShen,
    CounterBuyZed,
    CounterBuyDiana,
    CounterBuyKindred,
    CounterBuyTeemo,
    CounterBuyYuumi,
    CounterBuySett,
    CounterBuyAzir,
    CounterBuyGaren,
    CounterBuyJarvanIV,
    CounterBuyKatarina,
    CounterBuyNidalee,
    CounterBuyTryndamere,
    CounterBuyVi,
]

# counters for origins

if VARIABLE_PRINT_MODE:
    for origin in origin_list:
        print("Counter" + origin + " = tk.IntVar()")


CounterCultist = tk.IntVar()
CounterDaredevil = tk.IntVar()
CounterDivine = tk.IntVar()
CounterDragonsoul = tk.IntVar()
CounterElderwood = tk.IntVar()
CounterEnlightened = tk.IntVar()
CounterExile = tk.IntVar()
CounterFabled = tk.IntVar()
CounterFortune = tk.IntVar()
CounterNinja = tk.IntVar()
CounterSpirit = tk.IntVar()
CounterTheBoss = tk.IntVar()
CounterWarlord = tk.IntVar()


if VARIABLE_PRINT_MODE:
    print("origin_counters = [")
    for origin in origin_list:
        print("Counter" + origin, end=", ")
    print("]")


origin_counters = [
    CounterCultist,
    CounterDaredevil,
    CounterDivine,
    CounterDragonsoul,
    CounterElderwood,
    CounterEnlightened,
    CounterExile,
    CounterFabled,
    CounterFortune,
    CounterNinja,
    CounterSpirit,
    CounterTheBoss,
    CounterWarlord,
]

# counters for classes


if VARIABLE_PRINT_MODE:
    for clas in class_list:
        print("Counter" + clas + " = tk.IntVar()")


CounterAdept = tk.IntVar()
CounterAssassin = tk.IntVar()
CounterBlacksmith = tk.IntVar()
CounterBrawler = tk.IntVar()
CounterDuelist = tk.IntVar()
CounterEmperor = tk.IntVar()
CounterExecutioner = tk.IntVar()
CounterKeeper = tk.IntVar()
CounterMage = tk.IntVar()
CounterMystic = tk.IntVar()
CounterSharpshooter = tk.IntVar()
CounterSlayer = tk.IntVar()
CounterSyphoner = tk.IntVar()
CounterVanguard = tk.IntVar()


if VARIABLE_PRINT_MODE:
    print("class_counters = [")
    for clas in class_list:
        print("Counter" + clas, end=", ")
    print("]")

class_counters = [
    CounterAdept,
    CounterAssassin,
    CounterBlacksmith,
    CounterBrawler,
    CounterDuelist,
    CounterEmperor,
    CounterExecutioner,
    CounterKeeper,
    CounterMage,
    CounterMystic,
    CounterSharpshooter,
    CounterSlayer,
    CounterSyphoner,
    CounterVanguard,
]


# Champion namedtuple things


champion_info = []
logging.debug("Filling champion_info in purpose of creating namedtuple")
for i, champ in enumerate(df.champion):
    champion_info.append(
        [
            champ,
            champions_list_for_ocr[i],
            i,
            origin_champs_counters[i],
            df.origin_prim[i],
            df.origin_sec[i],
            df.class_prim[i],
            df.class_sec[i],
        ]
    )
logging.debug("First filling champion_info has ended.")


champion_to_buy_info = []
logging.debug("Filling champion_to_buy_info in purpose of creating namedtuple")
for i, champ in enumerate(df.champion):
    champion_to_buy_info.append(
        [
            champ,
            champions_list_for_ocr[i],
            i,
            origin_champs_counters_to_buy[i],
            df.origin_prim[i],
            df.origin_sec[i],
            df.class_prim[i],
            df.class_sec[i],
        ]
    )
logging.debug("First filling champion_to_buy_info has ended.")


dss.append_counters_to_input_list(
    champion_info,
    origin_list_=origin_list,
    class_list_=class_list,
    origin_counters_=origin_counters,
    class_counters_=class_counters,
    df_=df,
)

dss.append_counters_to_input_list(
    champion_to_buy_info,
    origin_list_=origin_list,
    class_list_=class_list,
    origin_counters_=origin_counters,
    class_counters_=class_counters,
    df_=df,
)

champion_info_df = pd.DataFrame.from_records(
    champion_info,
    columns=[
        "champion",
        "name_ocr",
        "index_ocr",
        "ChampCounter",
        "origin_prim",
        "origin_sec",
        "class_prim",
        "class_sec",
        "OriginPrimCounter",
        "OriginSecCounter",
        "ClassPrimCounter",
        "ClassSecCounter",
    ],
)

champion_to_buy_info_df = pd.DataFrame.from_records(
    champion_info,
    columns=[
        "champion",
        "name_ocr",
        "index_ocr",
        "ChampCounter",
        "origin_prim",
        "origin_sec",
        "class_prim",
        "class_sec",
        "OriginPrimCounter",
        "OriginSecCounter",
        "ClassPrimCounter",
        "ClassSecCounter",
    ],
)


if VARIABLE_PRINT_MODE:
    for i, champ in enumerate(champion_info):
        print(champ[0] + " = Champion(*champion_info[%d])" % i)

Aatrox = Champion(*champion_info[0])
Elise = Champion(*champion_info[1])
Kalista = Champion(*champion_info[2])
Pyke = Champion(*champion_info[3])
Sivir = Champion(*champion_info[4])
TwistedFate = Champion(*champion_info[5])
Vladimir = Champion(*champion_info[6])
Zilean = Champion(*champion_info[7])
Samira = Champion(*champion_info[8])
Jax = Champion(*champion_info[9])
Kayle = Champion(*champion_info[10])
LeeSin = Champion(*champion_info[11])
Nasus = Champion(*champion_info[12])
Wukong = Champion(*champion_info[13])
AurelionSol = Champion(*champion_info[14])
Brand = Champion(*champion_info[15])
Braum = Champion(*champion_info[16])
Olaf = Champion(*champion_info[17])
Shyvana = Champion(*champion_info[18])
Swain = Champion(*champion_info[19])
Tristana = Champion(*champion_info[20])
Lulu = Champion(*champion_info[21])
Maokai = Champion(*champion_info[22])
Nunu = Champion(*champion_info[23])
Ornn = Champion(*champion_info[24])
Rakan = Champion(*champion_info[25])
Veigar = Champion(*champion_info[26])
Xayah = Champion(*champion_info[27])
Fiora = Champion(*champion_info[28])
Irelia = Champion(*champion_info[29])
Janna = Champion(*champion_info[30])
Morgana = Champion(*champion_info[31])
Talon = Champion(*champion_info[32])
Yasuo = Champion(*champion_info[33])
Yone = Champion(*champion_info[34])
Chogath = Champion(*champion_info[35])
Nautilus = Champion(*champion_info[36])
Neeko = Champion(*champion_info[37])
Annie = Champion(*champion_info[38])
Darius = Champion(*champion_info[39])
Sejuani = Champion(*champion_info[40])
TahmKench = Champion(*champion_info[41])
Akali = Champion(*champion_info[42])
Kennen = Champion(*champion_info[43])
Shen = Champion(*champion_info[44])
Zed = Champion(*champion_info[45])
Diana = Champion(*champion_info[46])
Kindred = Champion(*champion_info[47])
Teemo = Champion(*champion_info[48])
Yuumi = Champion(*champion_info[49])
Sett = Champion(*champion_info[50])
Azir = Champion(*champion_info[51])
Garen = Champion(*champion_info[52])
JarvanIV = Champion(*champion_info[53])
Katarina = Champion(*champion_info[54])
Nidalee = Champion(*champion_info[55])
Tryndamere = Champion(*champion_info[56])
Vi = Champion(*champion_info[57])


if VARIABLE_PRINT_MODE:
    print("champions_list = [")
    for champ in champion_info:
        print(champ[0], end=", ")
    print("]")
    print()


champions_list = [
    Aatrox,
    Elise,
    Kalista,
    Pyke,
    Sivir,
    TwistedFate,
    Vladimir,
    Zilean,
    Samira,
    Jax,
    Kayle,
    LeeSin,
    Nasus,
    Wukong,
    AurelionSol,
    Brand,
    Braum,
    Olaf,
    Shyvana,
    Swain,
    Tristana,
    Lulu,
    Maokai,
    Nunu,
    Ornn,
    Rakan,
    Veigar,
    Xayah,
    Fiora,
    Irelia,
    Janna,
    Morgana,
    Talon,
    Yasuo,
    Yone,
    Chogath,
    Nautilus,
    Neeko,
    Annie,
    Darius,
    Sejuani,
    TahmKench,
    Akali,
    Kennen,
    Shen,
    Zed,
    Diana,
    Kindred,
    Teemo,
    Yuumi,
    Sett,
    Azir,
    Garen,
    JarvanIV,
    Katarina,
    Nidalee,
    Tryndamere,
    Vi,
]


if VARIABLE_PRINT_MODE:
    for i, champ in enumerate(champion_to_buy_info):
        print(champ[0] + "ToBuy" + " = Champion(*champion_to_buy_info[{}])".format(i))

AatroxToBuy = Champion(*champion_to_buy_info[0])
EliseToBuy = Champion(*champion_to_buy_info[1])
KalistaToBuy = Champion(*champion_to_buy_info[2])
PykeToBuy = Champion(*champion_to_buy_info[3])
SivirToBuy = Champion(*champion_to_buy_info[4])
TwistedFateToBuy = Champion(*champion_to_buy_info[5])
VladimirToBuy = Champion(*champion_to_buy_info[6])
ZileanToBuy = Champion(*champion_to_buy_info[7])
SamiraToBuy = Champion(*champion_to_buy_info[8])
JaxToBuy = Champion(*champion_to_buy_info[9])
KayleToBuy = Champion(*champion_to_buy_info[10])
LeeSinToBuy = Champion(*champion_to_buy_info[11])
NasusToBuy = Champion(*champion_to_buy_info[12])
WukongToBuy = Champion(*champion_to_buy_info[13])
AurelionSolToBuy = Champion(*champion_to_buy_info[14])
BrandToBuy = Champion(*champion_to_buy_info[15])
BraumToBuy = Champion(*champion_to_buy_info[16])
OlafToBuy = Champion(*champion_to_buy_info[17])
ShyvanaToBuy = Champion(*champion_to_buy_info[18])
SwainToBuy = Champion(*champion_to_buy_info[19])
TristanaToBuy = Champion(*champion_to_buy_info[20])
LuluToBuy = Champion(*champion_to_buy_info[21])
MaokaiToBuy = Champion(*champion_to_buy_info[22])
NunuToBuy = Champion(*champion_to_buy_info[23])
OrnnToBuy = Champion(*champion_to_buy_info[24])
RakanToBuy = Champion(*champion_to_buy_info[25])
VeigarToBuy = Champion(*champion_to_buy_info[26])
XayahToBuy = Champion(*champion_to_buy_info[27])
FioraToBuy = Champion(*champion_to_buy_info[28])
IreliaToBuy = Champion(*champion_to_buy_info[29])
JannaToBuy = Champion(*champion_to_buy_info[30])
MorganaToBuy = Champion(*champion_to_buy_info[31])
TalonToBuy = Champion(*champion_to_buy_info[32])
YasuoToBuy = Champion(*champion_to_buy_info[33])
YoneToBuy = Champion(*champion_to_buy_info[34])
ChogathToBuy = Champion(*champion_to_buy_info[35])
NautilusToBuy = Champion(*champion_to_buy_info[36])
NeekoToBuy = Champion(*champion_to_buy_info[37])
AnnieToBuy = Champion(*champion_to_buy_info[38])
DariusToBuy = Champion(*champion_to_buy_info[39])
SejuaniToBuy = Champion(*champion_to_buy_info[40])
TahmKenchToBuy = Champion(*champion_to_buy_info[41])
AkaliToBuy = Champion(*champion_to_buy_info[42])
KennenToBuy = Champion(*champion_to_buy_info[43])
ShenToBuy = Champion(*champion_to_buy_info[44])
ZedToBuy = Champion(*champion_to_buy_info[45])
DianaToBuy = Champion(*champion_to_buy_info[46])
KindredToBuy = Champion(*champion_to_buy_info[47])
TeemoToBuy = Champion(*champion_to_buy_info[48])
YuumiToBuy = Champion(*champion_to_buy_info[49])
SettToBuy = Champion(*champion_to_buy_info[50])
AzirToBuy = Champion(*champion_to_buy_info[51])
GarenToBuy = Champion(*champion_to_buy_info[52])
JarvanIVToBuy = Champion(*champion_to_buy_info[53])
KatarinaToBuy = Champion(*champion_to_buy_info[54])
NidaleeToBuy = Champion(*champion_to_buy_info[55])
TryndamereToBuy = Champion(*champion_to_buy_info[56])
ViToBuy = Champion(*champion_to_buy_info[57])


if VARIABLE_PRINT_MODE:
    print("champions_to_buy_list = [")
    for champ in champion_to_buy_info:
        print(champ[0] + "ToBuy", end=", ")
    print("]")
    print()


champions_to_buy_list = [
    AatroxToBuy,
    EliseToBuy,
    KalistaToBuy,
    PykeToBuy,
    SivirToBuy,
    TwistedFateToBuy,
    VladimirToBuy,
    ZileanToBuy,
    SamiraToBuy,
    JaxToBuy,
    KayleToBuy,
    LeeSinToBuy,
    NasusToBuy,
    WukongToBuy,
    AurelionSolToBuy,
    BrandToBuy,
    BraumToBuy,
    OlafToBuy,
    ShyvanaToBuy,
    SwainToBuy,
    TristanaToBuy,
    LuluToBuy,
    MaokaiToBuy,
    NunuToBuy,
    OrnnToBuy,
    RakanToBuy,
    VeigarToBuy,
    XayahToBuy,
    FioraToBuy,
    IreliaToBuy,
    JannaToBuy,
    MorganaToBuy,
    TalonToBuy,
    YasuoToBuy,
    YoneToBuy,
    ChogathToBuy,
    NautilusToBuy,
    NeekoToBuy,
    AnnieToBuy,
    DariusToBuy,
    SejuaniToBuy,
    TahmKenchToBuy,
    AkaliToBuy,
    KennenToBuy,
    ShenToBuy,
    ZedToBuy,
    DianaToBuy,
    KindredToBuy,
    TeemoToBuy,
    YuumiToBuy,
    SettToBuy,
    AzirToBuy,
    GarenToBuy,
    JarvanIVToBuy,
    KatarinaToBuy,
    NidaleeToBuy,
    TryndamereToBuy,
    ViToBuy,
]


# GUI


LabelTitle = tk.Label(MainWindow, text="Champion pool", font=BOLDED_FONT)
LabelTitle.grid(row=0, column=SHIFT_BETWEEN_ORIGINS * 5)

LabelTitle = tk.Label(MainWindow, text=origin_list[0])
LabelTitle.grid(row=1, column=ORIGIN_LABEL_POSITION_COLUMN)

LabelTitle = tk.Label(MainWindow, text="Champions to buy", font=BOLDED_FONT)
LabelTitle.grid(row=DOWNSIDE - 1, column=SHIFT_BETWEEN_ORIGINS * 5)

# CHAMPIONS
for i in range(0, len(origin_champs_from_df_list), 1):
    dss.show_champions_from_origin(
        window_tk=MainWindow,
        origin_index=i,
        origin_champs_from_df_list_=origin_champs_from_df_list[i],
        origin_list_=origin_list,
        champions_list_=champions_list,
        shift_between_upside_downside=UPSIDE,
    )

for i in range(0, len(origin_champs_from_df_list), 1):
    dss.show_champions_from_origin(
        window_tk=MainWindow,
        origin_index=i,
        origin_champs_from_df_list_=origin_champs_from_df_list[i],
        origin_list_=origin_list,
        champions_list_=champions_to_buy_list,
        shift_between_upside_downside=DOWNSIDE,
    )

# ORIGINS
dss.show_classes_or_origins(
    window_tk=MainWindow,
    origin_or_class_list=origin_list,
    origin_or_class_counters_list=origin_counters,
    shift_between_upside_downside=UPSIDE,
    origin_or_class_string="Origins",
)

# CLASSES
dss.show_classes_or_origins(
    window_tk=MainWindow,
    origin_or_class_list=class_list,
    origin_or_class_counters_list=class_counters,
    shift_between_upside_downside=UPSIDE,
    origin_or_class_string="Classes",
)
Labeling = tk.Label(MainWindow, text="Left to buy", font=BOLDED_FONT)
Labeling.grid(row=12 + 0, column=0)

Labeling = tk.Label(MainWindow, text="Points", font=BOLDED_FONT)
Labeling.grid(row=14 + 0, column=0)

ButtonCal = tk.Button(
    MainWindow,
    text="reset",
    command=lambda: dss.reset_counters_in_list(origin_champs_counters_to_buy),
)
ButtonCal.grid(row=DOWNSIDE, column=6)

ButtonCal = tk.Button(
    MainWindow,
    text="update classes",
    command=lambda: dss.update_classes_and_origins(
        origin_list_=origin_list,
        champions_list_=champions_list,
        origin_counters_=origin_counters,
        class_list_=class_list,
        class_counters_=class_counters,
    ),
)
ButtonCal.grid(row=DOWNSIDE, column=12)


ButtonCal = tk.Button(
    MainWindow,
    text="show points",
    command=lambda: dss.show_nonzero_counters_with_points(
        tk_window=MainWindow,
        origin_champs_counters_=origin_champs_counters,
        origin_champs_counters_to_buy_=origin_champs_counters_to_buy,
        champions_list_=champions_list,
        df_=df,
        origin_list_=origin_list,
        origin_counters_=origin_counters,
        class_list_=class_list,
        class_counters_=class_counters,
    ),
)
ButtonCal.grid(row=DOWNSIDE, column=18)

ButtonCal = tk.Button(
    MainWindow,
    text="OCR",
    command=lambda: dss.update_champions_to_buy_from_ocr_detection(
        champions_list_for_ocr, origin_champs_counters_to_buy, reader_=reader
    ),
)
ButtonCal.grid(row=DOWNSIDE, column=24)

ButtonCal = tk.Button(
    MainWindow,
    text="draw rectangles",
    command=lambda: dss.draw_on_champion_to_buy_cards(
        rgb_colours_list_=rgb_colours_list,
        champions_list_for_ocr_=champions_list_for_ocr,
        origin_champs_counters_to_buy_=origin_champs_counters_to_buy,
        reader_=reader,
        tk_window=MainWindow,
        origin_champs_counters_=origin_champs_counters,
        df_=df,
        origin_list_=origin_list,
        champions_list_=champions_list,
        origin_counters_=origin_counters,
        class_list_=class_list,
        class_counters_=class_counters,
    ),
)
ButtonCal.grid(row=DOWNSIDE, column=30)

ButtonCal = tk.Button(
    MainWindow,
    text="scan&go",
    command=lambda: dss.draw_rectangles_show_points_show_buttons_reset_counters(
        rgb_colours_list_=rgb_colours_list,
        champions_list_for_ocr_=champions_list_for_ocr,
        origin_champs_counters_to_buy_=origin_champs_counters_to_buy,
        reader_=reader,
        tk_window=MainWindow,
        origin_champs_counters_=origin_champs_counters,
        df_=df,
        origin_list_=origin_list,
        champions_list_=champions_list,
        origin_counters_=origin_counters,
        class_list_=class_list,
        class_counters_=class_counters,
    ),
)
ButtonCal.grid(row=DOWNSIDE, column=36)

MainWindow.attributes("-alpha", 0.9)
MainWindow.mainloop()
