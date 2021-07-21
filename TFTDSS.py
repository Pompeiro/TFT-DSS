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
IMAGE_DEBUG_MODE_FULLSCREEN = 0

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
CHAMPIONS_TO_BUY_VISIBLE = 0
# CHAMPIONS_TO_BUY_VISIBLE = 1
# TEST_BUTTON_VISIBLE = 0
TEST_BUTTON_VISIBLE = 1

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

if CHAMPIONS_TO_BUY_VISIBLE:
    MainWindow = tk.Tk()
    MainWindow.geometry("1900x800+0+0")
    MainWindow.title("TFTDSS")
else:
    MainWindow = tk.Tk()
    MainWindow.geometry("1900x450+0+0")
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
    "Brand",
    "Fiddlesticks",
    "Kalista",
    "Nunu & Willump",
    "Garen",
    "Gragas",
    "Karma",
    "Kha Zix",
    "Nidalee",
    "Riven",
    "Soraka",
    "Ashe",
    "Galio",
    "Heimerdinger",
    "Sett",
    "Udyr",
    "Zyra",
    "Draven",
    "Hecarim",
    "Miss Fortune",
    "Thresh",
    "Vayne",
    "Viego",
    "Kennen",
    "Kled",
    "Lulu",
    "Poppy",
    "Teemo",
    "Tristana",
    "Ziggs",
    "Gwen",
    "Jax",
    "Nautilus",
    "Aphelios",
    "Diana",
    "Lee Sin",
    "Sejuani",
    "Vladimir",
    "Yasuo",
    "Aatrox",
    "Kayle",
    "Leona",
    "Lux",
    "Rell",
    "Syndra",
    "Varus",
    "Vel'Koz",
    "Ivern",
    "Nocturne",
    "Volibear",
    "Akshan",
    "Irelia",
    "Lucian",
    "Olaf",
    "Pyke",
    "Rakan",
    "Senna",
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

abomination_champs = list(df.query('origin_prim == "Abomination"').champion)
dawnbringer_champs = list(df.query('origin_prim == "Dawnbringer"').champion)
draconic_champs = list(df.query('origin_prim == "Draconic"').champion)
forgotten_champs = list(df.query('origin_prim == "Forgotten"').champion)
hellion_champs = list(df.query('origin_prim == "Hellion"').champion)
inanimate_champs = list(df.query('origin_prim == "Inanimate"').champion)
ironclad_champs = list(df.query('origin_prim == "Ironclad"').champion)
nightbringer_champs = list(df.query('origin_prim == "Nightbringer"').champion)
redeemed_champs = list(df.query('origin_prim == "Redeemed"').champion)
revenant_champs = list(df.query('origin_prim == "Revenant"').champion)
sentinel_champs = list(df.query('origin_prim == "Sentinel"').champion)

origin_champs_from_df_list = [
    abomination_champs,
    dawnbringer_champs,
    draconic_champs,
    forgotten_champs,
    hellion_champs,
    inanimate_champs,
    ironclad_champs,
    nightbringer_champs,
    redeemed_champs,
    revenant_champs,
    sentinel_champs,
]


class_list = list(set(df.class_prim)) + list(set(df.class_sec))
class_list = list(set(class_list))
class_list.remove("None")
class_list.sort()


# COUNTERS FOR CHAMPIONS IN POOL

if VARIABLE_PRINT_MODE:
    for champ in df.champion:
        print("Counter" + champ + " = tk.IntVar()")


CounterBrand = tk.IntVar()
CounterFiddlesticks = tk.IntVar()
CounterKalista = tk.IntVar()
CounterNunu = tk.IntVar()
CounterGaren = tk.IntVar()
CounterGragas = tk.IntVar()
CounterKarma = tk.IntVar()
CounterKhazix = tk.IntVar()
CounterNidalee = tk.IntVar()
CounterRiven = tk.IntVar()
CounterSoraka = tk.IntVar()
CounterAshe = tk.IntVar()
CounterGalio = tk.IntVar()
CounterHeimerdinger = tk.IntVar()
CounterSett = tk.IntVar()
CounterUdyr = tk.IntVar()
CounterZyra = tk.IntVar()
CounterDraven = tk.IntVar()
CounterHecarim = tk.IntVar()
CounterMissFortune = tk.IntVar()
CounterThresh = tk.IntVar()
CounterVayne = tk.IntVar()
CounterViego = tk.IntVar()
CounterKennen = tk.IntVar()
CounterKled = tk.IntVar()
CounterLulu = tk.IntVar()
CounterPoppy = tk.IntVar()
CounterTeemo = tk.IntVar()
CounterTristana = tk.IntVar()
CounterZiggs = tk.IntVar()
CounterGwen = tk.IntVar()
CounterJax = tk.IntVar()
CounterNautilus = tk.IntVar()
CounterAphelios = tk.IntVar()
CounterDiana = tk.IntVar()
CounterLeeSin = tk.IntVar()
CounterSejuani = tk.IntVar()
CounterVladimir = tk.IntVar()
CounterYasuo = tk.IntVar()
CounterAatrox = tk.IntVar()
CounterKayle = tk.IntVar()
CounterLeona = tk.IntVar()
CounterLux = tk.IntVar()
CounterRell = tk.IntVar()
CounterSyndra = tk.IntVar()
CounterVarus = tk.IntVar()
CounterVelkoz = tk.IntVar()
CounterIvern = tk.IntVar()
CounterNocturne = tk.IntVar()
CounterVolibear = tk.IntVar()
CounterAkshan = tk.IntVar()
CounterIrelia = tk.IntVar()
CounterLucian = tk.IntVar()
CounterOlaf = tk.IntVar()
CounterPyke = tk.IntVar()
CounterRakan = tk.IntVar()
CounterSenna = tk.IntVar()

if VARIABLE_PRINT_MODE:
    print("origin_champs_counters = [")
    for champ in df.champion:
        print("Counter" + champ, end=", ")
    print("]")
    print()

origin_champs_counters = [
    CounterBrand,
    CounterFiddlesticks,
    CounterKalista,
    CounterNunu,
    CounterGaren,
    CounterGragas,
    CounterKarma,
    CounterKhazix,
    CounterNidalee,
    CounterRiven,
    CounterSoraka,
    CounterAshe,
    CounterGalio,
    CounterHeimerdinger,
    CounterSett,
    CounterUdyr,
    CounterZyra,
    CounterDraven,
    CounterHecarim,
    CounterMissFortune,
    CounterThresh,
    CounterVayne,
    CounterViego,
    CounterKennen,
    CounterKled,
    CounterLulu,
    CounterPoppy,
    CounterTeemo,
    CounterTristana,
    CounterZiggs,
    CounterGwen,
    CounterJax,
    CounterNautilus,
    CounterAphelios,
    CounterDiana,
    CounterLeeSin,
    CounterSejuani,
    CounterVladimir,
    CounterYasuo,
    CounterAatrox,
    CounterKayle,
    CounterLeona,
    CounterLux,
    CounterRell,
    CounterSyndra,
    CounterVarus,
    CounterVelkoz,
    CounterIvern,
    CounterNocturne,
    CounterVolibear,
    CounterAkshan,
    CounterIrelia,
    CounterLucian,
    CounterOlaf,
    CounterPyke,
    CounterRakan,
    CounterSenna,
]

# COUNTERS for champions to buy

if VARIABLE_PRINT_MODE:
    for champ in df.champion:
        print("CounterBuy" + champ + " = tk.IntVar()")


CounterBuyBrand = tk.IntVar()
CounterBuyFiddlesticks = tk.IntVar()
CounterBuyKalista = tk.IntVar()
CounterBuyNunu = tk.IntVar()
CounterBuyGaren = tk.IntVar()
CounterBuyGragas = tk.IntVar()
CounterBuyKarma = tk.IntVar()
CounterBuyKhazix = tk.IntVar()
CounterBuyNidalee = tk.IntVar()
CounterBuyRiven = tk.IntVar()
CounterBuySoraka = tk.IntVar()
CounterBuyAshe = tk.IntVar()
CounterBuyGalio = tk.IntVar()
CounterBuyHeimerdinger = tk.IntVar()
CounterBuySett = tk.IntVar()
CounterBuyUdyr = tk.IntVar()
CounterBuyZyra = tk.IntVar()
CounterBuyDraven = tk.IntVar()
CounterBuyHecarim = tk.IntVar()
CounterBuyMissFortune = tk.IntVar()
CounterBuyThresh = tk.IntVar()
CounterBuyVayne = tk.IntVar()
CounterBuyViego = tk.IntVar()
CounterBuyKennen = tk.IntVar()
CounterBuyKled = tk.IntVar()
CounterBuyLulu = tk.IntVar()
CounterBuyPoppy = tk.IntVar()
CounterBuyTeemo = tk.IntVar()
CounterBuyTristana = tk.IntVar()
CounterBuyZiggs = tk.IntVar()
CounterBuyGwen = tk.IntVar()
CounterBuyJax = tk.IntVar()
CounterBuyNautilus = tk.IntVar()
CounterBuyAphelios = tk.IntVar()
CounterBuyDiana = tk.IntVar()
CounterBuyLeeSin = tk.IntVar()
CounterBuySejuani = tk.IntVar()
CounterBuyVladimir = tk.IntVar()
CounterBuyYasuo = tk.IntVar()
CounterBuyAatrox = tk.IntVar()
CounterBuyKayle = tk.IntVar()
CounterBuyLeona = tk.IntVar()
CounterBuyLux = tk.IntVar()
CounterBuyRell = tk.IntVar()
CounterBuySyndra = tk.IntVar()
CounterBuyVarus = tk.IntVar()
CounterBuyVelkoz = tk.IntVar()
CounterBuyIvern = tk.IntVar()
CounterBuyNocturne = tk.IntVar()
CounterBuyVolibear = tk.IntVar()
CounterBuyAkshan = tk.IntVar()
CounterBuyIrelia = tk.IntVar()
CounterBuyLucian = tk.IntVar()
CounterBuyOlaf = tk.IntVar()
CounterBuyPyke = tk.IntVar()
CounterBuyRakan = tk.IntVar()
CounterBuySenna = tk.IntVar()


if VARIABLE_PRINT_MODE:
    print("origin_champs_counters_to_buy = [")
    for champ in df.champion:
        print("CounterBuy" + champ, end=", ")
    print("]")
    print()

origin_champs_counters_to_buy = [
    CounterBuyBrand,
    CounterBuyFiddlesticks,
    CounterBuyKalista,
    CounterBuyNunu,
    CounterBuyGaren,
    CounterBuyGragas,
    CounterBuyKarma,
    CounterBuyKhazix,
    CounterBuyNidalee,
    CounterBuyRiven,
    CounterBuySoraka,
    CounterBuyAshe,
    CounterBuyGalio,
    CounterBuyHeimerdinger,
    CounterBuySett,
    CounterBuyUdyr,
    CounterBuyZyra,
    CounterBuyDraven,
    CounterBuyHecarim,
    CounterBuyMissFortune,
    CounterBuyThresh,
    CounterBuyVayne,
    CounterBuyViego,
    CounterBuyKennen,
    CounterBuyKled,
    CounterBuyLulu,
    CounterBuyPoppy,
    CounterBuyTeemo,
    CounterBuyTristana,
    CounterBuyZiggs,
    CounterBuyGwen,
    CounterBuyJax,
    CounterBuyNautilus,
    CounterBuyAphelios,
    CounterBuyDiana,
    CounterBuyLeeSin,
    CounterBuySejuani,
    CounterBuyVladimir,
    CounterBuyYasuo,
    CounterBuyAatrox,
    CounterBuyKayle,
    CounterBuyLeona,
    CounterBuyLux,
    CounterBuyRell,
    CounterBuySyndra,
    CounterBuyVarus,
    CounterBuyVelkoz,
    CounterBuyIvern,
    CounterBuyNocturne,
    CounterBuyVolibear,
    CounterBuyAkshan,
    CounterBuyIrelia,
    CounterBuyLucian,
    CounterBuyOlaf,
    CounterBuyPyke,
    CounterBuyRakan,
    CounterBuySenna,
]

# counters for origins

if VARIABLE_PRINT_MODE:
    for origin in origin_list:
        print("Counter" + origin + " = tk.IntVar()")


CounterAbomination = tk.IntVar()
CounterDawnbringer = tk.IntVar()
CounterDraconic = tk.IntVar()
CounterForgotten = tk.IntVar()
CounterHellion = tk.IntVar()
CounterInanimate = tk.IntVar()
CounterIronclad = tk.IntVar()
CounterNightbringer = tk.IntVar()
CounterRedeemed = tk.IntVar()
CounterRevenant = tk.IntVar()
CounterSentinel = tk.IntVar()


if VARIABLE_PRINT_MODE:
    print("origin_counters = [")
    for origin in origin_list:
        print("Counter" + origin, end=", ")
    print("]")


origin_counters = [
    CounterAbomination,
    CounterDawnbringer,
    CounterDraconic,
    CounterForgotten,
    CounterHellion,
    CounterInanimate,
    CounterIronclad,
    CounterNightbringer,
    CounterRedeemed,
    CounterRevenant,
    CounterSentinel,
]

# counters for classes


if VARIABLE_PRINT_MODE:
    for clas in class_list:
        print("Counter" + clas + " = tk.IntVar()")


CounterAssassin = tk.IntVar()
CounterBrawler = tk.IntVar()
CounterCannoneer = tk.IntVar()
CounterCaretaker = tk.IntVar()
CounterCavalier = tk.IntVar()
CounterCruel = tk.IntVar()
CounterInvoker = tk.IntVar()
CounterKnight = tk.IntVar()
CounterLegionnaire = tk.IntVar()
CounterMystic = tk.IntVar()
CounterRanger = tk.IntVar()
CounterRenewer = tk.IntVar()
CounterSkirmisher = tk.IntVar()
CounterSpellweaver = tk.IntVar()
CounterVictorious = tk.IntVar()


if VARIABLE_PRINT_MODE:
    print("class_counters = [")
    for clas in class_list:
        print("Counter" + clas, end=", ")
    print("]")

class_counters = [
    CounterAssassin,
    CounterBrawler,
    CounterCannoneer,
    CounterCaretaker,
    CounterCavalier,
    CounterCruel,
    CounterInvoker,
    CounterKnight,
    CounterLegionnaire,
    CounterMystic,
    CounterRanger,
    CounterRenewer,
    CounterSkirmisher,
    CounterSpellweaver,
    CounterVictorious,
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

Brand = Champion(*champion_info[0])
Fiddlesticks = Champion(*champion_info[1])
Kalista = Champion(*champion_info[2])
Nunu = Champion(*champion_info[3])
Garen = Champion(*champion_info[4])
Gragas = Champion(*champion_info[5])
Karma = Champion(*champion_info[6])
Khazix = Champion(*champion_info[7])
Nidalee = Champion(*champion_info[8])
Riven = Champion(*champion_info[9])
Soraka = Champion(*champion_info[10])
Ashe = Champion(*champion_info[11])
Galio = Champion(*champion_info[12])
Heimerdinger = Champion(*champion_info[13])
Sett = Champion(*champion_info[14])
Udyr = Champion(*champion_info[15])
Zyra = Champion(*champion_info[16])
Draven = Champion(*champion_info[17])
Hecarim = Champion(*champion_info[18])
MissFortune = Champion(*champion_info[19])
Thresh = Champion(*champion_info[20])
Vayne = Champion(*champion_info[21])
Viego = Champion(*champion_info[22])
Kennen = Champion(*champion_info[23])
Kled = Champion(*champion_info[24])
Lulu = Champion(*champion_info[25])
Poppy = Champion(*champion_info[26])
Teemo = Champion(*champion_info[27])
Tristana = Champion(*champion_info[28])
Ziggs = Champion(*champion_info[29])
Gwen = Champion(*champion_info[30])
Jax = Champion(*champion_info[31])
Nautilus = Champion(*champion_info[32])
Aphelios = Champion(*champion_info[33])
Diana = Champion(*champion_info[34])
LeeSin = Champion(*champion_info[35])
Sejuani = Champion(*champion_info[36])
Vladimir = Champion(*champion_info[37])
Yasuo = Champion(*champion_info[38])
Aatrox = Champion(*champion_info[39])
Kayle = Champion(*champion_info[40])
Leona = Champion(*champion_info[41])
Lux = Champion(*champion_info[42])
Rell = Champion(*champion_info[43])
Syndra = Champion(*champion_info[44])
Varus = Champion(*champion_info[45])
Velkoz = Champion(*champion_info[46])
Ivern = Champion(*champion_info[47])
Nocturne = Champion(*champion_info[48])
Volibear = Champion(*champion_info[49])
Akshan = Champion(*champion_info[50])
Irelia = Champion(*champion_info[51])
Lucian = Champion(*champion_info[52])
Olaf = Champion(*champion_info[53])
Pyke = Champion(*champion_info[54])
Rakan = Champion(*champion_info[55])
Senna = Champion(*champion_info[56])


if VARIABLE_PRINT_MODE:
    print("champions_list = [")
    for champ in champion_info:
        print(champ[0], end=", ")
    print("]")
    print()


champions_list = [
    Brand,
    Fiddlesticks,
    Kalista,
    Nunu,
    Garen,
    Gragas,
    Karma,
    Khazix,
    Nidalee,
    Riven,
    Soraka,
    Ashe,
    Galio,
    Heimerdinger,
    Sett,
    Udyr,
    Zyra,
    Draven,
    Hecarim,
    MissFortune,
    Thresh,
    Vayne,
    Viego,
    Kennen,
    Kled,
    Lulu,
    Poppy,
    Teemo,
    Tristana,
    Ziggs,
    Gwen,
    Jax,
    Nautilus,
    Aphelios,
    Diana,
    LeeSin,
    Sejuani,
    Vladimir,
    Yasuo,
    Aatrox,
    Kayle,
    Leona,
    Lux,
    Rell,
    Syndra,
    Varus,
    Velkoz,
    Ivern,
    Nocturne,
    Volibear,
    Akshan,
    Irelia,
    Lucian,
    Olaf,
    Pyke,
    Rakan,
    Senna,
]


if VARIABLE_PRINT_MODE:
    for i, champ in enumerate(champion_to_buy_info):
        print(champ[0] + "ToBuy" + " = Champion(*champion_to_buy_info[{}])".format(i))

BrandToBuy = Champion(*champion_to_buy_info[0])
FiddlesticksToBuy = Champion(*champion_to_buy_info[1])
KalistaToBuy = Champion(*champion_to_buy_info[2])
NunuToBuy = Champion(*champion_to_buy_info[3])
GarenToBuy = Champion(*champion_to_buy_info[4])
GragasToBuy = Champion(*champion_to_buy_info[5])
KarmaToBuy = Champion(*champion_to_buy_info[6])
KhazixToBuy = Champion(*champion_to_buy_info[7])
NidaleeToBuy = Champion(*champion_to_buy_info[8])
RivenToBuy = Champion(*champion_to_buy_info[9])
SorakaToBuy = Champion(*champion_to_buy_info[10])
AsheToBuy = Champion(*champion_to_buy_info[11])
GalioToBuy = Champion(*champion_to_buy_info[12])
HeimerdingerToBuy = Champion(*champion_to_buy_info[13])
SettToBuy = Champion(*champion_to_buy_info[14])
UdyrToBuy = Champion(*champion_to_buy_info[15])
ZyraToBuy = Champion(*champion_to_buy_info[16])
DravenToBuy = Champion(*champion_to_buy_info[17])
HecarimToBuy = Champion(*champion_to_buy_info[18])
MissFortuneToBuy = Champion(*champion_to_buy_info[19])
ThreshToBuy = Champion(*champion_to_buy_info[20])
VayneToBuy = Champion(*champion_to_buy_info[21])
ViegoToBuy = Champion(*champion_to_buy_info[22])
KennenToBuy = Champion(*champion_to_buy_info[23])
KledToBuy = Champion(*champion_to_buy_info[24])
LuluToBuy = Champion(*champion_to_buy_info[25])
PoppyToBuy = Champion(*champion_to_buy_info[26])
TeemoToBuy = Champion(*champion_to_buy_info[27])
TristanaToBuy = Champion(*champion_to_buy_info[28])
ZiggsToBuy = Champion(*champion_to_buy_info[29])
GwenToBuy = Champion(*champion_to_buy_info[30])
JaxToBuy = Champion(*champion_to_buy_info[31])
NautilusToBuy = Champion(*champion_to_buy_info[32])
ApheliosToBuy = Champion(*champion_to_buy_info[33])
DianaToBuy = Champion(*champion_to_buy_info[34])
LeeSinToBuy = Champion(*champion_to_buy_info[35])
SejuaniToBuy = Champion(*champion_to_buy_info[36])
VladimirToBuy = Champion(*champion_to_buy_info[37])
YasuoToBuy = Champion(*champion_to_buy_info[38])
AatroxToBuy = Champion(*champion_to_buy_info[39])
KayleToBuy = Champion(*champion_to_buy_info[40])
LeonaToBuy = Champion(*champion_to_buy_info[41])
LuxToBuy = Champion(*champion_to_buy_info[42])
RellToBuy = Champion(*champion_to_buy_info[43])
SyndraToBuy = Champion(*champion_to_buy_info[44])
VarusToBuy = Champion(*champion_to_buy_info[45])
VelkozToBuy = Champion(*champion_to_buy_info[46])
IvernToBuy = Champion(*champion_to_buy_info[47])
NocturneToBuy = Champion(*champion_to_buy_info[48])
VolibearToBuy = Champion(*champion_to_buy_info[49])
AkshanToBuy = Champion(*champion_to_buy_info[50])
IreliaToBuy = Champion(*champion_to_buy_info[51])
LucianToBuy = Champion(*champion_to_buy_info[52])
OlafToBuy = Champion(*champion_to_buy_info[53])
PykeToBuy = Champion(*champion_to_buy_info[54])
RakanToBuy = Champion(*champion_to_buy_info[55])
SennaToBuy = Champion(*champion_to_buy_info[56])


if VARIABLE_PRINT_MODE:
    print("champions_to_buy_list = [")
    for champ in champion_to_buy_info:
        print(champ[0] + "ToBuy", end=", ")
    print("]")
    print()


champions_to_buy_list = [
    BrandToBuy,
    FiddlesticksToBuy,
    KalistaToBuy,
    NunuToBuy,
    GarenToBuy,
    GragasToBuy,
    KarmaToBuy,
    KhazixToBuy,
    NidaleeToBuy,
    RivenToBuy,
    SorakaToBuy,
    AsheToBuy,
    GalioToBuy,
    HeimerdingerToBuy,
    SettToBuy,
    UdyrToBuy,
    ZyraToBuy,
    DravenToBuy,
    HecarimToBuy,
    MissFortuneToBuy,
    ThreshToBuy,
    VayneToBuy,
    ViegoToBuy,
    KennenToBuy,
    KledToBuy,
    LuluToBuy,
    PoppyToBuy,
    TeemoToBuy,
    TristanaToBuy,
    ZiggsToBuy,
    GwenToBuy,
    JaxToBuy,
    NautilusToBuy,
    ApheliosToBuy,
    DianaToBuy,
    LeeSinToBuy,
    SejuaniToBuy,
    VladimirToBuy,
    YasuoToBuy,
    AatroxToBuy,
    KayleToBuy,
    LeonaToBuy,
    LuxToBuy,
    RellToBuy,
    SyndraToBuy,
    VarusToBuy,
    VelkozToBuy,
    IvernToBuy,
    NocturneToBuy,
    VolibearToBuy,
    AkshanToBuy,
    IreliaToBuy,
    LucianToBuy,
    OlafToBuy,
    PykeToBuy,
    RakanToBuy,
    SennaToBuy,
]


# GUI


LabelTitle = tk.Label(MainWindow, text="Champion pool", font=BOLDED_FONT)
LabelTitle.grid(row=0, column=SHIFT_BETWEEN_ORIGINS * 5)

LabelTitle = tk.Label(MainWindow, text=origin_list[0])
LabelTitle.grid(row=1, column=ORIGIN_LABEL_POSITION_COLUMN)

LabelTitle = tk.Label(MainWindow, text="Champions to buy", font=BOLDED_FONT)
LabelTitle.grid(row=DOWNSIDE - 1, column=SHIFT_BETWEEN_ORIGINS * 5)

LabelTitle = tk.Label(MainWindow, text="Captured round", font=BOLDED_FONT)
LabelTitle.grid(row=DOWNSIDE - 1, column=SHIFT_BETWEEN_ORIGINS * 9)

CounterOcrResultsRound = tk.IntVar()
CounterOcrResultsRound.set(11)

LabelTitle = tk.Label(MainWindow, textvariable=CounterOcrResultsRound, font=BOLDED_FONT)
LabelTitle.grid(row=DOWNSIDE, column=SHIFT_BETWEEN_ORIGINS * 9)

LabelTitle = tk.Label(MainWindow, text="Captured gold", font=BOLDED_FONT)
LabelTitle.grid(row=DOWNSIDE - 1, column=SHIFT_BETWEEN_ORIGINS * 10)

CounterOcrResultsGold = tk.IntVar()
CounterOcrResultsGold.set(0)

LabelTitle = tk.Label(MainWindow, textvariable=CounterOcrResultsGold, font=BOLDED_FONT)
LabelTitle.grid(row=DOWNSIDE, column=SHIFT_BETWEEN_ORIGINS * 10)

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

if CHAMPIONS_TO_BUY_VISIBLE:
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
    command=lambda: dss.show_nonzero_counters_with_points_from_ocr(
        tk_window=MainWindow,
        origin_champs_counters_=origin_champs_counters,
        origin_champs_counters_to_buy_=origin_champs_counters_to_buy,
        champions_list_=champions_list,
        df_=df,
        index_list=dss.update_champions_to_buy_from_ocr_detection(
            sorted_champions_to_buy_=dss.sorted_champions_to_buy,
            champions_list_for_ocr__=champions_list_for_ocr,
            origin_champs_counters_to_buy_=origin_champs_counters_to_buy,
            reader_=reader,
        )[1],
        origin_list_=origin_list,
        origin_counters_=origin_counters,
        class_list_=class_list,
        class_counters_=class_counters,
    ),
)
ButtonCal.grid(row=DOWNSIDE, column=24)


ButtonCal = tk.Button(
    MainWindow,
    text="scan&go",
    command=lambda: dss.draw_rectangles_show_points_show_buttons_reset_counters(
        rgb_colours_list_=rgb_colours_list,
        sorted_champions_to_buy_=dss.sorted_champions_to_buy,
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
        round_counter=CounterOcrResultsRound,
        gold_counter=CounterOcrResultsGold,
    ),
)
ButtonCal.grid(row=DOWNSIDE, column=30)


ButtonCal = tk.Button(
    MainWindow,
    text="buy xp",
    command=lambda: dss.buy_xp(),
)
ButtonCal.grid(row=DOWNSIDE, column=36)


ButtonCal = tk.Button(
    MainWindow,
    text="refresh",
    command=lambda: [
        dss.refresh(),
        dss.draw_rectangles_show_points_show_buttons_reset_counters(
            rgb_colours_list_=rgb_colours_list,
            sorted_champions_to_buy_=dss.sorted_champions_to_buy,
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
            round_counter=CounterOcrResultsRound,
            gold_counter=CounterOcrResultsGold,
        ),
    ],
)
ButtonCal.grid(row=DOWNSIDE, column=42)

if TEST_BUTTON_VISIBLE:
    ButtonCal = tk.Button(
        MainWindow,
        text="TEST",
        command=lambda: create_new_window(),
    )
    ButtonCal.grid(row=DOWNSIDE, column=48)


def create_new_window():
    """
    Create window with buttons that will let to test DSS functions.

    Returns
    -------
    None.

    """
    logging.debug("Function create_new_window() called")

    new_window = tk.Toplevel()
    new_window.title("Test functions")

    ButtonCal = tk.Button(
        new_window,
        text="update_origins()",
        command=lambda: dss.update_origins(
            origin_list_=origin_list,
            champions_list_=champions_list,
            origin_counters_=origin_counters,
        ),
    )
    ButtonCal.grid(row=1, column=0)

    ButtonCal = tk.Button(
        new_window,
        text="update_classes()",
        command=lambda: dss.update_classes(
            class_list_=class_list,
            champions_list_=champions_list,
            class_counters_=class_counters,
        ),
    )
    ButtonCal.grid(row=2, column=0)

    ButtonCal = tk.Button(
        new_window,
        text="update_classes_and_origins()",
        command=lambda: dss.update_classes_and_origins(
            origin_list_=origin_list,
            champions_list_=champions_list,
            origin_counters_=origin_counters,
            class_list_=class_list,
            class_counters_=class_counters,
        ),
    )
    ButtonCal.grid(row=3, column=0)

    # is_in_game = tk.IntVar()
    # dss.create_gui_counter_with_plus_minus(window_tk=new_window, origin_index=1, counter=is_in_game, shift_between_upside_downside=0)

    ButtonCal = tk.Button(
        new_window,
        text="update_champions_to_buy_from_ocr_detection()",
        command=lambda: dss.update_champions_to_buy_from_ocr_detection(
            sorted_champions_to_buy_=dss.sorted_champions_to_buy,
            champions_list_for_ocr__=champions_list_for_ocr,
            origin_champs_counters_to_buy_=origin_champs_counters_to_buy,
            reader_=reader,
        ),
    )
    ButtonCal.grid(row=4, column=0)

    ButtonCal = tk.Button(
        new_window,
        text="show_nonzero_counters_from_ocr()",
        command=lambda: dss.show_nonzero_counters_from_ocr(
            tk_window=MainWindow,
            origin_champs_counters_=origin_champs_counters,
            origin_champs_counters_to_buy_=origin_champs_counters_to_buy,
            champions_list_=champions_list,
            df_=df,
            index_list=dss.update_champions_to_buy_from_ocr_detection(
                sorted_champions_to_buy_=dss.sorted_champions_to_buy,
                champions_list_for_ocr__=champions_list_for_ocr,
                origin_champs_counters_to_buy_=origin_champs_counters_to_buy,
                reader_=reader,
            )[1],
        ),
    )
    ButtonCal.grid(row=5, column=0)

    Labeling = tk.Label(
        new_window, text="Care additional points in below", font=BOLDED_FONT
    )
    Labeling.grid(row=6, column=0)

    ButtonCal = tk.Button(
        new_window,
        text="show_points_for_nonzero_counters_from_ocr()",
        command=lambda: dss.show_points_for_nonzero_counters_from_ocr(
            tk_window=MainWindow,
            origin_champs_counters_to_buy_=origin_champs_counters_to_buy,
            champions_list_=champions_list,
            df_=df,
            index_list=dss.update_champions_to_buy_from_ocr_detection(
                sorted_champions_to_buy_=dss.sorted_champions_to_buy,
                champions_list_for_ocr__=champions_list_for_ocr,
                origin_champs_counters_to_buy_=origin_champs_counters_to_buy,
                reader_=reader,
            )[1],
        ),
    )
    ButtonCal.grid(row=7, column=0)

    ButtonCal = tk.Button(
        new_window,
        text="show_nonzero_counters_with_points_from_ocr() OCR button",
        command=lambda: dss.show_nonzero_counters_with_points_from_ocr(
            tk_window=MainWindow,
            origin_champs_counters_=origin_champs_counters,
            origin_champs_counters_to_buy_=origin_champs_counters_to_buy,
            champions_list_=champions_list,
            df_=df,
            index_list=dss.update_champions_to_buy_from_ocr_detection(
                sorted_champions_to_buy_=dss.sorted_champions_to_buy,
                champions_list_for_ocr__=champions_list_for_ocr,
                origin_champs_counters_to_buy_=origin_champs_counters_to_buy,
                reader_=reader,
            )[1],
            origin_list_=origin_list,
            origin_counters_=origin_counters,
            class_list_=class_list,
            class_counters_=class_counters,
        ),
    )
    ButtonCal.grid(row=8, column=0)

    Labeling = tk.Label(new_window, text="with Game", font=BOLDED_FONT)
    Labeling.grid(row=0, column=1)

    ButtonCal = tk.Button(
        new_window, text="update_curent_ss()", command=lambda: dss.update_curent_ss()
    )
    ButtonCal.grid(row=1, column=1)

    ButtonCal = tk.Button(
        new_window,
        text="update_curent_cropped_ss_with_champions()",
        command=lambda: dss.update_curent_cropped_ss_with_champions(),
    )
    ButtonCal.grid(row=2, column=1)

    ButtonCal = tk.Button(
        new_window,
        text="update_ocr_results_champions()",
        command=lambda: dss.update_ocr_results_champions(
            cropped_ss_with_champion_card_names=dss.crop_img,
            reader_=reader,
        ),
    )
    ButtonCal.grid(row=3, column=1)

    ButtonCal = tk.Button(
        new_window,
        text="update_sorted_champions_to_buy()",
        command=lambda: dss.update_sorted_champions_to_buy(
            ocr_results_sorted=dss.ocr_results_champions,
            champions_list_for_ocr_=champions_list_for_ocr,
        ),
    )
    ButtonCal.grid(row=4, column=1)

    ButtonCal = tk.Button(
        new_window,
        text="update_champions_to_buy_from_ocr_detection()",
        command=lambda: dss.update_champions_to_buy_from_ocr_detection(
            sorted_champions_to_buy_=dss.sorted_champions_to_buy,
            champions_list_for_ocr__=champions_list_for_ocr,
            origin_champs_counters_to_buy_=origin_champs_counters_to_buy,
            reader_=reader,
        ),
    )
    ButtonCal.grid(row=5, column=1)

    ButtonCal = tk.Button(
        new_window,
        text="draw_rectangles_show_points_show_buttons_reset_counters() scan&go",
        command=lambda: dss.draw_rectangles_show_points_show_buttons_reset_counters(
            rgb_colours_list_=rgb_colours_list,
            sorted_champions_to_buy_=dss.sorted_champions_to_buy,
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
            round_counter=CounterOcrResultsRound,
            gold_counter=CounterOcrResultsGold,
        ),
    )
    ButtonCal.grid(row=6, column=1)

    ButtonCal = tk.Button(
        new_window,
        text="filling_list_with_counter_for_namedtuple(4)",
        command=lambda: dss.filling_list_with_counter_for_namedtuple(
            field_to_check=4,
            input_list=champion_info,
            origin_list_=origin_list,
            class_list_=class_list,
            origin_counters_=origin_counters,
            class_counters_=class_counters,
            df_=df,
        ),
    )
    ButtonCal.grid(row=0, column=2)

    ButtonCal = tk.Button(
        new_window,
        text="filling_list_with_counter_for_namedtuple(5)",
        command=lambda: dss.filling_list_with_counter_for_namedtuple(
            field_to_check=5,
            input_list=champion_info,
            origin_list_=origin_list,
            class_list_=class_list,
            origin_counters_=origin_counters,
            class_counters_=class_counters,
            df_=df,
        ),
    )
    ButtonCal.grid(row=1, column=2)

    ButtonCal = tk.Button(
        new_window,
        text="filling_list_with_counter_for_namedtuple(6)",
        command=lambda: dss.filling_list_with_counter_for_namedtuple(
            field_to_check=6,
            input_list=champion_info,
            origin_list_=origin_list,
            class_list_=class_list,
            origin_counters_=origin_counters,
            class_counters_=class_counters,
            df_=df,
        ),
    )
    ButtonCal.grid(row=2, column=2)

    ButtonCal = tk.Button(
        new_window,
        text="filling_list_with_counter_for_namedtuple(7)",
        command=lambda: dss.filling_list_with_counter_for_namedtuple(
            field_to_check=7,
            input_list=champion_info,
            origin_list_=origin_list,
            class_list_=class_list,
            origin_counters_=origin_counters,
            class_counters_=class_counters,
            df_=df,
        ),
    )
    ButtonCal.grid(row=3, column=2)

    ButtonCal = tk.Button(
        new_window,
        text="append_counters_to_input_list(champion_info)",
        command=lambda: dss.append_counters_to_input_list(
            input_list=champion_info,
            origin_list_=origin_list,
            class_list_=class_list,
            origin_counters_=origin_counters,
            class_counters_=class_counters,
            df_=df,
        ),
    )
    ButtonCal.grid(row=4, column=2)

    ButtonCal = tk.Button(
        new_window,
        text="append_counters_to_input_list(champion_to_buy_info)",
        command=lambda: dss.append_counters_to_input_list(
            input_list=champion_to_buy_info,
            origin_list_=origin_list,
            class_list_=class_list,
            origin_counters_=origin_counters,
            class_counters_=class_counters,
            df_=df,
        ),
    )
    ButtonCal.grid(row=5, column=2)

    ButtonCal = tk.Button(
        new_window,
        text="calculate_card_position_on_screen(2)",
        command=lambda: dss.calculate_card_position_on_screen(
            card_index=2,
            X_FIRST_CHAMPION_CARD_=dss.X_FIRST_CHAMPION_CARD,
            PADDING_BETWEEN_CHAMPION_CARDS_=dss.PADDING_BETWEEN_CHAMPION_CARDS,
            W_CHAMPION_CARD_=dss.W_CHAMPION_CARD,
        ),
    )
    ButtonCal.grid(row=0, column=3)

    ButtonCal = tk.Button(
        new_window,
        text="build_list_of_champion_cards_rectangles()",
        command=lambda: dss.build_list_of_champion_cards_rectangles(
            CARDS_TO_BUY_AMOUNT_=dss.CARDS_TO_BUY_AMOUNT,
            Y_FIRST_CHAMPION_CARD_=dss.Y_FIRST_CHAMPION_CARD,
            W_CHAMPION_CARD_=dss.W_CHAMPION_CARD,
            H_CHAMPION_CARD_=dss.H_CHAMPION_CARD,
        ),
    )
    ButtonCal.grid(row=1, column=3)

    Labeling = tk.Label(
        new_window, text="Another cases below this row", font=BOLDED_FONT
    )
    Labeling.grid(row=9, column=0)

    ButtonCal = tk.Button(
        new_window,
        text="check_nonzero_counters()",
        command=lambda: dss.check_nonzero_counters(
            origin_champs_counters_to_buy_=origin_champs_counters_to_buy,
            champions_list_=champions_list,
        ),
    )
    ButtonCal.grid(row=10, column=0)

    ButtonCal = tk.Button(
        new_window,
        text="show_nonzero_counters()",
        command=lambda: dss.show_nonzero_counters(
            tk_window=MainWindow,
            origin_champs_counters_=origin_champs_counters,
            origin_champs_counters_to_buy_=origin_champs_counters_to_buy,
            champions_list_=champions_list,
            df_=df,
            row_offset=0,
            CARDS_TO_BUY_AMOUNT_=dss.CARDS_TO_BUY_AMOUNT,
            SHIFT_BETWEEN_ORIGINS_=dss.SHIFT_BETWEEN_ORIGINS,
        ),
    )
    ButtonCal.grid(row=11, column=0)

    ButtonCal = tk.Button(
        new_window,
        text="update_classes_and_origins()",
        command=lambda: dss.update_classes_and_origins(
            origin_list_=origin_list,
            champions_list_=champions_list,
            origin_counters_=origin_counters,
            class_list_=class_list,
            class_counters_=class_counters,
        ),
    )
    ButtonCal.grid(row=12, column=0)

    ButtonCal = tk.Button(
        new_window,
        text="show_points_for_nonzero_counters()",
        command=lambda: dss.show_points_for_nonzero_counters(
            tk_window=MainWindow,
            origin_champs_counters_to_buy_=origin_champs_counters_to_buy,
            champions_list_=champions_list,
            df_=df,
            row_offset=2,
            show_mode=1,
            CARDS_TO_BUY_AMOUNT_=dss.CARDS_TO_BUY_AMOUNT,
            SHIFT_BETWEEN_ORIGINS_=dss.SHIFT_BETWEEN_ORIGINS,
        ),
    )
    ButtonCal.grid(row=13, column=0)

    ButtonCal = tk.Button(
        new_window,
        text="show_nonzero_counters_with_points()",
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
    ButtonCal.grid(row=14, column=0)

    ButtonCal = tk.Button(
        new_window,
        text="reset_counters_in_list()",
        command=lambda: dss.reset_counters_in_list(
            origin_champs_counters_to_buy_=origin_champs_counters_to_buy
        ),
    )
    ButtonCal.grid(row=10, column=1)

    ButtonCal = tk.Button(
        new_window,
        text="update_champions_to_buy_from_ocr_detection()",
        command=lambda: dss.update_champions_to_buy_from_ocr_detection(
            sorted_champions_to_buy_=dss.sorted_champions_to_buy,
            champions_list_for_ocr__=champions_list_for_ocr,
            origin_champs_counters_to_buy_=origin_champs_counters_to_buy,
            reader_=reader,
        ),
    )
    ButtonCal.grid(row=11, column=1)

    ButtonCal = tk.Button(
        new_window,
        text="show_nonzero_counters_with_points_from_ocr()",
        command=lambda: dss.show_nonzero_counters_with_points_from_ocr(
            tk_window=MainWindow,
            origin_champs_counters_=origin_champs_counters,
            origin_champs_counters_to_buy_=origin_champs_counters_to_buy,
            champions_list_=champions_list,
            df_=df,
            index_list=dss.update_champions_to_buy_from_ocr_detection(
                sorted_champions_to_buy_=dss.sorted_champions_to_buy,
                champions_list_for_ocr__=champions_list_for_ocr,
                origin_champs_counters_to_buy_=origin_champs_counters_to_buy,
                reader_=reader,
            )[1],
            origin_list_=origin_list,
            origin_counters_=origin_counters,
            class_list_=class_list,
            class_counters_=class_counters,
        ),
    )
    ButtonCal.grid(row=12, column=1)

    ButtonCal = tk.Button(
        new_window,
        text="build_list_of_champion_cards_rectangles()",
        command=lambda: dss.build_list_of_champion_cards_rectangles(
            CARDS_TO_BUY_AMOUNT_=dss.CARDS_TO_BUY_AMOUNT,
            Y_FIRST_CHAMPION_CARD_=dss.Y_FIRST_CHAMPION_CARD,
            W_CHAMPION_CARD_=dss.W_CHAMPION_CARD,
            H_CHAMPION_CARD_=dss.H_CHAMPION_CARD,
        ),
    )
    ButtonCal.grid(row=13, column=1)

    ButtonCal = tk.Button(
        new_window,
        text="draw_rectangles_show_points_show_buttons_reset_counters() scan&go",
        command=lambda: dss.draw_rectangles_show_points_show_buttons_reset_counters(
            rgb_colours_list_=rgb_colours_list,
            sorted_champions_to_buy_=dss.sorted_champions_to_buy,
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
            round_counter=CounterOcrResultsRound,
            gold_counter=CounterOcrResultsGold,
        ),
    )
    ButtonCal.grid(row=14, column=1)

    ButtonCal = tk.Button(
        new_window, text="update_curent_ss()", command=lambda: dss.update_curent_ss()
    )
    ButtonCal.grid(row=10, column=2)

    ButtonCal = tk.Button(
        new_window,
        text="update_curent_cropped_ss_with_rounds()",
        command=lambda: dss.update_curent_cropped_ss_with_rounds(),
    )
    ButtonCal.grid(row=11, column=2)

    ButtonCal = tk.Button(
        new_window,
        text="update_ocr_results_round()",
        command=lambda: dss.update_ocr_results_round(
            reader_=reader, round_counter=CounterOcrResultsRound
        ),
    )
    ButtonCal.grid(row=12, column=2)

    ButtonCal = tk.Button(
        new_window,
        text="full_state_update_champions_ocr()",
        command=lambda: dss.full_state_update_rounds_ocr(
            reader_=reader, round_counter=CounterOcrResultsRound
        ),
    )
    ButtonCal.grid(row=13, column=2)

    ButtonCal = tk.Button(
        new_window, text="update_curent_ss()", command=lambda: dss.update_curent_ss()
    )
    ButtonCal.grid(row=10, column=3)

    ButtonCal = tk.Button(
        new_window,
        text="update_curent_cropped_ss_with_gold()",
        command=lambda: dss.update_curent_cropped_ss_with_gold(),
    )
    ButtonCal.grid(row=11, column=3)

    ButtonCal = tk.Button(
        new_window,
        text="update_ocr_results_gold()",
        command=lambda: dss.update_ocr_results_gold(
            reader_=reader,
            gold_counter=CounterOcrResultsGold,
        ),
    )
    ButtonCal.grid(row=12, column=3)

    ButtonCal = tk.Button(
        new_window,
        text="full_state_update_gold_ocr()",
        command=lambda: dss.full_state_update_gold_ocr(
            reader_=reader,
            gold_counter=CounterOcrResultsGold,
        ),
    )
    ButtonCal.grid(row=13, column=3)

    logging.debug("Function create_new_window() end")


MainWindow.attributes("-alpha", 0.9)
MainWindow.mainloop()
