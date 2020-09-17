# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 11:39:13 2020

@author: Janusz
"""


from selenium import webdriver
import pandas as pd
df = pd.DataFrame(columns=['Champion','DPS','Attack Speed','Damage','Range']) # creates master dataframe 
from collections import namedtuple

import time


driver = webdriver.Opera()
driver.get('https://tftactics.gg/db/champion-stats')
time.sleep(3)
driver.find_element_by_xpath('//a[@class="cmpboxbtn cmpboxbtnyes"]').click() # accept cookies
time.sleep(1)

driver.find_element_by_xpath('//div[@class="rt-th -cursor-pointer"]').click()



list_category_elements=[]
for i in range(1,5,1):
    list_category_elements.append(driver.find_elements_by_xpath('//a[@class="characters-item c%d"]'%i))
    
links = driver.find_elements_by_xpath('//div[@class="rt-tr-group"]')


content = driver.find_elements_by_css_selector('a')

pStart = 0
pStop = 0
for i in range(0,len(content),1):
    if content[i].text == 'Aatrox': ############ First champion sorted by name
        pStart = i
    if content[i].text =='Zilean':############ Last champion sorted by name
        pStop = i+1####  +1 because for loop stops at i +1
        
championList = [0] * (pStop-pStart)
for i in range(pStart,pStop,1):
    championList[i-35]=content[i].text



NEWSTATSGATHERINGFLAG = 0

fStart = 0    
u=0
listOfResults = (0,) * len(championList)

def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]






def stats_gathering(resultslist,flag):
    links = driver.find_elements_by_xpath('//div[@class="rt-tr-group"]')


    resultslist=list(resultslist)
    for j in range(0,len(championList),1):
        # fStart = 0    ######## need to reset 
        
        
        result=[0] * (len(find(links[j].text,"\n")) +1) ### how many elements is in the table 
        # print(result)
        fEnd=find(links[j].text,"\n") +[500] ### 500 means to the end
        fStart = fEnd[0:-1]
        fStart = [x+1 for x in fStart]
        fStart = [0] + fStart
        # print(links[j].text)
        # print("RESULT",result)
        for i in range(0,len(result),1):
            # print(u)
            # print(links[j].text)
            try:
                # print("Result,i",result,i)
                # print("fstart, fEnd[i]",fStart[i],fEnd[i])
                # print(fStart[i])
                result[i] = float(links[j].text[fStart[i]:fEnd[i]])
                # print("Result[i]",result[i])
            except ValueError:
                result[i] = links[j].text[fStart[i]:fEnd[i]]
              #   print("This is result: ", result)
 
            
            try:
                result[i] = result[i].replace(" ", "")
            except:
                pass
        # print(links[j].text)
        # print("Thats j",j)
        # print("Thats results",result)        
        if flag == 0:        
            resultslist[j] = result
        else:
            resultslist[j] = resultslist[j]+result[1:]
        # print("Thats listOfResults[j]: ",resultslist[j])
        # print("Thats listOfResults: ",listOfResults)

    return tuple(resultslist) #### i dont want it to be mutable to check step1 and step2
# print(listOfResults)

step1 = stats_gathering(listOfResults,NEWSTATSGATHERINGFLAG)


driver.find_element_by_xpath('//div[@class="tag"]').click()

driver.find_element_by_xpath('//div[@class="rt-th -cursor-pointer"]').click()

NEWSTATSGATHERINGFLAG=1


step2 = stats_gathering(step1,NEWSTATSGATHERINGFLAG)


driver.get('https://tftactics.gg/db/champions')



driver.find_element_by_xpath('//div[@class="rt-th -cursor-pointer"]').click()


NEWSTATSGATHERINGFLAG=2


step3 = stats_gathering(step2,NEWSTATSGATHERINGFLAG)


for champ in step3:
    if len(champ) == 12:
        champ.insert(11,'None')





driver.get('https://tftactics.gg/tierlist/champions')





image_elements = driver.find_elements_by_xpath('//div[@class="character-wrapper"]/img')
#### count how many champs are in each tier
ChampionTier = namedtuple('ChampTier', ['Champion', 'Tier'])
Stier = 3
Atier = 16
Btier = 22
Ctier = 14
Dtier = 3
ChampionTierList =[]
for i in range(0,Stier,1):
    ChampionTierList.append(ChampionTier(image_elements[i].get_attribute('alt'),5))
    
for i in range(Stier,Atier+Stier,1):
    ChampionTierList.append(ChampionTier(image_elements[i].get_attribute('alt'),4))


for i in range(Atier+Stier,Btier+Atier+Stier,1):
    ChampionTierList.append(ChampionTier(image_elements[i].get_attribute('alt'),3))
    
for i in range(Btier+Atier+Stier,Ctier+Btier+Atier+Stier,1):
    ChampionTierList.append(ChampionTier(image_elements[i].get_attribute('alt'),2))

for i in range(Ctier+Btier+Atier+Stier,Dtier+Ctier+Btier+Atier+Stier,1):
    ChampionTierList.append(ChampionTier(image_elements[i].get_attribute('alt'),1))    
    
    
ChampionTierList.sort()    


# driver.close()

for i,champ in enumerate(step3):
    champ.insert(13,ChampionTierList[i].Tier)


Champion = namedtuple('Champ', ['Champion', 'DPS', 'AS', 'DMG', 'Range', 'HP', 'Mana', 'Armor', 'MR', 'Origin', 'ClassPrimary', 'ClassSecondary', 'Cost', 'Tier'])



############# need to add origin secondary

classList = ['Adept', 'Assassin', 'Brawler', 'Dazzler', 'Duelist', 'Hunter',
             'Keeper', 'Mage', 'Mystic', 'Shade', 'Sharpshooter', 'Vanguard']

originsList = ['Cultist', 'Divine', 'Dusk', 'Elderwood', 'Enlightened', 'Exile', 
               'Fortune', 'Moonlight', 'Ninja', 'Spirit', 'TheBoss', 'Tormented', 
               'Warlord']


for champ in step3:
    champ.insert(10, 'None')
    if champ[11] in originsList:
        champ[10] = champ[11]
        champ[11] = champ[12]
        champ[12] = 'None'
        

z = pd.DataFrame.from_records(step3, columns=['Champion', 'DPS', 'AS', 'DMG', 'Range', 'HP', 'Mana', 'Armor', 'MR', 'OriginPrimary', 'OriginSecondary', 'ClassPrimary', 'ClassSecondary', 'Cost', 'Tier'])


z.to_csv('championsData.csv', encoding='utf-8')



championNamesList =z.Champion.to_list()

for i,name in enumerate(championNamesList): ######## wasted 2 hours for searching answer how to create variable variable
    print(name.replace(" ", ""), end='')
    print(' = Champion(*step3[%d])'%i)
    
    
    
# z.to_csv('file_name.csv', encoding='utf-8')
Aatrox = Champion(*step3[0])
Ahri = Champion(*step3[1])
Akali = Champion(*step3[2])
Annie = Champion(*step3[3])
Aphelios = Champion(*step3[4])
Ashe = Champion(*step3[5])
Azir = Champion(*step3[6])
Cassiopeia = Champion(*step3[7])
Diana = Champion(*step3[8])
Elise = Champion(*step3[9])
Evelynn = Champion(*step3[10])
Ezreal = Champion(*step3[11])
Fiora = Champion(*step3[12])
Garen = Champion(*step3[13])
Hecarim = Champion(*step3[14])
Irelia = Champion(*step3[15])
Janna = Champion(*step3[16])
JarvanIV = Champion(*step3[17])
Jax = Champion(*step3[18])
Jhin = Champion(*step3[19])
Jinx = Champion(*step3[20])
Kalista = Champion(*step3[21])
Katarina = Champion(*step3[22])
Kayn = Champion(*step3[23])
Kennen = Champion(*step3[24])
Kindred = Champion(*step3[25])
LeeSin = Champion(*step3[26])
Lillia = Champion(*step3[27])
Lissandra = Champion(*step3[28])
Lulu = Champion(*step3[29])
Lux = Champion(*step3[30])
Maokai = Champion(*step3[31])
Morgana = Champion(*step3[32])
Nami = Champion(*step3[33])
Nidalee = Champion(*step3[34])
Nunu = Champion(*step3[35])
Pyke = Champion(*step3[36])
Riven = Champion(*step3[37])
Sejuani = Champion(*step3[38])
Sett = Champion(*step3[39])
Shen = Champion(*step3[40])
Sylas = Champion(*step3[41])
TahmKench = Champion(*step3[42])
Talon = Champion(*step3[43])
Teemo = Champion(*step3[44])
Thresh = Champion(*step3[45])
TwistedFate = Champion(*step3[46])
Vayne = Champion(*step3[47])
Veigar = Champion(*step3[48])
Vi = Champion(*step3[49])
Warwick = Champion(*step3[50])
Wukong = Champion(*step3[51])
XinZhao = Champion(*step3[52])
Yasuo = Champion(*step3[53])
Yone = Champion(*step3[54])
Yuumi = Champion(*step3[55])
Zed = Champion(*step3[56])
Zilean = Champion(*step3[57])


