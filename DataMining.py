# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 11:39:13 2020

@author: Janusz
https://stackoverflow.com/questions/43441269/finding-an-element-within-an-element-using-selenium-webdriver
.// search only in parent element
// search whole document
"""

import logging
import time
from collections import namedtuple

import pandas as pd
from selenium import webdriver

logging.basicConfig(level=logging.INFO)
driver = webdriver.Opera()
driver.get("https://tftactics.gg/db/champion-stats")
driver.maximize_window()
time.sleep(3)
accept_all_cookies_button = driver.find_element_by_xpath(
    '//a[@class="cmpboxbtn cmpboxbtnyes"]'
)
accept_all_cookies_button.click()
time.sleep(1)

sort_by_champion_button = driver.find_element_by_xpath(
    '//div[@class="rt-th -cursor-pointer"]'
)
sort_by_champion_button.click()


champion_web_elements_by_tiers_list = []
tiers = range(1, 5, 1)
for t in tiers:
    champion_web_elements_by_tiers_list.append(
        driver.find_elements_by_xpath('//a[@class="characters-item c%d"]' % t)
    )

champion_row_list = driver.find_elements_by_xpath('//div[@class="rt-tr-group"]')


champion_names = driver.find_elements_by_css_selector("a")

first_champion_index_in_a_selector = 0
last_champion_index_in_a_selector = 0
for i in range(0, len(champion_names), 1):
    if champion_names[i].text == "Aatrox":  ############ First champion sorted by name
        first_champion_index_in_a_selector = i
        logging.info(
            "Found first champion index in 'a' selector: %d",
            first_champion_index_in_a_selector,
        )
    if champion_names[i].text == "Zilean":  ############ Last champion sorted by name
        last_champion_index_in_a_selector = (
            i + 1
        )  ####  +1 because for loop stops at i +1
        logging.info(
            "Found last champion index in 'a' selector: %d",
            last_champion_index_in_a_selector,
        )
        break

found_champions = last_champion_index_in_a_selector - first_champion_index_in_a_selector
logging.info("Number of found champions: %d", found_champions)

champions_list = []
for i in range(
    first_champion_index_in_a_selector, last_champion_index_in_a_selector, 1
):
    logging.info(
        "Appending champion name: %s with index in 'a' css selector %d",
        champion_names[i].text,
        i,
    )
    champions_list.append(champion_names[i].text)


def find(s, ch):
    """
    https://stackoverflow.com/questions/11122291/how-to-find-char-in-string-and-get-all-the-indexes

    Parameters
    ----------
    s : string.
    ch : character to be found in string.

    Returns
    -------
    list
        DESCRIPTION.

    """
    logging.info(
        "find(s = %s, ch = %s) found character in string on indexes: %s",
        s,
        ch,
        [i for i, ltr in enumerate(s) if ltr == ch],
    )
    return [i for i, ltr in enumerate(s) if ltr == ch]


def stats_gathering(to_fill_list):
    champion_row_list = driver.find_elements_by_xpath('//div[@class="rt-tr-group"]')

    for i in range(0, len(champions_list), 1):

        champion_row_string = champion_row_list[i].text
        to_fill_list[i] = champion_row_string.split("\n")

        logging.info("champion_stats_list: %s", to_fill_list[i])

    return to_fill_list


offense_stats = [0] * len(champions_list)
offense_stats = stats_gathering(offense_stats)


defense_stats_button = driver.find_element_by_xpath('//div[@class="tag"]')
defense_stats_button.click()
time.sleep(1)

sort_by_champion_button = driver.find_element_by_xpath(
    '//div[@class="rt-th -cursor-pointer"]'
)
sort_by_champion_button.click()


defense_stats = [0] * len(champions_list)
defense_stats = stats_gathering(defense_stats)


driver.get("https://tftactics.gg/db/champions")

time.sleep(1)

sort_by_champion_button = driver.find_element_by_xpath(
    '//div[@class="rt-th -cursor-pointer"]'
)
sort_by_champion_button.click()


origin_stats = [0] * len(champions_list)
origin_stats = stats_gathering(origin_stats)


for champ in origin_stats:
    if len(champ) == 4:
        # origin secondary and class secondary should be set to none
        champ.insert(2, "None")
        champ.insert(4, "None")

origins_list = []
for stat in origin_stats:
    origins_list.append(stat[1])

origins_list = sorted(list(set(origins_list)))

class_list = []
for stat in origin_stats:
    if stat[2] == "None":
        class_list.append(stat[3])
        logging.info("stat[2]: %s, appending stat[3]: %s", stat[2], stat[3])
        logging.info("%s", class_list)

class_list = sorted(list(set(class_list)))


new_classes = []
for stat in origin_stats:
    if stat[2] not in (["None"] + class_list):
        if len(stat) == 5:
            # double origin without secondary class
            logging.info(
                "Double origin for champ: %s, second origin: %s", stat[0], stat[2]
            )
            stat.insert(4, "None")
            logging.info(
                "Stats with none inserted as secondary class: %s, len: %s",
                stat,
                len(stat),
            )
    if stat[3] not in (["None"] + origins_list):
        if len(stat) == 5:
            # double class without secondary origin
            logging.info(
                "Double class for champ: %s,second class: %s", stat[0], stat[3]
            )
            if stat[3] not in (["None"] + origins_list + new_classes):
                logging.info(
                    "Class not seen yet appending into new_classes: %s", stat[3]
                )
                new_classes.append(stat[3])
            stat.insert(2, "None")
            logging.info(
                "Stats with none inserted as secondary origin: %s, len: %s",
                stat,
                len(stat),
            )

class_list = class_list + new_classes
class_list = sorted(list(set(class_list)))

driver.get("https://tftactics.gg/tierlist/champions")

image_elements = driver.find_elements_by_xpath('//div[@class="character-wrapper"]/img')

tier_elements_list = driver.find_elements_by_xpath('//div[@class="characters-list"]')

len_of_tier_elements_list = []
for tier in tier_elements_list:
    champs_tier_elements_list = tier.find_elements_by_xpath(
        './/div[@class="character-wrapper"]/img'
    )
    len_of_tier_elements_list.append(len(champs_tier_elements_list))

#### count how many champs are in each tier
ChampionTier = namedtuple("ChampTier", ["champion", "tier"])
s_tier = len_of_tier_elements_list[0]
a_tier = len_of_tier_elements_list[1]
b_tier = len_of_tier_elements_list[2]
c_tier = len_of_tier_elements_list[3]
d_tier = len_of_tier_elements_list[4]
champion_tier_list = []
for i in range(0, s_tier, 1):
    champion_tier_list.append(ChampionTier(image_elements[i].get_attribute("alt"), 5))

for i in range(s_tier, a_tier + s_tier, 1):
    champion_tier_list.append(ChampionTier(image_elements[i].get_attribute("alt"), 4))


for i in range(a_tier + s_tier, b_tier + a_tier + s_tier, 1):
    champion_tier_list.append(ChampionTier(image_elements[i].get_attribute("alt"), 3))

for i in range(b_tier + a_tier + s_tier, c_tier + b_tier + a_tier + s_tier, 1):
    champion_tier_list.append(ChampionTier(image_elements[i].get_attribute("alt"), 2))

for i in range(
    c_tier + b_tier + a_tier + s_tier, d_tier + c_tier + b_tier + a_tier + s_tier, 1
):
    champion_tier_list.append(ChampionTier(image_elements[i].get_attribute("alt"), 1))


champion_tier_list.sort()


driver.close()

gathered_stats_list = []
for i in range(0, len(champions_list)):
    gathered_stats_list.append(
        offense_stats[i] + defense_stats[i][1:] + origin_stats[i][1:]
    )
    gathered_stats_list[i].insert(14, champion_tier_list[i].tier)


df = pd.DataFrame.from_records(
    gathered_stats_list,
    columns=[
        "champion",
        "dps",
        "as_",
        "dmg",
        "range",
        "hp",
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


df.to_csv("championsData.csv", encoding="utf-8")


championNamesList = df.champion.to_list()


Champion = namedtuple(
    "Champion",
    [
        "champion",
        "dps",
        "as_",
        "dmg",
        "range",
        "hp",
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


for i, name in enumerate(championNamesList):
    # wasted 2 hours for searching answer how to create variable variable
    print(name.replace(" ", ""), end="")
    print(" = Champion(*gathered_stats_list[%d])" % i)


Aatrox = Champion(*gathered_stats_list[0])
Akali = Champion(*gathered_stats_list[1])
Annie = Champion(*gathered_stats_list[2])
AurelionSol = Champion(*gathered_stats_list[3])
Azir = Champion(*gathered_stats_list[4])
Brand = Champion(*gathered_stats_list[5])
Braum = Champion(*gathered_stats_list[6])
Chogath = Champion(*gathered_stats_list[7])
Darius = Champion(*gathered_stats_list[8])
Diana = Champion(*gathered_stats_list[9])
Elise = Champion(*gathered_stats_list[10])
Fiora = Champion(*gathered_stats_list[11])
Garen = Champion(*gathered_stats_list[12])
Irelia = Champion(*gathered_stats_list[13])
Janna = Champion(*gathered_stats_list[14])
JarvanIV = Champion(*gathered_stats_list[15])
Jax = Champion(*gathered_stats_list[16])
Kalista = Champion(*gathered_stats_list[17])
Katarina = Champion(*gathered_stats_list[18])
Kayle = Champion(*gathered_stats_list[19])
Kennen = Champion(*gathered_stats_list[20])
Kindred = Champion(*gathered_stats_list[21])
LeeSin = Champion(*gathered_stats_list[22])
Lulu = Champion(*gathered_stats_list[23])
Maokai = Champion(*gathered_stats_list[24])
Morgana = Champion(*gathered_stats_list[25])
Nasus = Champion(*gathered_stats_list[26])
Nautilus = Champion(*gathered_stats_list[27])
Neeko = Champion(*gathered_stats_list[28])
Nidalee = Champion(*gathered_stats_list[29])
Nunu = Champion(*gathered_stats_list[30])
Olaf = Champion(*gathered_stats_list[31])
Ornn = Champion(*gathered_stats_list[32])
Pyke = Champion(*gathered_stats_list[33])
Rakan = Champion(*gathered_stats_list[34])
Samira = Champion(*gathered_stats_list[35])
Sejuani = Champion(*gathered_stats_list[36])
Sett = Champion(*gathered_stats_list[37])
Shen = Champion(*gathered_stats_list[38])
Shyvana = Champion(*gathered_stats_list[39])
Sivir = Champion(*gathered_stats_list[40])
Swain = Champion(*gathered_stats_list[41])
TahmKench = Champion(*gathered_stats_list[42])
Talon = Champion(*gathered_stats_list[43])
Teemo = Champion(*gathered_stats_list[44])
Tristana = Champion(*gathered_stats_list[45])
Tryndamere = Champion(*gathered_stats_list[46])
TwistedFate = Champion(*gathered_stats_list[47])
Veigar = Champion(*gathered_stats_list[48])
Vi = Champion(*gathered_stats_list[49])
Vladimir = Champion(*gathered_stats_list[50])
Wukong = Champion(*gathered_stats_list[51])
Xayah = Champion(*gathered_stats_list[52])
Yasuo = Champion(*gathered_stats_list[53])
Yone = Champion(*gathered_stats_list[54])
Yuumi = Champion(*gathered_stats_list[55])
Zed = Champion(*gathered_stats_list[56])
Zilean = Champion(*gathered_stats_list[57])
