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
driver.get("https://tftactics.gg/tierlist/origins")
driver.maximize_window()
time.sleep(3)
accept_all_cookies_button = driver.find_element_by_xpath(
    '//a[@class="cmpboxbtn cmpboxbtnyes"]'
)
accept_all_cookies_button.click()
time.sleep(1)

origin_container_class = "characters-item"

elements_inside_origin_container_class = driver.find_elements_by_class_name(
    origin_container_class
)

origin_list = []
for element in elements_inside_origin_container_class:
    logging.info(
        "Element inside elements_inside_origin_container_class text: %s", element.text
    )
    if element.text:
        # if string isnt void then append element to list
        origin_list.append(element.text)

# to avoid duplicates
origin_list = list(set(origin_list))

driver.get("https://tftactics.gg/tierlist/classes")
time.sleep(2)
class_container_class = "characters-item"
elements_inside_class_container_class = driver.find_elements_by_class_name(
    class_container_class
)

class_list = []
for element in elements_inside_class_container_class:
    logging.info(
        "Element inside elements_inside_class_container_class text: %s", element.text
    )
    if element.text:
        # if string isnt void then append element to list
        class_list.append(element.text)

# to avoid duplicates
class_list = list(set(class_list))

driver.get("https://tftactics.gg/db/champion-stats")
time.sleep(2)

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


champion_names = driver.find_elements_by_css_selector("a")

for i in range(0, len(champion_names), 1):
    if champion_names[i].text == "Aatrox":  # First champion sorted by name
        FIRST_CHAMPION_IN_A_SELECTOR = i
        logging.info(
            "Found first champion index in 'a' selector: %d",
            FIRST_CHAMPION_IN_A_SELECTOR,
        )
    if champion_names[i].text == "Zyra":  # Last champion sorted by name
        LAST_CHAMPION_INDEX_IN_A_SELECTOR = i + 1  # +1 because for loop stops at i +1
        logging.info(
            "Found last champion index in 'a' selector: %d",
            LAST_CHAMPION_INDEX_IN_A_SELECTOR,
        )
        break

found_champions = LAST_CHAMPION_INDEX_IN_A_SELECTOR - FIRST_CHAMPION_IN_A_SELECTOR
logging.info("Number of found champions: %d", found_champions)

champions_list = []
for i in range(FIRST_CHAMPION_IN_A_SELECTOR, LAST_CHAMPION_INDEX_IN_A_SELECTOR, 1):
    logging.info(
        "Appending champion name: %s with index in 'a' css selector %d",
        champion_names[i].text,
        i,
    )
    champions_list.append(champion_names[i].text)


def find(string, character):
    """
    https://stackoverflow.com/questions/11122291/how-to-find-char-in-string-and-get-all-the-indexes

    Parameters
    ----------
    string : string.
    character : character to be found in string.

    Returns
    -------
    list
        DESCRIPTION.

    """
    logging.info(
        "find(string = %s, character = %s) found character in string on indexes: %s",
        string,
        character,
        [i for i, ltr in enumerate(string) if ltr == character],
    )
    return [i for i, ltr in enumerate(string) if ltr == character]


def stats_gathering(to_fill_list):
    """
    Gathering stats from site.

    Parameters
    ----------
    to_fill_list : empty list.

    Returns
    -------
    to_fill_list : list filled with stats from site.

    """
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

logging.info("Validation of data in origin_stats in comparison with origin_list")
for champ in origin_stats:
    if champ[1] in origin_list:
        logging.info("%s is in origin_list", champ[1])
    else:
        logging.error("%s is NOT in origin_list", champ[1])

    if champ[2] in origin_list:
        logging.info("%s is in origin_list, double origin there", champ[2])
    else:
        logging.info(
            "%s is NOT in origin_list, single origin there, inserting None", champ[2]
        )
        champ.insert(2, "None")

logging.info("Validation of data in origin_stats in comparison with class_list")
for champ in origin_stats:
    if champ[3] in class_list:
        logging.info("%s is in class_list", champ[3])
    elif champ[3] == "None":
        logging.info("%s is None", champ[3])
    else:
        logging.error("%s is NOT in class_list", champ[3])

    if champ[4] in class_list:
        logging.info("%s is in class_list", champ[4])
    else:
        logging.info(
            "%s is NOT in class_list, single class there, inserting None", champ[4]
        )
        champ.insert(4, "None")


for champ in origin_stats:
    if len(champ) == 4:
        # origin secondary and class secondary should be set to none
        champ.insert(2, "None")
        champ.insert(4, "None")


driver.get("https://tftactics.gg/tierlist/champions")

image_elements = driver.find_elements_by_xpath('//div[@class="character-wrapper"]/img')

tier_elements_list = driver.find_elements_by_xpath('//div[@class="characters-list"]')

len_of_tier_elements_list = []
for tier in tier_elements_list:
    champs_tier_elements_list = tier.find_elements_by_xpath(
        './/div[@class="character-wrapper"]/img'
    )
    len_of_tier_elements_list.append(len(champs_tier_elements_list))

# count how many champs are in each tier
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


df.to_csv("champions_data.csv", encoding="utf-8")


champion_names_list = df.champion.to_list()


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


for i, name in enumerate(champion_names_list):
    # wasted 2 hours for searching answer how to create variable variable
    print(name.replace(" ", ""), end="")
    print(" = Champion(*gathered_stats_list[%d])" % i)


Aatrox = Champion(*gathered_stats_list[0])
Akshan = Champion(*gathered_stats_list[1])
Aphelios = Champion(*gathered_stats_list[2])
Ashe = Champion(*gathered_stats_list[3])
Brand = Champion(*gathered_stats_list[4])
Diana = Champion(*gathered_stats_list[5])
Draven = Champion(*gathered_stats_list[6])
Fiddlesticks = Champion(*gathered_stats_list[7])
Galio = Champion(*gathered_stats_list[8])
Garen = Champion(*gathered_stats_list[9])
Gragas = Champion(*gathered_stats_list[10])
Gwen = Champion(*gathered_stats_list[11])
Hecarim = Champion(*gathered_stats_list[12])
Heimerdinger = Champion(*gathered_stats_list[13])
Irelia = Champion(*gathered_stats_list[14])
Ivern = Champion(*gathered_stats_list[15])
Jax = Champion(*gathered_stats_list[16])
Kalista = Champion(*gathered_stats_list[17])
Karma = Champion(*gathered_stats_list[18])
Kayle = Champion(*gathered_stats_list[19])
Kennen = Champion(*gathered_stats_list[20])
Khazix = Champion(*gathered_stats_list[21])
Kled = Champion(*gathered_stats_list[22])
LeeSin = Champion(*gathered_stats_list[23])
Leona = Champion(*gathered_stats_list[24])
Lucian = Champion(*gathered_stats_list[25])
Lulu = Champion(*gathered_stats_list[26])
Lux = Champion(*gathered_stats_list[27])
MissFortune = Champion(*gathered_stats_list[28])
Nautilus = Champion(*gathered_stats_list[29])
Nidalee = Champion(*gathered_stats_list[30])
Nocturne = Champion(*gathered_stats_list[31])
Nunu = Champion(*gathered_stats_list[32])
Olaf = Champion(*gathered_stats_list[33])
Poppy = Champion(*gathered_stats_list[34])
Pyke = Champion(*gathered_stats_list[35])
Rakan = Champion(*gathered_stats_list[36])
Rell = Champion(*gathered_stats_list[37])
Riven = Champion(*gathered_stats_list[38])
Sejuani = Champion(*gathered_stats_list[39])
Senna = Champion(*gathered_stats_list[40])
Sett = Champion(*gathered_stats_list[41])
Soraka = Champion(*gathered_stats_list[42])
Syndra = Champion(*gathered_stats_list[43])
Teemo = Champion(*gathered_stats_list[44])
Thresh = Champion(*gathered_stats_list[45])
Tristana = Champion(*gathered_stats_list[46])
Udyr = Champion(*gathered_stats_list[47])
Varus = Champion(*gathered_stats_list[48])
Vayne = Champion(*gathered_stats_list[49])
Velkoz = Champion(*gathered_stats_list[50])
Viego = Champion(*gathered_stats_list[51])
Vladimir = Champion(*gathered_stats_list[52])
Volibear = Champion(*gathered_stats_list[53])
Yasuo = Champion(*gathered_stats_list[54])
Ziggs = Champion(*gathered_stats_list[55])
Zyra = Champion(*gathered_stats_list[56])
