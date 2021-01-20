# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 10:54:45 2020

@author: Janusz
"""

import logging
import tkinter as tk
import tkinter.font as tkFont
from collections import namedtuple

from cv2 import cv2 as cv
import easyocr
import pandas as pd

from windowcapture import WindowCapture

# REMEMBER TO SET GAME TO WINDOW MODE!!!!!!!!!!!!!!!!!!!!
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

logging.basicConfig(level=logging.DEBUG)

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


CARDS_TO_BUY_AMOUNT = 5

VARIABLE_PRINT_MODE = 0
# VARIABLE_PRINT_MODE = 1

# IMAGE_DEBUG_MODE = 0
IMAGE_DEBUG_MODE = 1

reader = easyocr.Reader(["en"])


# IF U WANT TEST WITHOUT GAME THEN COMMENT HERE
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


wincap = WindowCapture("League of Legends (TM) Client")
LOAD_IMAGE = 0

# wincap = None
# LOAD_IMAGE = 1


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


# drawing rectangles things
# First champion card to buy on screen

X_FIRST_CHAMPION_CARD = 505
W_CHAMPION_CARD = 175
Y_FIRST_CHAMPION_CARD = 865
H_CHAMPION_CARD = 135

PADDING_BETWEEN_CHAMPION_CARDS = 14

# drawing rectangles

line_color = (255, 0, 255)
LINE_TYPE = cv.LINE_4
marker_color = (255, 0, 255)
MARKER_TYPE = cv.MARKER_CROSS


rgb_colours_list = [
    (255, 0, 255),
    (0, 255, 255),
    (0, 255, 255),
    (0, 255, 255),
    (0, 255, 0),
]

# rgb_colours_list = ["worst", "medium3", "medium2", "medium1", "best"]

# worst magenta mediums in yellow and best in green

# rgb_colours_list=range(0,5)
# next card, indexing from 0 = most left side


# WINDOW THINGS


MainWindow = tk.Tk()
MainWindow.geometry("1900x800+0+0")
MainWindow.title("TFTDSS")


BOLDED_FONT = tkFont.Font(family="Arial", size=10, weight=tkFont.BOLD)

SHIFT_BETWEEN_ORIGINS = 6

ORIGIN_LABEL_POSITION_COLUMN = 1


UPSIDE = 0  # champion pool
DOWNSIDE = 16  # champions to buy


df = pd.read_csv("scaledChampionsdf.csv")

df.drop("Unnamed: 0", axis=1, inplace=True)
df.Points = df["Points"].round(3)

# order as in GUI
df.sort_values(by=["OriginPrimary", "Champion"], inplace=True)
df.reset_index(drop=True, inplace=True)


origin_list = list(set(df.OriginPrimary)) + list(set(df.OriginSecondary))
origin_list = list(set(origin_list))
origin_list.remove("None")
origin_list.sort()

if VARIABLE_PRINT_MODE:
    for origin in origin_list:
        print(
            origin.lower()
            + "_champs = list(df.query("
            + "'OriginPrimary == "
            + '"'
            + "%s" % origin
            + '"'
            + "').Champion)"
        )

if VARIABLE_PRINT_MODE:
    print("origin_champs_from_df_list = [", end=" ")
    for origin in origin_list:
        print(origin.lower() + "_champs", end=", ")
    print("]")

cultist_champs = list(df.query('OriginPrimary == "Cultist"').Champion)
divine_champs = list(df.query('OriginPrimary == "Divine"').Champion)
dusk_champs = list(df.query('OriginPrimary == "Dusk"').Champion)
elderwood_champs = list(df.query('OriginPrimary == "Elderwood"').Champion)
enlightened_champs = list(df.query('OriginPrimary == "Enlightened"').Champion)
exile_champs = list(df.query('OriginPrimary == "Exile"').Champion)
fortune_champs = list(df.query('OriginPrimary == "Fortune"').Champion)
moonlight_champs = list(df.query('OriginPrimary == "Moonlight"').Champion)
ninja_champs = list(df.query('OriginPrimary == "Ninja"').Champion)
spirit_champs = list(df.query('OriginPrimary == "Spirit"').Champion)
the_boss_champs = list(df.query('OriginPrimary == "TheBoss"').Champion)
tormented_champs = list(df.query('OriginPrimary == "Tormented"').Champion)
warlord_champs = list(df.query('OriginPrimary == "Warlord"').Champion)

origin_champs_from_df_list = [
    cultist_champs,
    divine_champs,
    dusk_champs,
    elderwood_champs,
    enlightened_champs,
    exile_champs,
    fortune_champs,
    moonlight_champs,
    ninja_champs,
    spirit_champs,
    the_boss_champs,
    tormented_champs,
    warlord_champs,
]


class_list = list(set(df.ClassPrimary)) + list(set(df.ClassSecondary))
class_list = list(set(class_list))
class_list.remove("None")
class_list.sort()


# OCR things

if VARIABLE_PRINT_MODE:
    print("champions_list_for_ocr = [", end=" ")
    for champ in df.Champion:
        print("'" + champ + "'", end=", ")
    print("]")


champions_list_for_ocr = [
    "Aatrox",
    "Elise",
    "Evelynn",
    "Jhin",
    "Kalista",
    "Pyke",
    "Twisted Fate",
    "Zilean",
    "Jax",
    "Lee Sin",
    "Lux",
    "Warwick",
    "Wukong",
    "Cassiopeia",
    "Lillia",
    "Riven",
    "Thresh",
    "Vayne",
    "Ashe",
    "Ezreal",
    "Hecarim",
    "Lulu",
    "Maokai",
    "Nunu & Willump",
    "Veigar",
    "Fiora",
    "Irelia",
    "Janna",
    "Morgana",
    "Nami",
    "Talon",
    "Yasuo",
    "Yone",
    "Annie",
    "Jinx",
    "Sejuani",
    "Tahm Kench",
    "Aphelios",
    "Diana",
    "Lissandra",
    "Sylas",
    "Akali",
    "Kennen",
    "Shen",
    "Zed",
    "Ahri",
    "Kindred",
    "Teemo",
    "Yuumi",
    "Sett",
    "Kayn",
    "Azir",
    "Garen",
    "Jarvan IV",
    "Katarina",
    "Nidalee",
    "Vi",
    "Xin Zhao",
]


# COUNTERS FOR CHAMPIONS IN POOL

if VARIABLE_PRINT_MODE:
    for champ in df.Champion:
        print("Counter" + champ + " = tk.IntVar()")


CounterAatrox = tk.IntVar()
CounterElise = tk.IntVar()
CounterEvelynn = tk.IntVar()
CounterJhin = tk.IntVar()
CounterKalista = tk.IntVar()
CounterPyke = tk.IntVar()
CounterTwistedFate = tk.IntVar()
CounterZilean = tk.IntVar()
CounterJax = tk.IntVar()
CounterLeeSin = tk.IntVar()
CounterLux = tk.IntVar()
CounterWarwick = tk.IntVar()
CounterWukong = tk.IntVar()
CounterCassiopeia = tk.IntVar()
CounterLillia = tk.IntVar()
CounterRiven = tk.IntVar()
CounterThresh = tk.IntVar()
CounterVayne = tk.IntVar()
CounterAshe = tk.IntVar()
CounterEzreal = tk.IntVar()
CounterHecarim = tk.IntVar()
CounterLulu = tk.IntVar()
CounterMaokai = tk.IntVar()
CounterNunu = tk.IntVar()
CounterVeigar = tk.IntVar()
CounterFiora = tk.IntVar()
CounterIrelia = tk.IntVar()
CounterJanna = tk.IntVar()
CounterMorgana = tk.IntVar()
CounterNami = tk.IntVar()
CounterTalon = tk.IntVar()
CounterYasuo = tk.IntVar()
CounterYone = tk.IntVar()
CounterAnnie = tk.IntVar()
CounterJinx = tk.IntVar()
CounterSejuani = tk.IntVar()
CounterTahmKench = tk.IntVar()
CounterAphelios = tk.IntVar()
CounterDiana = tk.IntVar()
CounterLissandra = tk.IntVar()
CounterSylas = tk.IntVar()
CounterAkali = tk.IntVar()
CounterKennen = tk.IntVar()
CounterShen = tk.IntVar()
CounterZed = tk.IntVar()
CounterAhri = tk.IntVar()
CounterKindred = tk.IntVar()
CounterTeemo = tk.IntVar()
CounterYuumi = tk.IntVar()
CounterSett = tk.IntVar()
CounterKayn = tk.IntVar()
CounterAzir = tk.IntVar()
CounterGaren = tk.IntVar()
CounterJarvanIV = tk.IntVar()
CounterKatarina = tk.IntVar()
CounterNidalee = tk.IntVar()
CounterVi = tk.IntVar()
CounterXinZhao = tk.IntVar()

if VARIABLE_PRINT_MODE:
    print("origin_champs_counters = [")
    for champ in df.Champion:
        print("Counter" + champ, end=", ")
    print("]")
    print()

origin_champs_counters = [
    CounterAatrox,
    CounterElise,
    CounterEvelynn,
    CounterJhin,
    CounterKalista,
    CounterPyke,
    CounterTwistedFate,
    CounterZilean,
    CounterJax,
    CounterLeeSin,
    CounterLux,
    CounterWarwick,
    CounterWukong,
    CounterCassiopeia,
    CounterLillia,
    CounterRiven,
    CounterThresh,
    CounterVayne,
    CounterAshe,
    CounterEzreal,
    CounterHecarim,
    CounterLulu,
    CounterMaokai,
    CounterNunu,
    CounterVeigar,
    CounterFiora,
    CounterIrelia,
    CounterJanna,
    CounterMorgana,
    CounterNami,
    CounterTalon,
    CounterYasuo,
    CounterYone,
    CounterAnnie,
    CounterJinx,
    CounterSejuani,
    CounterTahmKench,
    CounterAphelios,
    CounterDiana,
    CounterLissandra,
    CounterSylas,
    CounterAkali,
    CounterKennen,
    CounterShen,
    CounterZed,
    CounterAhri,
    CounterKindred,
    CounterTeemo,
    CounterYuumi,
    CounterSett,
    CounterKayn,
    CounterAzir,
    CounterGaren,
    CounterJarvanIV,
    CounterKatarina,
    CounterNidalee,
    CounterVi,
    CounterXinZhao,
]

# COUNTERS for champions to buy

if VARIABLE_PRINT_MODE:
    for champ in df.Champion:
        print("CounterBuy" + champ + " = tk.IntVar()")


CounterBuyAatrox = tk.IntVar()
CounterBuyElise = tk.IntVar()
CounterBuyEvelynn = tk.IntVar()
CounterBuyJhin = tk.IntVar()
CounterBuyKalista = tk.IntVar()
CounterBuyPyke = tk.IntVar()
CounterBuyTwistedFate = tk.IntVar()
CounterBuyZilean = tk.IntVar()
CounterBuyJax = tk.IntVar()
CounterBuyLeeSin = tk.IntVar()
CounterBuyLux = tk.IntVar()
CounterBuyWarwick = tk.IntVar()
CounterBuyWukong = tk.IntVar()
CounterBuyCassiopeia = tk.IntVar()
CounterBuyLillia = tk.IntVar()
CounterBuyRiven = tk.IntVar()
CounterBuyThresh = tk.IntVar()
CounterBuyVayne = tk.IntVar()
CounterBuyAshe = tk.IntVar()
CounterBuyEzreal = tk.IntVar()
CounterBuyHecarim = tk.IntVar()
CounterBuyLulu = tk.IntVar()
CounterBuyMaokai = tk.IntVar()
CounterBuyNunu = tk.IntVar()
CounterBuyVeigar = tk.IntVar()
CounterBuyFiora = tk.IntVar()
CounterBuyIrelia = tk.IntVar()
CounterBuyJanna = tk.IntVar()
CounterBuyMorgana = tk.IntVar()
CounterBuyNami = tk.IntVar()
CounterBuyTalon = tk.IntVar()
CounterBuyYasuo = tk.IntVar()
CounterBuyYone = tk.IntVar()
CounterBuyAnnie = tk.IntVar()
CounterBuyJinx = tk.IntVar()
CounterBuySejuani = tk.IntVar()
CounterBuyTahmKench = tk.IntVar()
CounterBuyAphelios = tk.IntVar()
CounterBuyDiana = tk.IntVar()
CounterBuyLissandra = tk.IntVar()
CounterBuySylas = tk.IntVar()
CounterBuyAkali = tk.IntVar()
CounterBuyKennen = tk.IntVar()
CounterBuyShen = tk.IntVar()
CounterBuyZed = tk.IntVar()
CounterBuyAhri = tk.IntVar()
CounterBuyKindred = tk.IntVar()
CounterBuyTeemo = tk.IntVar()
CounterBuyYuumi = tk.IntVar()
CounterBuySett = tk.IntVar()
CounterBuyKayn = tk.IntVar()
CounterBuyAzir = tk.IntVar()
CounterBuyGaren = tk.IntVar()
CounterBuyJarvanIV = tk.IntVar()
CounterBuyKatarina = tk.IntVar()
CounterBuyNidalee = tk.IntVar()
CounterBuyVi = tk.IntVar()
CounterBuyXinZhao = tk.IntVar()


if VARIABLE_PRINT_MODE:
    print("origin_champs_counters_to_buy = [")
    for champ in df.Champion:
        print("CounterBuy" + champ, end=", ")
    print("]")
    print()

origin_champs_counters_to_buy = [
    CounterBuyAatrox,
    CounterBuyElise,
    CounterBuyEvelynn,
    CounterBuyJhin,
    CounterBuyKalista,
    CounterBuyPyke,
    CounterBuyTwistedFate,
    CounterBuyZilean,
    CounterBuyJax,
    CounterBuyLeeSin,
    CounterBuyLux,
    CounterBuyWarwick,
    CounterBuyWukong,
    CounterBuyCassiopeia,
    CounterBuyLillia,
    CounterBuyRiven,
    CounterBuyThresh,
    CounterBuyVayne,
    CounterBuyAshe,
    CounterBuyEzreal,
    CounterBuyHecarim,
    CounterBuyLulu,
    CounterBuyMaokai,
    CounterBuyNunu,
    CounterBuyVeigar,
    CounterBuyFiora,
    CounterBuyIrelia,
    CounterBuyJanna,
    CounterBuyMorgana,
    CounterBuyNami,
    CounterBuyTalon,
    CounterBuyYasuo,
    CounterBuyYone,
    CounterBuyAnnie,
    CounterBuyJinx,
    CounterBuySejuani,
    CounterBuyTahmKench,
    CounterBuyAphelios,
    CounterBuyDiana,
    CounterBuyLissandra,
    CounterBuySylas,
    CounterBuyAkali,
    CounterBuyKennen,
    CounterBuyShen,
    CounterBuyZed,
    CounterBuyAhri,
    CounterBuyKindred,
    CounterBuyTeemo,
    CounterBuyYuumi,
    CounterBuySett,
    CounterBuyKayn,
    CounterBuyAzir,
    CounterBuyGaren,
    CounterBuyJarvanIV,
    CounterBuyKatarina,
    CounterBuyNidalee,
    CounterBuyVi,
    CounterBuyXinZhao,
]

# counters for origins

if VARIABLE_PRINT_MODE:
    for origin in origin_list:
        print("Counter" + origin + " = tk.IntVar()")


CounterCultist = tk.IntVar()
CounterDivine = tk.IntVar()
CounterDusk = tk.IntVar()
CounterElderwood = tk.IntVar()
CounterEnlightened = tk.IntVar()
CounterExile = tk.IntVar()
CounterFortune = tk.IntVar()
CounterMoonlight = tk.IntVar()
CounterNinja = tk.IntVar()
CounterSpirit = tk.IntVar()
CounterTheBoss = tk.IntVar()
CounterTormented = tk.IntVar()
CounterWarlord = tk.IntVar()


if VARIABLE_PRINT_MODE:
    print("origin_counters = [")
    for origin in origin_list:
        print("Counter" + origin, end=", ")
    print("]")


origin_counters = [
    CounterCultist,
    CounterDivine,
    CounterDusk,
    CounterElderwood,
    CounterEnlightened,
    CounterExile,
    CounterFortune,
    CounterMoonlight,
    CounterNinja,
    CounterSpirit,
    CounterTheBoss,
    CounterTormented,
    CounterWarlord,
]

# counters for classes


if VARIABLE_PRINT_MODE:
    for clas in class_list:
        print("Counter" + clas + " = tk.IntVar()")


CounterAdept = tk.IntVar()
CounterAssassin = tk.IntVar()
CounterBrawler = tk.IntVar()
CounterDazzler = tk.IntVar()
CounterDuelist = tk.IntVar()
CounterEmperor = tk.IntVar()
CounterHunter = tk.IntVar()
CounterKeeper = tk.IntVar()
CounterMage = tk.IntVar()
CounterMystic = tk.IntVar()
CounterShade = tk.IntVar()
CounterSharpshooter = tk.IntVar()
CounterVanguard = tk.IntVar()


if VARIABLE_PRINT_MODE:
    print("class_counters = [")
    for clas in class_list:
        print("Counter" + clas, end=", ")
    print("]")

class_counters = [
    CounterAdept,
    CounterAssassin,
    CounterBrawler,
    CounterDazzler,
    CounterDuelist,
    CounterEmperor,
    CounterHunter,
    CounterKeeper,
    CounterMage,
    CounterMystic,
    CounterShade,
    CounterSharpshooter,
    CounterVanguard,
]


# Champion namedtuple things


champion_info = []
logging.debug("Filling champion_info in purpose of creating namedtuple")
for i, champ in enumerate(df.Champion):
    champion_info.append(
        [
            champ,
            champions_list_for_ocr[i],
            i,
            origin_champs_counters[i],
            df.OriginPrimary[i],
            df.OriginSecondary[i],
            df.ClassPrimary[i],
            df.ClassSecondary[i],
        ]
    )
logging.debug("First filling champion_info has ended.")


champion_to_buy_info = []
logging.debug("Filling champion_to_buy_info in purpose of creating namedtuple")
for i, champ in enumerate(df.Champion):
    champion_to_buy_info.append(
        [
            champ,
            champions_list_for_ocr[i],
            i,
            origin_champs_counters_to_buy[i],
            df.OriginPrimary[i],
            df.OriginSecondary[i],
            df.ClassPrimary[i],
            df.ClassSecondary[i],
        ]
    )
logging.debug("First filling champion_to_buy_info has ended.")


def filling_list_with_counter_for_namedtuple(field_to_check, input_list):
    """


    Parameters
    ----------
    field_to_check : {4:"origin_prim", 5:"origin_sec", 6:"class_prim",
                           7:"class_sec"}
    input_list : List with 4,5,6,7 field == field_to_check. The default is champion_info.

    Returns
    -------
    list_of_counters : List of GUI counters

    """
    logging.debug("Function filling_list_with_counter_for_namedtuple() called")
    field_to_check_2_string = {
        4: "origin_prim",
        5: "origin_sec",
        6: "class_prim",
        7: "class_sec",
    }
    field_to_check_2_check_list = {
        4: origin_list,
        5: origin_list,
        6: class_list,
        7: class_list,
    }
    field_to_check_2_check_list_string = {
        4: "origin_list",
        5: "origin_list",
        6: "class_list",
        7: "class_list",
    }
    field_to_check_2_counters_list = {
        4: origin_counters,
        5: origin_counters,
        6: class_counters,
        7: class_counters,
    }
    list_of_counters = [None] * len(df.Champion)
    for i, champ in enumerate(df.Champion):
        if input_list[i][field_to_check] == "None":
            logging.info("Champion name: %s, champion index = %d", champ, i)
            logging.info(
                "Field with index %d == 'NONE' filling None as %sCounter",
                field_to_check,
                field_to_check_2_string[field_to_check],
            )
            list_of_counters[i] = None
        else:
            logging.info("%s IS NOT 'NONE'", field_to_check_2_string[field_to_check])
            for j, class_or_origin in enumerate(
                field_to_check_2_check_list[field_to_check]
            ):
                if input_list[i][field_to_check] == class_or_origin:
                    logging.info("Champion name: %s, champion index = %d", champ, i)
                    logging.info(
                        "Found match in champion %s and %s for : %s",
                        field_to_check_2_string[field_to_check],
                        field_to_check_2_check_list_string[field_to_check],
                        class_or_origin,
                    )
                    logging.info(
                        "Filling %s counter: %s",
                        field_to_check_2_string[field_to_check],
                        field_to_check_2_counters_list[field_to_check][j],
                    )
                    list_of_counters[i] = field_to_check_2_counters_list[
                        field_to_check
                    ][j]
    logging.debug("Function filling_list_with_counter_for_namedtuple() end")
    return list_of_counters


def append_counters_to_input_list(input_list):
    """


    Parameters
    ----------
    input_list : Appending counters to list with fields like {4:"origin_prim",
    5:"origin_sec", 6:"class_prim", 7:"class_sec"}.

    Returns
    -------
    None.

    """

    logging.debug("Function filling_list_with_counter_for_namedtuple() called")

    counters_to_append = [4, 5, 6, 7]
    for j in counters_to_append:
        list_of_counters_to_append = filling_list_with_counter_for_namedtuple(
            j, input_list
        )
        for i, champ in enumerate(input_list):
            champ.append(list_of_counters_to_append[i])

    logging.debug("Function filling_list_with_counter_for_namedtuple() end")


append_counters_to_input_list(champion_info)

append_counters_to_input_list(champion_to_buy_info)

champion_info_df = pd.DataFrame.from_records(
    champion_info,
    columns=[
        "Champion",
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
        "Champion",
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
Evelynn = Champion(*champion_info[2])
Jhin = Champion(*champion_info[3])
Kalista = Champion(*champion_info[4])
Pyke = Champion(*champion_info[5])
TwistedFate = Champion(*champion_info[6])
Zilean = Champion(*champion_info[7])
Jax = Champion(*champion_info[8])
LeeSin = Champion(*champion_info[9])
Lux = Champion(*champion_info[10])
Warwick = Champion(*champion_info[11])
Wukong = Champion(*champion_info[12])
Cassiopeia = Champion(*champion_info[13])
Lillia = Champion(*champion_info[14])
Riven = Champion(*champion_info[15])
Thresh = Champion(*champion_info[16])
Vayne = Champion(*champion_info[17])
Ashe = Champion(*champion_info[18])
Ezreal = Champion(*champion_info[19])
Hecarim = Champion(*champion_info[20])
Lulu = Champion(*champion_info[21])
Maokai = Champion(*champion_info[22])
Nunu = Champion(*champion_info[23])
Veigar = Champion(*champion_info[24])
Fiora = Champion(*champion_info[25])
Irelia = Champion(*champion_info[26])
Janna = Champion(*champion_info[27])
Morgana = Champion(*champion_info[28])
Nami = Champion(*champion_info[29])
Talon = Champion(*champion_info[30])
Yasuo = Champion(*champion_info[31])
Yone = Champion(*champion_info[32])
Annie = Champion(*champion_info[33])
Jinx = Champion(*champion_info[34])
Sejuani = Champion(*champion_info[35])
TahmKench = Champion(*champion_info[36])
Aphelios = Champion(*champion_info[37])
Diana = Champion(*champion_info[38])
Lissandra = Champion(*champion_info[39])
Sylas = Champion(*champion_info[40])
Akali = Champion(*champion_info[41])
Kennen = Champion(*champion_info[42])
Shen = Champion(*champion_info[43])
Zed = Champion(*champion_info[44])
Ahri = Champion(*champion_info[45])
Kindred = Champion(*champion_info[46])
Teemo = Champion(*champion_info[47])
Yuumi = Champion(*champion_info[48])
Sett = Champion(*champion_info[49])
Kayn = Champion(*champion_info[50])
Azir = Champion(*champion_info[51])
Garen = Champion(*champion_info[52])
JarvanIV = Champion(*champion_info[53])
Katarina = Champion(*champion_info[54])
Nidalee = Champion(*champion_info[55])
Vi = Champion(*champion_info[56])
XinZhao = Champion(*champion_info[57])


if VARIABLE_PRINT_MODE:
    print("champions_list = [")
    for champ in champion_info:
        print(champ[0], end=", ")
    print("]")
    print()


champions_list = [
    Aatrox,
    Elise,
    Evelynn,
    Jhin,
    Kalista,
    Pyke,
    TwistedFate,
    Zilean,
    Jax,
    LeeSin,
    Lux,
    Warwick,
    Wukong,
    Cassiopeia,
    Lillia,
    Riven,
    Thresh,
    Vayne,
    Ashe,
    Ezreal,
    Hecarim,
    Lulu,
    Maokai,
    Nunu,
    Veigar,
    Fiora,
    Irelia,
    Janna,
    Morgana,
    Nami,
    Talon,
    Yasuo,
    Yone,
    Annie,
    Jinx,
    Sejuani,
    TahmKench,
    Aphelios,
    Diana,
    Lissandra,
    Sylas,
    Akali,
    Kennen,
    Shen,
    Zed,
    Ahri,
    Kindred,
    Teemo,
    Yuumi,
    Sett,
    Kayn,
    Azir,
    Garen,
    JarvanIV,
    Katarina,
    Nidalee,
    Vi,
    XinZhao,
]


if VARIABLE_PRINT_MODE:
    for i, champ in enumerate(champion_to_buy_info):
        print(champ[0] + "ToBuy" + " = Champion(*champion_to_buy_info[{}])".format(i))

AatroxToBuy = Champion(*champion_to_buy_info[0])
EliseToBuy = Champion(*champion_to_buy_info[1])
EvelynnToBuy = Champion(*champion_to_buy_info[2])
JhinToBuy = Champion(*champion_to_buy_info[3])
KalistaToBuy = Champion(*champion_to_buy_info[4])
PykeToBuy = Champion(*champion_to_buy_info[5])
TwistedFateToBuy = Champion(*champion_to_buy_info[6])
ZileanToBuy = Champion(*champion_to_buy_info[7])
JaxToBuy = Champion(*champion_to_buy_info[8])
LeeSinToBuy = Champion(*champion_to_buy_info[9])
LuxToBuy = Champion(*champion_to_buy_info[10])
WarwickToBuy = Champion(*champion_to_buy_info[11])
WukongToBuy = Champion(*champion_to_buy_info[12])
CassiopeiaToBuy = Champion(*champion_to_buy_info[13])
LilliaToBuy = Champion(*champion_to_buy_info[14])
RivenToBuy = Champion(*champion_to_buy_info[15])
ThreshToBuy = Champion(*champion_to_buy_info[16])
VayneToBuy = Champion(*champion_to_buy_info[17])
AsheToBuy = Champion(*champion_to_buy_info[18])
EzrealToBuy = Champion(*champion_to_buy_info[19])
HecarimToBuy = Champion(*champion_to_buy_info[20])
LuluToBuy = Champion(*champion_to_buy_info[21])
MaokaiToBuy = Champion(*champion_to_buy_info[22])
NunuToBuy = Champion(*champion_to_buy_info[23])
VeigarToBuy = Champion(*champion_to_buy_info[24])
FioraToBuy = Champion(*champion_to_buy_info[25])
IreliaToBuy = Champion(*champion_to_buy_info[26])
JannaToBuy = Champion(*champion_to_buy_info[27])
MorganaToBuy = Champion(*champion_to_buy_info[28])
NamiToBuy = Champion(*champion_to_buy_info[29])
TalonToBuy = Champion(*champion_to_buy_info[30])
YasuoToBuy = Champion(*champion_to_buy_info[31])
YoneToBuy = Champion(*champion_to_buy_info[32])
AnnieToBuy = Champion(*champion_to_buy_info[33])
JinxToBuy = Champion(*champion_to_buy_info[34])
SejuaniToBuy = Champion(*champion_to_buy_info[35])
TahmKenchToBuy = Champion(*champion_to_buy_info[36])
ApheliosToBuy = Champion(*champion_to_buy_info[37])
DianaToBuy = Champion(*champion_to_buy_info[38])
LissandraToBuy = Champion(*champion_to_buy_info[39])
SylasToBuy = Champion(*champion_to_buy_info[40])
AkaliToBuy = Champion(*champion_to_buy_info[41])
KennenToBuy = Champion(*champion_to_buy_info[42])
ShenToBuy = Champion(*champion_to_buy_info[43])
ZedToBuy = Champion(*champion_to_buy_info[44])
AhriToBuy = Champion(*champion_to_buy_info[45])
KindredToBuy = Champion(*champion_to_buy_info[46])
TeemoToBuy = Champion(*champion_to_buy_info[47])
YuumiToBuy = Champion(*champion_to_buy_info[48])
SettToBuy = Champion(*champion_to_buy_info[49])
KaynToBuy = Champion(*champion_to_buy_info[50])
AzirToBuy = Champion(*champion_to_buy_info[51])
GarenToBuy = Champion(*champion_to_buy_info[52])
JarvanIVToBuy = Champion(*champion_to_buy_info[53])
KatarinaToBuy = Champion(*champion_to_buy_info[54])
NidaleeToBuy = Champion(*champion_to_buy_info[55])
ViToBuy = Champion(*champion_to_buy_info[56])
XinZhaoToBuy = Champion(*champion_to_buy_info[57])


if VARIABLE_PRINT_MODE:
    print("champions_to_buy_list = [")
    for champ in champion_to_buy_info:
        print(champ[0] + "ToBuy", end=", ")
    print("]")
    print()


champions_to_buy_list = [
    AatroxToBuy,
    EliseToBuy,
    EvelynnToBuy,
    JhinToBuy,
    KalistaToBuy,
    PykeToBuy,
    TwistedFateToBuy,
    ZileanToBuy,
    JaxToBuy,
    LeeSinToBuy,
    LuxToBuy,
    WarwickToBuy,
    WukongToBuy,
    CassiopeiaToBuy,
    LilliaToBuy,
    RivenToBuy,
    ThreshToBuy,
    VayneToBuy,
    AsheToBuy,
    EzrealToBuy,
    HecarimToBuy,
    LuluToBuy,
    MaokaiToBuy,
    NunuToBuy,
    VeigarToBuy,
    FioraToBuy,
    IreliaToBuy,
    JannaToBuy,
    MorganaToBuy,
    NamiToBuy,
    TalonToBuy,
    YasuoToBuy,
    YoneToBuy,
    AnnieToBuy,
    JinxToBuy,
    SejuaniToBuy,
    TahmKenchToBuy,
    ApheliosToBuy,
    DianaToBuy,
    LissandraToBuy,
    SylasToBuy,
    AkaliToBuy,
    KennenToBuy,
    ShenToBuy,
    ZedToBuy,
    AhriToBuy,
    KindredToBuy,
    TeemoToBuy,
    YuumiToBuy,
    SettToBuy,
    KaynToBuy,
    AzirToBuy,
    GarenToBuy,
    JarvanIVToBuy,
    KatarinaToBuy,
    NidaleeToBuy,
    ViToBuy,
    XinZhaoToBuy,
]


# FUNCTIONS


def add(counter):
    """Adding one to counter"""
    logging.debug("Function add() called")

    logging.info("input = %d", counter.get())
    counter.set(counter.get() + 1)

    logging.info("after call = %d", counter.get())
    logging.debug("Function add() end")


def sub(counter):
    """Minus one to counter"""
    logging.debug("Function sub() called")

    logging.info("input = %d", counter.get())
    if counter.get() > 0:
        counter.set(counter.get() - 1)

    logging.info("after call = %d", counter.get())
    logging.debug("Function sub() end")


def sort_detected_champions_to_buy_by_position(ocr_results_sorted):
    """

    Sorting input in order from left to right by placement on the screen
    (lowest width is first).Then filters out champion names, numbers(champions cost)
    are discarded.

    Parameters
    ----------
    ocr_results_sorted : Typical == ocr_on_cropped_img(make_cropped_ss())

    Returns
    -------
    sorted_champions_to_buy : List of champions that were found in input.

    """

    logging.debug("Function sort_detected_champions_to_buy_by_position() called")
    # sort from lowest width (left to right side)
    ocr_results_sorted = sorted(ocr_results_sorted, key=lambda x: x[0])
    sorted_champions_to_buy = []
    for text in ocr_results_sorted:
        for champ in champions_list_for_ocr:
            if champ in text:  # filters champion names
                sorted_champions_to_buy.append(champ)
                logging.info(
                    "from for loop in sort_detected_champions_to_buy_by_position()"
                )
                logging.info("found %s", champ)
    logging.info("return in sort_detected_champions_to_buy_by_position()")
    logging.info("List of sorted champions to buy: %s", sorted_champions_to_buy)

    logging.debug("Function sort_detected_champions_to_buy_by_position() end")
    return sorted_champions_to_buy


def make_cropped_ss(
    load_image=LOAD_IMAGE,
    window=wincap,
    cropping_x=450,
    cropping_y=970,
    cropping_width=1000,
    cropping_height=30,
):
    """


    Parameters
    ----------
    LOAD_IMAGE : If want to open without game then change to 1.
        The default is 0.
    window : Window to be captured, set to None if want to open without game.
        The default is wincap.

        Defaults to cropp screenshot from first to fifth(1-5) champion card name.
    cropping_x :  The default is 450.
    cropping_y :  The default is 970.
    cropping_width :  The default is 1000.
    cropping_height :  The default is 30.

    Returns
    -------
    crop_img : Cropped screenshot.

    """
    logging.debug("Function make_cropped_ss() called")

    if load_image:
        screenshot = cv.imread("ss.jpg", cv.IMREAD_UNCHANGED)
    else:
        screenshot = window.get_screenshot()
    crop_img = screenshot[
        cropping_y : cropping_y + cropping_height,
        cropping_x : cropping_x + cropping_width,
    ]

    if IMAGE_DEBUG_MODE:
        cv.imshow("make_cropped_ss()", crop_img)

    logging.debug("Function make_cropped_ss() end")
    return crop_img, screenshot


def ocr_on_cropped_img(cropped_ss_with_champion_card_names):
    """


    Parameters
    ----------
    cropped_ss_with_champion_card_names : for example if want to OCR card names then
    input there make_cropped_ss(LOAD_IMAGE=0, window=wincap, cropping_x=450,
                                cropping_y=970, cropping_width=1000, cropping_height=30)

    Returns
    -------
    ocr_result :

    """
    logging.debug("Function ocr_on_cropped_img() called")

    ocr_result = reader.readtext(cropped_ss_with_champion_card_names)
    logging.info("OCR results(return): %s", ocr_result)

    logging.debug("Function ocr_on_cropped_img() end")
    return ocr_result


def update_champions_to_buy_from_ocr_detection():
    """
    Add 1 to every champion to buy counter detected in ocr_result.
    champion to buy counters GLOBAL STATE CHANGE !!!!!!!!!!!!!!!!!!!!

    Returns
    -------
    None.

    """
    logging.debug("Function update_champions_to_buy_from_ocr_detection() called")

    list_of_champs_to_buy_this_turn = sort_detected_champions_to_buy_by_position(
        ocr_on_cropped_img(make_cropped_ss()[0])
    )
    for champ_to_buy in list_of_champs_to_buy_this_turn:
        for i, champ in enumerate(champions_list_for_ocr):
            if champ_to_buy == champ:
                logging.info(
                    "IF inside for loop in update_champions_to_buy_from_ocr_detection()"
                )
                logging.info("Index in champions_list_for_ocr that is detected: %d", i)
                logging.info("Champ name in this index: %s", champ)
                add(origin_champs_counters_to_buy[i])
                break

    logging.debug("Function update_champions_to_buy_from_ocr_detection() end")
    return list_of_champs_to_buy_this_turn


def calculate_card_position_on_screen(card_index):
    """


    Parameters
    ----------
    card_index : simply from 0-4(first to fifth card)

    Returns
    -------
    x_card : x Position on the screen of the top left corner for card

    """
    logging.debug("Function calculate_card_position_on_screen() called")

    x_card = (
        X_FIRST_CHAMPION_CARD
        + PADDING_BETWEEN_CHAMPION_CARDS * card_index
        + W_CHAMPION_CARD * card_index
    )
    logging.info("X coord of card with index= %d is: %s", card_index, x_card)
    logging.debug("Function calculate_card_position_on_screen() end")
    return x_card


def build_list_of_champion_cards_rectangles():
    """
    This function building list of card rectangles position on screen.

    Returns
    -------
    cards_rectangles : list of card rectangles position on screen

    """
    logging.debug("Function build_list_of_champion_cards_rectangles() called")

    cards_rectangles = [0] * CARDS_TO_BUY_AMOUNT
    for i in range(0, CARDS_TO_BUY_AMOUNT):
        top_left = (calculate_card_position_on_screen(i), Y_FIRST_CHAMPION_CARD)
        bottom_right = (
            calculate_card_position_on_screen(i) + W_CHAMPION_CARD,
            Y_FIRST_CHAMPION_CARD + H_CHAMPION_CARD,
        )
        center = (
            top_left[0] + W_CHAMPION_CARD // 2,
            top_left[1] + H_CHAMPION_CARD // 2,
        )
        # print("Type" ,type(center))
        cards_rectangles[i] = [top_left, bottom_right, center]

    logging.debug("Function build_list_of_champion_cards_rectangles() end")
    return cards_rectangles


# https://stackoverflow.com/questions/6618515/sorting-list-based-on-values-from-another-list
def draw_on_champion_to_buy_cards(colors=rgb_colours_list, mode="points"):
    """
    This function is making OCR detection on champion cards, and then draws by
    input mode like default points on screenshot.

    Parameters
    ----------
    colors : ["worst", "medium3", "medium2", "medium1", "best"]. list of RGB tuples.
    The default is rgb_colours_list.
    mode :  The default is "points". Also there are cross and rectangle.

    Returns
    -------
    None.

    """
    logging.debug("Function draw_on_champion_to_buy_cards() called")

    champions_to_buy_in_order_as_in_screen = (
        update_champions_to_buy_from_ocr_detection()
    )
    champions_to_buy_points_and_position = show_nonzero_counters_with_points()

    champions_position_to_buy_ordered_by_screen = [
        champions_list_for_ocr.index(i) for i in champions_to_buy_in_order_as_in_screen
    ]
    logging.info(
        "champions_position_to_buy_ordered_by_screen: %s",
        champions_position_to_buy_ordered_by_screen,
    )

    champions_to_buy_points = list(zip(*champions_to_buy_points_and_position))[0]
    champions_to_buy_position = list(zip(*champions_to_buy_points_and_position))[1]
    logging.info(
        "Points (in alphabetical by champ name order?): %s", champions_to_buy_points
    )
    logging.info(
        "Champions position (in alphabetical by champ name order?): %s",
        champions_to_buy_position,
    )
    sorted_champions_to_buy_points_and_position = sorted(
        champions_to_buy_points_and_position
    )
    logging.info(
        "Points and Champions position (in alphabetical by champ name order?): %s",
        sorted_champions_to_buy_points_and_position,
    )
    sorted_champions_to_buy_position = list(
        zip(*sorted_champions_to_buy_points_and_position)
    )[1]
    logging.info(
        "sorted_champions_to_buy_position in alphabetical order?: %s",
        sorted_champions_to_buy_position,
    )
    values_by_points_indexes_order_by_position_on_screen = [
        sorted_champions_to_buy_position.index(i)
        for i in champions_position_to_buy_ordered_by_screen
    ]
    logging.info(
        "values_by_points_indexes_order_by_position_on_screen 0 worst 4 best card: %s",
        values_by_points_indexes_order_by_position_on_screen,
    )
    cards_rectangles = build_list_of_champion_cards_rectangles()
    screenshot = wincap.get_screenshot()
    # screenshot = cv.imread("ss.jpg",cv.IMREAD_UNCHANGED)

    # at the end
    # values_by_points_indexes_order_by_position_on_screen contains champions
    # sorted by points from lowest(0) to highest(4)
    # and indexes represents champion placement on the screen

    if mode == "rectangle":
        for i in range(0, CARDS_TO_BUY_AMOUNT):
            cv.rectangle(
                screenshot,
                cards_rectangles[i][0],
                cards_rectangles[i][1],
                color=colors[values_by_points_indexes_order_by_position_on_screen[i]],
                lineType=LINE_TYPE,
                thickness=2,
            )
        cv.imshow("draw_on_champion_to_buy_cards()", screenshot)
    elif mode == "cross":
        for i in range(0, CARDS_TO_BUY_AMOUNT):
            # Draw the center point
            cv.drawMarker(
                screenshot,
                cards_rectangles[i][2],
                color=colors[values_by_points_indexes_order_by_position_on_screen[i]],
                markerType=MARKER_TYPE,
                markerSize=40,
                thickness=2,
            )
        cv.imshow("draw_on_champion_to_buy_cards()", screenshot)
    elif mode == "points":
        for i in range(0, CARDS_TO_BUY_AMOUNT):
            # Draw the center point
            cv.putText(
                screenshot,
                "{:.3f}".format(
                    sorted_champions_to_buy_points_and_position[
                        values_by_points_indexes_order_by_position_on_screen[i]
                    ][0]
                ),
                cards_rectangles[i][2],
                cv.FONT_HERSHEY_SIMPLEX,
                0.6,
                colors[values_by_points_indexes_order_by_position_on_screen[i]],
                2,
            )
        cv.imshow("draw_on_champion_to_buy_cards()", screenshot)

    logging.debug("Function draw_on_champion_to_buy_cards() end")


# need to fix double calculate points inside draw_on_champion_to_buy_cards
def draw_rectangles_show_points_show_buttons_reset_counters():
    """
    Draws rectangles then show points with buttons and reset counters.

    Returns
    -------
    None.

    """
    logging.debug(
        "Function draw_rectangles_show_points_show_buttons_reset_counters() called"
    )

    update_classes_and_origins()
    reset_counters_in_list(origin_champs_counters_to_buy)
    draw_on_champion_to_buy_cards()

    logging.debug(
        "Function draw_rectangles_show_points_show_buttons_reset_counters() end"
    )


def show_champions_from_origin(
    origin_position_in_origin_list,
    origin_champs_from_df,
    champs_list,
    shift_between_upside_downside,
):
    """Adding buttons and text labels for single origin.
    In: origin_position_in_origin_list - its used to pickup origin from origin_list,
    and place text on the window.
    origin_champs_from_df  - list of champions in origin.
    champs_list - list of champions namedtuples.
    shift_between_upside_downside - placing on the window, UPSIDE is upper location,
    DOWNSIDE is lower location.

    """
    logging.debug("Function show_champions_from_origin() called")

    tk.Label(MainWindow, text=origin_list[origin_position_in_origin_list]).grid(
        row=1 + shift_between_upside_downside,
        column=ORIGIN_LABEL_POSITION_COLUMN
        * SHIFT_BETWEEN_ORIGINS
        * origin_position_in_origin_list,
    )

    for i, champ_name in enumerate(origin_champs_from_df):
        tk.Label(MainWindow, text=champ_name).grid(
            row=2 + i + shift_between_upside_downside,
            column=ORIGIN_LABEL_POSITION_COLUMN
            * SHIFT_BETWEEN_ORIGINS
            * origin_position_in_origin_list,
        )
        for champ in champs_list:
            if champ.name == champ_name:
                tk.Entry(MainWindow, textvariable=champ.ChampCounter, width=2).grid(
                    row=2 + i + shift_between_upside_downside,
                    column=SHIFT_BETWEEN_ORIGINS * origin_position_in_origin_list + 1,
                )
                tk.Button(
                    MainWindow,
                    text="+",
                    command=lambda counter=champ.ChampCounter: add(counter),
                ).grid(
                    row=2 + i + shift_between_upside_downside,
                    column=SHIFT_BETWEEN_ORIGINS * origin_position_in_origin_list + 2,
                )
                tk.Button(
                    MainWindow,
                    text="-",
                    command=lambda counter=champ.ChampCounter: sub(counter),
                ).grid(
                    row=2 + i + shift_between_upside_downside,
                    column=SHIFT_BETWEEN_ORIGINS * origin_position_in_origin_list + 3,
                )
                break
    logging.debug("Function show_champions_from_origin() end")


def show_classes_or_origins(
    origin_position_in_origin_list,
    origin_or_class_list,
    origin_or_class_counter_list,
    shift_between_upside_downside,
    origin_or_class_string,
):
    """Adding buttons and text labels for single origin.
    In: origin_position_in_origin_list - its used to pickup origin from origin_list,
    and place text on the window.
    origin_or_class_list  - list of origin or class names.
    origin_or_class_counter_list - list counters for origin or class.
    shift_between_upside_downside - placing on the window, UPSIDE is upper location,
    DOWNSIDE is lower location.
    origin_or_class_string - Title above counters
    """
    logging.debug("Function show_classes_or_origins() called")

    tk.Label(MainWindow, text=origin_or_class_string).grid(
        row=1 + shift_between_upside_downside,
        column=ORIGIN_LABEL_POSITION_COLUMN
        * SHIFT_BETWEEN_ORIGINS
        * origin_position_in_origin_list,
    )

    for i, champ in enumerate(origin_or_class_list):
        tk.Label(MainWindow, text=champ).grid(
            row=2 + i + shift_between_upside_downside,
            column=ORIGIN_LABEL_POSITION_COLUMN
            * SHIFT_BETWEEN_ORIGINS
            * origin_position_in_origin_list,
        )
        tk.Entry(
            MainWindow, textvariable=origin_or_class_counter_list[i], width=2
        ).grid(
            row=2 + i + shift_between_upside_downside,
            column=SHIFT_BETWEEN_ORIGINS * origin_position_in_origin_list + 1,
        )
        tk.Button(
            MainWindow,
            text="+",
            command=lambda counter=origin_or_class_counter_list[i]: add(counter),
        ).grid(
            row=2 + i + shift_between_upside_downside,
            column=SHIFT_BETWEEN_ORIGINS * origin_position_in_origin_list + 2,
        )
        tk.Button(
            MainWindow,
            text="-",
            command=lambda counter=origin_or_class_counter_list[i]: sub(counter),
        ).grid(
            row=2 + i + shift_between_upside_downside,
            column=SHIFT_BETWEEN_ORIGINS * origin_position_in_origin_list + 3,
        )

    logging.debug("Function show_classes_or_origins() end")


def reset_counters_in_list(list1d=origin_champs_counters_to_buy):
    """Reset counters to 0, used when roll or new round starts.
    In: list1d by default its origin_champs_counters_to_buy."""
    logging.debug("Function reset_counters_in_list() called")

    for champ_counter in list1d:
        champ_counter.set(0)

    delete_all_buttons()

    logging.debug("Function reset_counters_in_list() end")


def check_nonzero_counters(list1d=origin_champs_counters_to_buy):
    """Check how much champion counters are nonzero.
    IF ladder to append repetitions to list.
    In: list1d by default its origin_champs_counters_to_buy.
    Out: position of counters in champions list that are nonzero"""
    logging.debug("Function check_nonzero_counters() called")

    nonzero_counters_list = []
    nonzero_counters_number_list = []
    for i, champ_counter in enumerate(list1d):
        if champ_counter.get() >= 1:
            nonzero_counters_list.append(champ_counter)
            nonzero_counters_number_list.append(i)
            if champ_counter.get() >= 2:
                nonzero_counters_list.append(champ_counter)
                nonzero_counters_number_list.append(i)
                if champ_counter.get() >= 3:
                    nonzero_counters_list.append(champ_counter)
                    nonzero_counters_number_list.append(i)
                    if champ_counter.get() >= 4:
                        nonzero_counters_list.append(champ_counter)
                        nonzero_counters_number_list.append(i)
    logging.info("Nonzero counters list human readable: ")
    for champ_index in nonzero_counters_number_list:
        logging.info("%s", champions_list[champ_index].name)
    logging.info("Nonzero counters indexes(return): %s", nonzero_counters_number_list)
    logging.info("This is nonzero Counter list: %s", nonzero_counters_list)

    logging.debug("Function check_nonzero_counters() end")
    return nonzero_counters_number_list


def show_nonzero_counters(row_offset=0):
    """It shows up champions to buy that counters are nonzero, as a button.
    Created button will add one to champion pool counter, delete itself from window
    and sub one from counters champions that can be bought.
    In: row_offset by default = 0 for buttons row placement."""
    logging.debug("Function show_nonzero_counters() called")

    global button_calc_list
    button_calc_list = [0] * CARDS_TO_BUY_AMOUNT
    champion_position_in_list_ordered_by_origin = check_nonzero_counters()
    for i in range(0, len(champion_position_in_list_ordered_by_origin), 1):
        button_calc_list[i] = tk.Button(
            MainWindow,
            text=(df.Champion[champion_position_in_list_ordered_by_origin[i]]),
            command=lambda i=i: [
                add(
                    origin_champs_counters[
                        champion_position_in_list_ordered_by_origin[i]
                    ]
                ),
                delete_button(i),
                sub(
                    origin_champs_counters_to_buy[
                        champion_position_in_list_ordered_by_origin[i]
                    ]
                ),
            ],
        )
        button_calc_list[i].grid(
            row=12 + row_offset, column=SHIFT_BETWEEN_ORIGINS * (i + 1)
        )

    logging.debug("Function show_nonzero_counters() end")


def show_points_for_nonzero_counters(row_offset=2, show_mode=1):
    """It shows up champions POINTS to buy that counters are nonzero, as a text.
    Doesnt disappear currently, should be fixed.
    In: row_offset by default = 0 for buttons row placement."""
    logging.debug("Function show_points_for_nonzero_counters() called")

    global text_label_list
    points_for_champion_to_buy = [0] * CARDS_TO_BUY_AMOUNT
    text_label_list = [0] * CARDS_TO_BUY_AMOUNT
    champion_position_in_list_ordered_by_origin = check_nonzero_counters()
    for i in range(0, len(champion_position_in_list_ordered_by_origin), 1):
        points_for_champion_to_buy[i] = (
            df.Points[champion_position_in_list_ordered_by_origin[i]]
            + additional_points_from_origin_combo(
                champion_position_in_list_ordered_by_origin[i]
            )
            + additional_points_from_class_combo(
                champion_position_in_list_ordered_by_origin[i]
            )
            + additional_points_from_champions_in_pool(
                champion_position_in_list_ordered_by_origin[i]
            )
        )
        points_for_champion_to_buy[i] = round(points_for_champion_to_buy[i], 3)
        if show_mode:
            text_label_list[i] = tk.Label(
                MainWindow, text=points_for_champion_to_buy[i]
            )
            text_label_list[i].grid(
                row=12 + row_offset, column=SHIFT_BETWEEN_ORIGINS * (i + 1)
            )
    logging.info(
        "Points and champion_position_in_list_ordered_by_origin: %s",
        list(
            zip(
                points_for_champion_to_buy,
                champion_position_in_list_ordered_by_origin,
            )
        ),
    )

    human_readable_champions = []
    logging.info("Should be empty list: %s", human_readable_champions)
    for champ_index in champion_position_in_list_ordered_by_origin:
        human_readable_champions.append(champions_list[champ_index].name)
    logging.info(
        "Should be filled with nonzero champions to buy: %s", human_readable_champions
    )

    logging.info(
        "Champions availbable to buy with calculated points list readable: %s",
        list(zip(points_for_champion_to_buy, human_readable_champions)),
    )

    logging.debug("Function show_points_for_nonzero_counters() end")
    return list(
        zip(points_for_champion_to_buy, champion_position_in_list_ordered_by_origin)
    )


def show_nonzero_counters_with_points(row_offset_buttons=0, row_offset_points=2):
    """First updates classes and origins to get points updated, then shows
    champions to buy as a buttons and their points as a text.
    In: row_offset_buttons by default 0 for buttons.
    row_offset_points by default 2 for points as a text."""
    logging.debug("Function show_nonzero_counters_with_points() called")

    update_classes_and_origins()
    show_nonzero_counters(row_offset_buttons)
    points_with_position_zip = show_points_for_nonzero_counters(row_offset_points)

    logging.debug("Function show_nonzero_counters_with_points() end")
    return points_with_position_zip


def update_origins():
    """Checks nonzero counters for champions in pool and updates origins by
    setting origin counters."""
    logging.debug("Function update_origins() called")

    origin_counters_value_list = [0] * len(origin_list)
    for i, origin_ in enumerate(origin_list):  # looping over counters for every origin
        logging.info("Current origin: %s", origin_)
        for (
            champ
        ) in (
            champions_list
        ):  # for loop to assign how much champions are nonzero in origin
            if champ.ChampCounter.get() >= 1:
                logging.info("Current champ with counter >=1: %s", champ.name)
                if origin_ in (champ.origin_prim, champ.origin_sec):
                    logging.info(
                        "Current champ with counter >=1 match origin Prim or Sec \
                                 : %s or %s",
                        champ.origin_prim,
                        champ.origin_sec,
                    )
                    origin_counters_value_list[i] = origin_counters_value_list[i] + 1
        logging.info(
            "Number of nonzero champions in this origin: %s",
            origin_counters_value_list[i],
        )
        origin_counters[i].set(origin_counters_value_list[i])

    logging.debug("Function update_origins() end")


def update_classes():
    """Checks nonzero counters for champions in pool and updates classes by
    setting class counters."""
    logging.debug("Function update_classes() called")

    class_counters_value_list = [0] * len(class_list)
    for i, class_ in enumerate(class_list):  # looping over counters for every class
        logging.info("Current class: %s", class_)
        for (
            champ
        ) in (
            champions_list
        ):  # for loop to assign how much champions are nonzero in class
            if champ.ChampCounter.get() >= 1:
                logging.info("Current champ with counter >=1: %s", champ.name)
                if class_ in (champ.class_prim, champ.class_sec):
                    logging.info(
                        "Current champ with counter >=1 match class Prim or Sec \
                                 : %s or %s",
                        champ.class_prim,
                        champ.class_sec,
                    )
                    class_counters_value_list[i] = class_counters_value_list[i] + 1
        logging.info(
            "Number of nonzero champions in this class = %s",
            class_counters_value_list[i],
        )
        class_counters[i].set(class_counters_value_list[i])

    logging.debug("Function update_classes() end")


def update_classes_and_origins():
    """Checks nonzero counters for champions in pool and updates classes and origins."""
    logging.debug("Function update_classes_and_origins() called")

    update_origins()
    update_classes()

    logging.debug("Function update_classes_and_origins() end")


def additional_points_from_origin_combo(champion_position):
    """Part of sum points, bonus from origin for specific champion.
    In: champion_position its just position of champion in list by primal
    champions to buy list.
    Out: Bonus points from origin."""
    logging.debug("Function additional_points_from_origin_combo() called")

    logging.info(
        "Calculating origin points for champ named: %s",
        champions_list[champion_position].name,
    )
    bonus_points_from_origin = 0.2
    total_count = champions_list[champion_position].OriginPrimCounter.get()
    logging.info("Origin primary counter = %d", total_count)
    if champions_list[champion_position].origin_sec != "None":
        total_count = (
            champions_list[champion_position].OriginSecCounter.get() + total_count
        )
        logging.info("Origin primary + secondary counter = %f", total_count)

    origin_bonus = total_count * bonus_points_from_origin
    logging.info("Bonus(return) = %f", origin_bonus)
    logging.debug("Function additional_points_from_origin_combo() end")
    return origin_bonus


def additional_points_from_class_combo(champion_position):
    """Part of sum points, bonus from class for specific champion.
    In: champion_position its just position of champion in list by primal
    champions to buy list.
    Out: Bonus points from class."""
    logging.debug("Function additional_points_from_class_combo() called")

    logging.info(
        "Calculating class points for champ named: %s ",
        champions_list[champion_position].name,
    )
    bonus_points_from_class = 0.2
    total_count = champions_list[champion_position].ClassPrimCounter.get()
    if champions_list[champion_position].class_sec != "None":
        total_count = (
            champions_list[champion_position].ClassSecCounter.get() + total_count
        )
        logging.info("Class primary + secondary counter = %f", total_count)

    class_bonus = total_count * bonus_points_from_class
    logging.info("Bonus(return) = %f", class_bonus)
    logging.debug("Function additional_points_from_class_combo() end")
    return class_bonus


def additional_points_from_champions_in_pool(champion_position):
    """Part of sum points, bonus from champion in pool.
    In: champion_position its just position of champion in list by primal
    champions to buy list.
    Out: Bonus points from champions that are already in pool."""
    logging.debug("Function additional_points_from_champions_in_pool() called")

    champion_pool_bonus = (
        champions_list[champion_position].ChampCounter.get() - 1
    ) * 0.2
    logging.info(
        "champion_pool_bonus = %f for champ named: %s ",
        champion_pool_bonus,
        champions_list[champion_position].name,
    )

    logging.debug("Function additional_points_from_champions_in_pool() end")
    return champion_pool_bonus


def delete_button(position):
    """Deleting buttons"""
    logging.debug("Function delete_button() called")

    button_calc_list[position].destroy()

    logging.debug("Function delete_button() end")


def delete_all_buttons():
    """
    Deleting all buttons.

    Returns
    -------
    None.

    """
    logging.debug("Function delete_all_buttons() called")
    try:
        for button in button_calc_list:
            if button != 0:
                button.destroy()
    except NameError:
        print("There are no buttons to destroy.")

    logging.debug("Function delete_all_buttons() end")


# GUI


LabelTitle = tk.Label(MainWindow, text="Champion pool", font=BOLDED_FONT)
LabelTitle.grid(row=0, column=SHIFT_BETWEEN_ORIGINS * 5)

LabelTitle = tk.Label(MainWindow, text=origin_list[0])
LabelTitle.grid(row=1, column=ORIGIN_LABEL_POSITION_COLUMN)

LabelTitle = tk.Label(MainWindow, text="Champions to buy", font=BOLDED_FONT)
LabelTitle.grid(row=DOWNSIDE - 1, column=SHIFT_BETWEEN_ORIGINS * 5)

# CHAMPIONS
for i in range(0, len(origin_champs_from_df_list), 1):
    show_champions_from_origin(i, origin_champs_from_df_list[i], champions_list, UPSIDE)

for i in range(0, len(origin_champs_from_df_list), 1):
    show_champions_from_origin(
        i, origin_champs_from_df_list[i], champions_to_buy_list, DOWNSIDE
    )

# ORIGINS
show_classes_or_origins(
    len(origin_champs_from_df_list), origin_list, origin_counters, UPSIDE, "Origins"
)

# CLASSES
show_classes_or_origins(
    (len(origin_champs_from_df_list) + 1), class_list, class_counters, UPSIDE, "Classes"
)
Labeling = tk.Label(MainWindow, text="Left to buy", font=BOLDED_FONT)
Labeling.grid(row=12 + 0, column=0)

Labeling = tk.Label(MainWindow, text="Points", font=BOLDED_FONT)
Labeling.grid(row=14 + 0, column=0)

ButtonCal = tk.Button(
    MainWindow,
    text="reset",
    command=lambda: reset_counters_in_list(origin_champs_counters_to_buy),
)
ButtonCal.grid(row=DOWNSIDE, column=6)

ButtonCal = tk.Button(
    MainWindow, text="update classes", command=lambda: update_classes_and_origins()
)
ButtonCal.grid(row=DOWNSIDE, column=12)

ButtonCal = tk.Button(
    MainWindow, text="show points", command=lambda: show_nonzero_counters_with_points()
)
ButtonCal.grid(row=DOWNSIDE, column=18)

ButtonCal = tk.Button(
    MainWindow, text="OCR", command=lambda: update_champions_to_buy_from_ocr_detection()
)
ButtonCal.grid(row=DOWNSIDE, column=24)

ButtonCal = tk.Button(
    MainWindow, text="draw rectangles", command=lambda: draw_on_champion_to_buy_cards()
)
ButtonCal.grid(row=DOWNSIDE, column=30)

ButtonCal = tk.Button(
    MainWindow,
    text="scan&go",
    command=lambda: draw_rectangles_show_points_show_buttons_reset_counters(),
)
ButtonCal.grid(row=DOWNSIDE, column=36)

MainWindow.attributes("-alpha", 0.9)
MainWindow.mainloop()
