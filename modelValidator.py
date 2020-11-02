# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 20:04:21 2020

@author: janusz

This file should loop over every cropped screenshot to validate NN model

"""

import os

from fastbook import *
from fastai.vision.widgets import *

# path = "C:\\Users\\janusz\\Documents\\TFT-DSS\\first"
# path.ls(file_exts='.pth')


bear_types = 'akali','aphelios','diana','lissandra','lux','sylas'
path = Path('C:\\Users\\janusz\\Pictures\\tft\\images')
bears = DataBlock(
    blocks=(ImageBlock, CategoryBlock), 
    get_items=get_image_files, 
    splitter=RandomSplitter(valid_pct=0.2, seed=42),
    get_y=parent_label,
    item_tfms=Resize(128))
dls = bears.dataloaders(path,batch_size=8)


path = "C:\\Users\\janusz\\Documents\\TFT-DSS\\first"
learn = cnn_learner(dls, resnet18, metrics=error_rate)

learn_inf = learn.load(path) 

mainDirectory = 'C:\\Users\\janusz\\Pictures\\tft\\testingimages\\graTest'

u = os.listdir(mainDirectory)

fullPathToSecondaryDirectoryList = []

### fullPathToSecondaryDirectoryList filling

for i,filename in enumerate(u):
    print(filename)
    fullPathToSecondaryDirectoryList.append(os.path.join(mainDirectory, filename))
print(fullPathToSecondaryDirectoryList)


#### using model on every image

for i,filename in enumerate(fullPathToSecondaryDirectoryList):
    jpegsInSecondaryDirectory = os.listdir(fullPathToSecondaryDirectoryList[i])
    for j,filename in enumerate(jpegsInSecondaryDirectory):
        print(filename)
        pathToJPG = os.path.join(fullPathToSecondaryDirectoryList[i], filename)
        # print(pathToJPG)
        print(learn_inf.predict(pathToJPG))
