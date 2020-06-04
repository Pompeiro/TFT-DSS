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
    if content[i].text == 'Ahri': ############ First champion sorted by DPS
        pStart = i
    if content[i].text =='Zoe':############ Last champion sorted by DPS
        pStop = i+1####  +1 because for loop stops at i +1
        
championList = [0] * (pStop-pStart)
for i in range(pStart,pStop,1):
    championList[i-35]=content[i].text



NEWSTATSGATHERINGFLAG = 0

fStart = 0    
u=0
listOfResults = (0,) * len(championList)
def stats_gathering(resultslist,flag):
    links = driver.find_elements_by_xpath('//div[@class="rt-tr-group"]')
    resultslist=list(resultslist)
    for j in range(0,len(championList),1):
        fStart = 0    ######## need to reset 
        result=[0] * 5
        u=0
        i=0
        while u != -1:
            u = links[j].text.find('\n',fStart)
            # print(u)
            #print(links[j].text)
            if u != -1:
                result[i] = links[j].text[fStart:u]
              #   print("This is result: ", result)
                fStart = u+1
            else:
                result[i] = float(links[j].text[u-1:])
                # print("Last result is:",result)
            
            if i >0:
                result[i] = float(result[i])
            i=i+1
        # print(links[j].text)
        # print("Thats j",j)
                
        if flag == 0:        
            resultslist[j] = result
        else:
            resultslist[j] = resultslist[j]+result[1:]
        # print("Thats listOfResults[j]: ",listOfResults[j])
        # print("Thats listOfResults: ",listOfResults)

    return tuple(resultslist) #### i dont want it to be mutable to check step1 and step2
print(listOfResults)

step1 = stats_gathering(listOfResults,0)


driver.find_element_by_xpath('//div[@class="tag"]').click()

driver.find_element_by_xpath('//div[@class="rt-th -cursor-pointer"]').click()

NEWSTATSGATHERINGFLAG=1


step2 = stats_gathering(step1,1)
driver.close()




Champion = namedtuple('Champ', ['Champion', 'DPS', 'AS', 'DMG', 'Range', 'HP', 'Mana', 'Armor', 'MR'])









z = pd.DataFrame.from_records(step2, columns=['Champion', 'DPS', 'AS', 'DMG', 'Range', 'HP', 'Mana', 'Armor', 'MR'])

championNamesList =z.Champion.to_list()

for i,name in enumerate(championNamesList): ######## wasted 2 hours for searching answer how to create variable variable
    print(name.replace(" ", ""), end='')
    print(' = Champion(*step2[%d])'%i)
    
    
    

Ahri = Champion(*step2[0])
Annie = Champion(*step2[1])
Ashe = Champion(*step2[2])
AurelionSol = Champion(*step2[3])
Blitzcrank = Champion(*step2[4])
Caitlyn = Champion(*step2[5])
Chogath = Champion(*step2[6])
Darius = Champion(*step2[7])
Ekko = Champion(*step2[8])
Ezreal = Champion(*step2[9])
Fiora = Champion(*step2[10])
Fizz = Champion(*step2[11])
Gangplank = Champion(*step2[12])
Graves = Champion(*step2[13])
Irelia = Champion(*step2[14])
JarvanIV = Champion(*step2[15])
Jayce = Champion(*step2[16])
Jhin = Champion(*step2[17])
Jinx = Champion(*step2[18])
Kaisa = Champion(*step2[19])
Karma = Champion(*step2[20])
Kassadin = Champion(*step2[21])
Kayle = Champion(*step2[22])
Khazix = Champion(*step2[23])
Leona = Champion(*step2[24])
Lucian = Champion(*step2[25])
Lulu = Champion(*step2[26])
Lux = Champion(*step2[27])
Malphite = Champion(*step2[28])
MasterYi = Champion(*step2[29])
MissFortune = Champion(*step2[30])
Mordekaiser = Champion(*step2[31])
Neeko = Champion(*step2[32])
Poppy = Champion(*step2[33])
Rakan = Champion(*step2[34])
Rumble = Champion(*step2[35])
Shaco = Champion(*step2[36])
Shen = Champion(*step2[37])
Sona = Champion(*step2[38])
Soraka = Champion(*step2[39])
Syndra = Champion(*step2[40])
Thresh = Champion(*step2[41])
TwistedFate = Champion(*step2[42])
Velkoz = Champion(*step2[43])
Vi = Champion(*step2[44])
Wukong = Champion(*step2[45])
Xayah = Champion(*step2[46])
Xerath = Champion(*step2[47])
XinZhao = Champion(*step2[48])
Yasuo = Champion(*step2[49])
Ziggs = Champion(*step2[50])
Zoe = Champion(*step2[51])


