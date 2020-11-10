# TFT-DSS
Teamfight Tactics Decisive Support System  

17.09 back to business and working on improvements in set 4, was doing research about neural networks to deal with computer vision for DSS.

This is my current project, and I will work on advices which champion should user pick from 5 random champions that user can buy.  

I will use my knowledge to build fuzzy logic system that will calculate uncertain utility for every single champion and their combinations as a team.  I dont recommend using it in ranked games especially its was tested only about 30 times in game on my personal machine.

You can track my progress in projects section.


When u want to update csv files by yourself, if not then scroll down to TFTDSS.py 

# Web scraping with DataMining.py
This file uses selenium, pandas, collections/namedtuple and time.

Opera webdriver is required, or u can change it to Chrome but you need to change it in code also.

Website where I am gathering data about champions is tftactics.gg

Run DataMining.py -> in the back there are gathered and refined data filled into pandas dataframe

This dataframe is converted into championsData.csv
This file contains csv such as: Champion(name), DPS, AS, DMG, Range, HP, Mana, Armor, MR, OriginPrimary, OriginSecondary, ClassPrimary, ClassSecondary, Cost, Tier

Pros: works

Cons: some code should be more automated

# FuzzyCalculation.py
This file uses pandas, numpy, skfuzzy, namedtuple.

championsData.csv file is also required which is obtained by running DataMining.py


What happens there?

-Effective HP calculation
-Scaling all stats from 0.0 to 1.0
-Using fuzzy system to set preference that MEANHP is more important than HP
-Total points for single champion calculation with formula that is based on my knowledge about game(my playstyle/preferences) and Tier from tftactics.gg


Run FuzzyCalculation.py -> return scaledChampionsdf.csv

# ChampionsDataAnalysis.py
This file uses pandas, numpy, matplotlib.

scaledChampionsdf.csv file is also required which is obtained by running FuzzyCalculation.py

Data about some(7) champions is visualized on radar plot u can take a look for example, just scroll down.

U can change argument in line 183 to pick champions cost tier that u want to plot.


Run ChampionsDataAnalysis.py -> return figure with radar plots.

# TFTDSS.py
This file uses tkinter, pandas, namedtuple, easyocr, cv2(openCV).

scaledChampionsdf.csv file is also required which is obtained by running FuzzyCalculation.py

note: you should use window mode on full hd resolution in game.
-------------------------------------------------------------
GUI

-Semi automated GUI building
-Champions as counters
-Classes and origins as counters

-User can add(1) or sub(1) from counter
-User can reset every counter on Champions to buy pool to 0 value with single button(reset)
-User can update classes and origins based on Champion pool counters with single button(update classes)
-User can show points for champions to buy(show points button) // points are calculated basing on champion pool, origin and class counters
-User can use OCR to update champions to buy counters(OCR button)
-User can visualize which champion to buy, where champ with most points is bordered with green rectangle, then 3 champions with worse points score are presented with blue rectangles, and the worst champion has red rectangle(draw rectangles button)
-Scan&go button is reseting champions to buy counters. Then updating champion pool, origin and class counters. Next it uses OCR to detect champions to buy from buy zone. Finally it shows points for champions to buy.
-User can add(1) to Champion pool counter by clicking champion name that appear with points


You should use +- buttons in champion pool to feed system with ur current champion pool.
Then scan&go, and after buttons named by champions appear click on that, that you will buy them.
-----------------------------------------------------------------

Points calculation with champion pool included(not single champion like in FuzzyCalculation.py file).

Formula is based on my experience in game and my playstyle.

Points = single champion points(already calculated in FuzzyCalculation.py file) + bonus for the same origin(counter * 0.2) + bonus for the same class(counter * 0.2) + bonus for the same champion in pool((counter -1) * 0.2)


# SShelper.py
This file is used for cropping screenshots to extract in game champion models which im going to feed neural network model.







# Data visualization.
![StatsPlot](https://user-images.githubusercontent.com/60773657/85411123-3d6cfb00-b568-11ea-9eee-8dc245cdcd4e.png)


# Using DSS in game.


![TFTDSS1](https://user-images.githubusercontent.com/60773657/86474906-0951c100-bd44-11ea-9c46-7b530c1c4cb4.png)


Results of first three attempts playing normal game with 54 points in silver 4.
You should pay attention that TFTDSS supported me only in choosing champion to buy. I took care about items and champions placement on the field myself.

![Scores](https://user-images.githubusercontent.com/60773657/86474581-6bf68d00-bd43-11ea-849a-700741035bc8.png)

# Draw rectangles button(cross mode)
![crosses](https://user-images.githubusercontent.com/60773657/97043409-b7db7500-1572-11eb-88b3-b801c00439d9.jpg)


