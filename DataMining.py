# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 11:39:13 2020

@author: Janusz
"""


from selenium import webdriver
import pandas as pd
df = pd.DataFrame(columns=['Champion','DPS','Attack Speed','Damage','Range']) # creates master dataframe 
from collections import namedtuple




driver = webdriver.Opera()
driver.get('https://tftactics.gg/db/champion-stats')
driver.find_element_by_xpath('//div[@class="rt-th -cursor-pointer"]').click()



list_category_elements=[]
for i in range(1,5,1):
    list_category_elements.append(driver.find_elements_by_xpath('//a[@class="characters-item c%d"]'%i))
    
links = driver.find_elements_by_xpath('//div[@class="rt-tr-group"]')


content = driver.find_elements_by_css_selector('a')

pStart = 0
pStop = 0
for i in range(0,len(content),1):
    if content[i].text == 'Ahri': ############ First champion sorted by name
        pStart = i
    if content[i].text =='Zoe':############ Last champion sorted by name
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
Stier = 6
Atier = 19
Btier = 23
Ctier = 7
Dtier = 2
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


driver.close()

for i,champ in enumerate(step3):
    champ.insert(13,ChampionTierList[i].Tier)


Champion = namedtuple('Champ', ['Champion', 'DPS', 'AS', 'DMG', 'Range', 'HP', 'Mana', 'Armor', 'MR', 'Origin', 'ClassPrimary', 'ClassSecondary', 'Cost', 'Tier'])









z = pd.DataFrame.from_records(step3, columns=['Champion', 'DPS', 'AS', 'DMG', 'Range', 'HP', 'Mana', 'Armor', 'MR', 'Origin', 'ClassPrimary', 'ClassSecondary', 'Cost', 'Tier'])


z.to_csv('championsData.csv', encoding='utf-8')



championNamesList =z.Champion.to_list()

for i,name in enumerate(championNamesList): ######## wasted 2 hours for searching answer how to create variable variable
    print(name.replace(" ", ""), end='')
    print(' = Champion(*step3[%d])'%i)
    
    
    
# z.to_csv('file_name.csv', encoding='utf-8')
# Ahri = Champion(*step2[0])
# Annie = Champion(*step2[1])
# Ashe = Champion(*step2[2])
# AurelionSol = Champion(*step2[3])
# Blitzcrank = Champion(*step2[4])
# Caitlyn = Champion(*step2[5])
# Chogath = Champion(*step2[6])
# Darius = Champion(*step2[7])
# Ekko = Champion(*step2[8])
# Ezreal = Champion(*step2[9])
# Fiora = Champion(*step2[10])
# Fizz = Champion(*step2[11])
# Gangplank = Champion(*step2[12])
# Graves = Champion(*step2[13])
# Irelia = Champion(*step2[14])
# JarvanIV = Champion(*step2[15])
# Jayce = Champion(*step2[16])
# Jhin = Champion(*step2[17])
# Jinx = Champion(*step2[18])
# Kaisa = Champion(*step2[19])
# Karma = Champion(*step2[20])
# Kassadin = Champion(*step2[21])
# Kayle = Champion(*step2[22])
# Khazix = Champion(*step2[23])
# Leona = Champion(*step2[24])
# Lucian = Champion(*step2[25])
# Lulu = Champion(*step2[26])
# Lux = Champion(*step2[27])
# Malphite = Champion(*step2[28])
# MasterYi = Champion(*step2[29])
# MissFortune = Champion(*step2[30])
# Mordekaiser = Champion(*step2[31])
# Neeko = Champion(*step2[32])
# Poppy = Champion(*step2[33])
# Rakan = Champion(*step2[34])
# Rumble = Champion(*step2[35])
# Shaco = Champion(*step2[36])
# Shen = Champion(*step2[37])
# Sona = Champion(*step2[38])
# Soraka = Champion(*step2[39])
# Syndra = Champion(*step2[40])
# Thresh = Champion(*step2[41])
# TwistedFate = Champion(*step2[42])
# Velkoz = Champion(*step2[43])
# Vi = Champion(*step2[44])
# Wukong = Champion(*step2[45])
# Xayah = Champion(*step2[46])
# Xerath = Champion(*step2[47])
# XinZhao = Champion(*step2[48])
# Yasuo = Champion(*step2[49])
# Ziggs = Champion(*step2[50])
# Zoe = Champion(*step2[51])


