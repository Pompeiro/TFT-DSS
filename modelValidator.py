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




bear_types = 'akali', 'annie', 'aphelios', 'ashe', 'cassiopeia', 'diana', 'evelynn', 'fiora', 'garen', 'hecarim', 'irelia', 'janna', 'jarvan', 'jax', 'jhin', 'jinx', 'kalista', 'kennen', 'kindred', 'lee', 'lissandra', 'lulu', 'lux', 'maokai', 'morgana', 'nami', 'nidalee', 'nunu', 'pyke', 'sejuani', 'sett', 'shen', 'sylas', 'tahm', 'talon', 'teemo', 'thresh', 'vayne', 'veigar', 'vi', 'warwick', 'wukong', 'xin', 'yasuo', 'yone', 'yummi', 'zed', 'zilean'

path = Path('C:\\Users\\janusz\\Pictures\\tft\\testingimages\\testing')
bears = DataBlock(
    blocks=(ImageBlock, CategoryBlock), 
    get_items=get_image_files, 
    splitter=RandomSplitter(valid_pct=0.2, seed=42),
    get_y=parent_label,
    item_tfms=Resize(128))
dls = bears.dataloaders(path,batch_size=8)


path = "C:\\Users\\janusz\\Documents\\TFT-DSS\\models\\modelChampsWithoutLVL"
learn = cnn_learner(dls, resnet18, metrics=error_rate)

learn_inf = learn.load(path) 

mainDirectory = 'C:\\Users\\janusz\\Pictures\\tft\\testingimages\\graTest'

print(learn_inf.predict('C:\\Users\\janusz\\Pictures\\tft\\testingimages\\graTest\\part10\\name00000026.jpg')[0])



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
