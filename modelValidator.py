# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 20:04:21 2020

@author: janusz
"""

import os
mainDirectory = 'C:\\Users\\janusz\\Pictures\\tft\\testingimages\\graTest'

u = os.listdir(mainDirectory)

fullPathToSecondaryDirectoryList = []

for i,filename in enumerate(u):
    print(filename)
    fullPathToSecondaryDirectoryList.append(os.path.join(mainDirectory, filename))
print(fullPathToSecondaryDirectoryList)