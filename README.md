# SET5 update released: 4th May 2021

# Community
Help me to push this project forward by providing feedback in [Issues](https://github.com/Pompeiro/TFT-DSS/issues) or [Discussions](https://github.com/Pompeiro/TFT-DSS/discussions). U can even find me in Discord Papaj#3719, if u want to commit into the project.

# TFT-DSS
Teamfight Tactics Decisive Support System  

This is my current project, and I will work on advices which champion should user pick from 5 random champions that user can buy.  

# Click on image to watch the video

[![TFTvideo](https://user-images.githubusercontent.com/60773657/106586367-a67a0f80-6548-11eb-85ad-be8c59a92b8e.JPG)](https://user-images.githubusercontent.com/60773657/106585948-2e134e80-6548-11eb-8d20-d817a1261879.mp4)


# Installation

I highly recommend you to create new virtual environment. I am using Anaconda distribution. Python 3.8.5 is working for me.

conda create -n tft python=3.8.5

conda activate tft

then go to https://pytorch.org/ and check INSTALL PYTORCH section.

"Note 1: for Windows, please install torch and torchvision first by following the official instruction here https://pytorch.org. On pytorch website, be sure to select the right CUDA version you have. If you intend to run on CPU mode only, select CUDA = None."
Reference from https://github.com/JaidedAI/EasyOCR

Then install requirements from requirements.txt

Run TFTDSS.py in your IDE(for me working in Spyder and in Pycharm). You need to use tft virtual env.

# 14.04.2021 I'm back
Thanks to @Detergent13 I'm back to business. To test functions swap comments in TFTDSS.py
52 | TEST_BUTTON_VISIBLE = 0
53 | # TEST_BUTTON_VISIBLE = 1

When u want to update csv files by yourself, if not then scroll down to TFTDSS.py 


# Web scraping with DataMining.py
This file uses selenium, pandas, collections/namedtuple and time.

Opera webdriver is required, or u can change it to Chrome but you need to change it in code also.

Website where I am gathering data about champions is tftactics.gg

Run DataMining.py -> in the back there are gathered and refined data filled into pandas dataframe

This dataframe is converted into championsData.csv
This file contains csv such as: Champion(name), DPS, AS, DMG, Range, HP, Mana, Armor, MR, OriginPrimary, OriginSecondary, ClassPrimary, ClassSecondary, Cost, Tier


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
-User can directly refresh shop from GUI.
-User can directly buy xp from GUI.


You should use +- buttons in champion pool to feed system with ur current champion pool.
Then scan&go, and after buttons named by champions appear click on that, that you will buy them.
-----------------------------------------------------------------

Points calculation with champion pool included(not single champion like in FuzzyCalculation.py file).

Formula is based on my experience in game and my playstyle.

Points = single champion points(already calculated in FuzzyCalculation.py file) + bonus for the same origin(counter * 0.2) + bonus for the same class(counter * 0.2) + bonus for the same champion in pool((counter -1) * 0.2)


# Data visualization.
![DataAnalysisTier4](https://user-images.githubusercontent.com/60773657/105047831-1e393c00-5a6b-11eb-9fb0-fbf8cf76db6e.png)


# Using DSS in game.


![TFTDSSinGame](https://user-images.githubusercontent.com/60773657/105048410-d5ce4e00-5a6b-11eb-84ab-0ba6b5fe86e4.jpg)



Results of first three attempts playing normal game with 54 points in silver 4.
You should pay attention that TFTDSS supported me only in choosing champion to buy. I took care about items and champions placement on the field myself.

![Scores](https://user-images.githubusercontent.com/60773657/86474581-6bf68d00-bd43-11ea-849a-700741035bc8.png)

# Draw rectangles button(points mode)
![DrawRectangles](https://user-images.githubusercontent.com/60773657/105048542-fd251b00-5a6b-11eb-8cd3-bcf2b701984b.jpg)


# Champion object detection
I think i need to collect more images.
![Champion-detection2](https://user-images.githubusercontent.com/60773657/99180678-7fb9f300-2728-11eb-80bf-87b75fb2a74e.JPG)

![Champion-detection3](https://user-images.githubusercontent.com/60773657/99180674-76308b00-2728-11eb-9309-a37063c0dfa2.JPG)



07.12.2020 object champion detection with YOLO
![ROTD1](https://user-images.githubusercontent.com/60773657/101356751-d71b3100-3898-11eb-9756-85f22e17dbd7.jpg)



# botActions.py
Working bot which buy preffered class of champions for example brawlers. Shuffling champions on playground and subsitutes bench after champion is bought. Also spending gold in predefined rounds for XP or refreshing champions to buy. This bot is mainly for automate screenshots gathering to feed my dataset to train object detection model, but it performs well and can beat some players. For sure it beats "afk bots".
For sure you need to clone directories with JPGs like TemplateMatchingClient.

Just be sure to set windowed mode in game, and after log in u can run this code.
