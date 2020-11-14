# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 20:04:21 2020

@author: janusz

This file should loop over every cropped screenshot to validate NN model


Plan:
    1. loading model.
    2. ensure that model is ansering.
    
    3. load screenshot.
    4. Crop screenshot and save it to directory.
    5. Loop over every image with model.
    6. print predictions on screenshot.

"""

import os

from fastbook import *
from fastai.vision.widgets import *

import os
import cv2 as cv



##########3 model loading


bear_types = 'akali', 'annie', 'aphelios', 'ashe', 'cassiopeia', 'diana', 'evelynn', 'fiora', 'garen', 'hecarim', 'irelia', 'janna', 'jarvan', 'jax', 'jhin', 'jinx', 'kalista', 'kennen', 'kindred', 'lee', 'lissandra', 'lulu', 'lux', 'maokai', 'morgana', 'nami', 'nidalee', 'nunu', 'pyke', 'sejuani', 'sett', 'shen', 'sylas', 'tahm', 'talon', 'teemo', 'thresh', 'vayne', 'veigar', 'vi', 'warwick', 'wukong', 'xin', 'yasuo', 'yone', 'yummi', 'zed', 'zilean'

path = Path('C:\\Users\\janusz\\Pictures\\tft\\testingimages\\testing') ## path to directory with directories as labels.
bears = DataBlock(
    blocks=(ImageBlock, CategoryBlock), 
    get_items=get_image_files, 
    splitter=RandomSplitter(valid_pct=0.2, seed=42),
    get_y=parent_label,
    item_tfms=Resize(128))
dls = bears.dataloaders(path)


path = "C:\\Users\\janusz\\Documents\\TFT-DSS\\models\\modelChampsWithoutLVL" # model file without .pth extension
learn = cnn_learner(dls, resnet18, metrics=error_rate)

learn_inf = learn.load(path) 

############ ensure model is answering on jpg file with prediction(champion name)

print(learn_inf.predict('C:\\Users\\janusz\\Pictures\\tft\\testingimages\\graTest\\part10\\name00000026.jpg')[0])


mainDirectory = 'C:\\Users\\janusz\\Pictures\\tft\\testingimages\\TestSet'







###### cropping screenshot




wincap = None



###################################
####################################
##################################

line_color = (255, 0, 255)
line_color_odd = (0,255,0)
line_type = cv.LINE_4
marker_color = (255, 0, 255)
marker_type = cv.MARKER_CROSS
marker_type_rectangle = cv.MARKER_SQUARE


# FIRST WIDTH THEN HEIGHT

championWidth = 108
championHeight = 150

topLeftStart = [580, 130]


topLeft = (topLeftStart[0], topLeftStart[1])
bottomRight = (topLeft[0] + championWidth, topLeft[1] + championHeight)
center = ((topLeft[0]+bottomRight[0])//2, (topLeft[1]+bottomRight[1])//2)


marker_position = [topLeft, bottomRight, center]


basicSSname = 'C:\\Users\\janusz\\Pictures\\tft\\testingimages\\TestSet\\screen.jpg'


def make_ss_and_show(loadImage=1, window=wincap, croppingY=0, croppingX=0, croppingHeight=1080, croppingWidth=1920, showMode=0, saveMode=0, savingSSName=basicSSname):
    if loadImage:
        screenshot = cv.imread("C:\\Users\\janusz\\Pictures\\tft\\testingimages\\TestSet\\name00000016.jpg",cv.IMREAD_UNCHANGED)
    else:
        k=5+3
        # screenshot = window.get_screenshot()
    #print(screenshot)
    crop_img = screenshot[croppingY:croppingY+croppingHeight, croppingX:croppingX+croppingWidth]
    if showMode:
        cv.imshow("ss", crop_img)
    if saveMode:
        # while True:
        #     if keyboard.is_pressed("p"):
        #         print("You pressed p")
        #         break
        # screenshot = window.get_screenshot()
        # crop_img = screenshot[croppingY:croppingY+croppingHeight, croppingX:croppingX+croppingWidth]
        cv.imwrite(savingSSName, crop_img)
    
    return crop_img


def draw_rectangle_and_center_and_show(screenshot, markerPosition=marker_position,line_coloring=line_color, showMode=0,name="wind", textPrediction="none"):
    cv.drawMarker(screenshot, markerPosition[2], color=line_coloring,
                  markerType=marker_type, markerSize=40, thickness=2)
    cv.rectangle(screenshot, markerPosition[0], markerPosition[1], color=line_coloring,
                          lineType=line_type, thickness=2)
    cv.putText(screenshot, textPrediction, markerPosition[2], cv.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
    
    if showMode:
        cv.imshow(name, screenshot)
    return screenshot

def draw_prediction_and_show(screenshot, markerPosition=marker_position,line_coloring=line_color, showMode=0,name="wind", textPrediction="none"):
    cv.putText(screenshot, textPrediction, markerPosition[2], cv.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
    
    if showMode:
        cv.imshow(name, screenshot)
    return screenshot




# need to add row offset because hexes in row arent in the same positions

rowOffset =[0,40,-20,25]
championWidthOffset = [0,5,7,11]

saving_marker_position = []

for row in range(0,4,1):
    for column in range(0,7,1):
        if row % 2 == 0:
            line_coloring = line_color
        else:
            line_coloring = line_color_odd
        
        topLeftStart = [520 + rowOffset[row]  + (championWidth + championWidthOffset[row]) * column, 290 + championHeight//2 * row]
        
        
        topLeft = (topLeftStart[0], topLeftStart[1])
        bottomRight = (topLeft[0] + championWidth, topLeft[1] + championHeight)
        center = ((topLeft[0]+bottomRight[0])//2, (topLeft[1]+bottomRight[1])//2)
        
        marker_position = [topLeft, bottomRight, center]
        saving_marker_position.append(marker_position)
        
        if column == 0 and row == 0:
            u=draw_rectangle_and_center_and_show(make_ss_and_show(showMode=0,saveMode=0),markerPosition=marker_position, line_coloring=line_coloring, showMode=0)
        else:
            u=draw_rectangle_and_center_and_show(u, markerPosition=marker_position, line_coloring=line_coloring, showMode=0)
        
        
        
u=draw_rectangle_and_center_and_show(u, markerPosition=saving_marker_position[8], line_coloring=line_color_odd, showMode=1, textPrediction="none")       

        

        
# cv.imshow("window",u)







# print("Main directory for screens in this game")
# mainDirectoryName = input()
# print("Your input for main directory is: ",mainDirectoryName)


mainDirectoryName = "croppedTest"

parentDirectory = "C:\\Users\\janusz\\Pictures\\tft\\testingimages\\TestSet\\"



parentDirectory = os.path.join(parentDirectory, mainDirectoryName)

try:
    os.mkdir(parentDirectory)
except OSError:
    print ("Creation of the directory %s failed" % path)
else:
    print ("Successfully created the directory %s " % path)

def create_directory(dirCounter=0, parentDir=parentDirectory): 
    # Directory 
    directory = "part{:02}".format(dirCounter)
      
    # Path 
    path = os.path.join(parentDir, directory) 
      
    try:
        os.mkdir(path)
    except OSError:
        print ("Creation of the directory %s failed" % path)
    else:
        print ("Successfully created the directory %s " % path)
    return path


global directoryCounter
directoryCounter = 0



#### saving cropped images with single champion
def save_single_hexes_into_created_directory(parentDir=parentDirectory):
    global directoryCounter
    dirpath = create_directory(dirCounter=directoryCounter)
    for i,markerpos in enumerate(saving_marker_position):
        screenName='name{:08}.jpg'.format(i)
        screenName = os.path.join(dirpath, screenName) 
        make_ss_and_show(croppingY=markerpos[0][1], croppingX=markerpos[0][0], croppingHeight=markerpos[1][1]-markerpos[0][1], croppingWidth=markerpos[1][0]-markerpos[0][0], saveMode=1, savingSSName=screenName)
    directoryCounter = directoryCounter + 1


def make_ss_and_save_multiple_times_on_key_pressed():
    print("Now press p to save screenshots.")
    for i in range(0,40,1):
        while True:
            if keyboard.is_pressed("p"):
                print("You pressed p")
                save_single_hexes_into_created_directory()
                break
        


save_single_hexes_into_created_directory()





croppedImagesList = os.listdir("C:\\Users\\janusz\\Pictures\\tft\\testingimages\\TestSet\\croppedTest\\part00")

mainDirectoryWithCroppedImages = "C:\\Users\\janusz\\Pictures\\tft\\testingimages\\TestSet\\croppedTest\\part00"



# parentDirectory = os.path.join(mainDirectoryWithCroppedImages, croppedImage)

predictionList = []
for i,croppedImage in enumerate(croppedImagesList):
    croppedJPGfile = os.path.join(mainDirectoryWithCroppedImages, croppedImage)
    cv.imshow("ss",cv.imread(croppedJPGfile,cv.IMREAD_UNCHANGED))
    print("image: ",i)
    predictionList.append(learn_inf.predict(croppedJPGfile)[0])
    print(predictionList[i])
    







rowOffset =[0,40,-20,25]
championWidthOffset = [0,5,7,11]

saving_marker_position = []

j=0

for row in range(0,4,1):
    for column in range(0,7,1):
        if row % 2 == 0:
            line_coloring = line_color
        else:
            line_coloring = line_color_odd
        
        topLeftStart = [520 + rowOffset[row]  + (championWidth + championWidthOffset[row]) * column, 290 + championHeight//2 * row]
        
        
        topLeft = (topLeftStart[0], topLeftStart[1])
        bottomRight = (topLeft[0] + championWidth, topLeft[1] + championHeight)
        center = ((topLeft[0]+bottomRight[0])//2, (topLeft[1]+bottomRight[1])//2)
        
        marker_position = [topLeft, bottomRight, center]
        saving_marker_position.append(marker_position)
        
        if column == 0 and row == 0:
            u=draw_prediction_and_show(make_ss_and_show(showMode=0,saveMode=0),markerPosition=marker_position, line_coloring=line_coloring, showMode=0,textPrediction=predictionList[j])
        else:
            u=draw_prediction_and_show(u, markerPosition=marker_position, line_coloring=line_coloring, showMode=0,textPrediction=predictionList[j])
        j=j+1
        
        
u=draw_prediction_and_show(u, markerPosition=saving_marker_position[0], line_coloring=line_color_odd, showMode=1, textPrediction="none")       













# u = os.listdir(mainDirectory)

# fullPathToSecondaryDirectoryList = []

# ### fullPathToSecondaryDirectoryList filling

# for i,filename in enumerate(u):
#     print(filename)
#     fullPathToSecondaryDirectoryList.append(os.path.join(mainDirectory, filename))
# print(fullPathToSecondaryDirectoryList)


# #### using model on every image

# for i,filename in enumerate(fullPathToSecondaryDirectoryList):
#     jpegsInSecondaryDirectory = os.listdir(fullPathToSecondaryDirectoryList[i])
#     for j,filename in enumerate(jpegsInSecondaryDirectory):
#         print(filename)
#         pathToJPG = os.path.join(fullPathToSecondaryDirectoryList[i], filename)
#         # print(pathToJPG)
#         print(learn_inf.predict(pathToJPG))
