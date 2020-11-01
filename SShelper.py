# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 08:15:50 2020

@author: janusz
"""

from PIL import ImageGrab
snapshot = ImageGrab.grab()
save_path = "C:\\Users\\janusz\\Pictures\\tft\\MySnapshot.jpg"
snapshot.save(save_path)