# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 15:50:32 2021

@author: natha
"""

''' TO DO

Draw Pinhole
Convert to grayscale
Convert to Array
Perform Fourier Transform
Convert back to image
'''
#Import required image modules
import numpy as np
from PIL import Image, ImageDraw

#Create dark background and draw object
#Will be replaced with data from optics table

def simPin(xsize, ysize, radius):
    #create background
    arr = np.zeros([xsize, ysize], dtype = np.uint8)
    for x in range(xsize):
        for y in range(ysize):
            arr[x, y] = 0
            
    #prepare to draw pinhole
    im = Image.fromarray(arr)
    draw = ImageDraw.Draw(im)
    xcen = round(xsize * 0.5)
    ycen = round(ysize * 0.5)
    
    
    draw.ellipse([xcen - radius, ycen - radius, xcen +
                  radius, ycen + radius], fill = 255, 
                 outline = None)
    
    return im

pinhole = simPin(200, 200, 40)

pinhole.show()
    
    

