# -*- coding: utf-8 -*-
"""
MakeCoolArt.py: Generates some cool pictures using recursive
    function compositions.
    Make sure to check Chris Stone's original nifty assignments.
    Instead of doing objects, we could do this using nested lists
Created on Wed Dec 18 11:18:15 2013

@author: pruvolo
"""

import random
import math
from PIL import Image

class RandomFunction(object):
    def __init__(self,min_level=5,max_level=8):
        if (max_level > 0):
            if (min_level > 0):
                self.ftype = random.randint(3,6)
            else:
                self.ftype = random.randint(1,6)
            if (self.ftype > 2 and self.ftype <= 4):
                self.child_func1 = RandomFunction(min_level - 1,max_level - 1)
                self.child_func2 = RandomFunction(min_level - 1,max_level - 1)
            if (self.ftype > 4):
                self.child_func = RandomFunction(min_level - 1, max_level -1)
        else:
            self.ftype = random.randint(1,2)
    
    def evaluate(self,x,y):
        x = float(x)
        y = float(y)
        if (self.ftype == 1):
            return x
        if (self.ftype == 2):
            return y
        if (self.ftype == 3):
            return self.child_func1.evaluate(x,y)*self.child_func2.evaluate(x,y)
        if (self.ftype == 4):
            return (self.child_func1.evaluate(x,y)+self.child_func2.evaluate(x,y))/2.    
        if (self.ftype == 5):
            return math.sin(math.pi*self.child_func.evaluate(x,y))
        if (self.ftype == 6):
            return math.cos(math.pi*self.child_func.evaluate(x,y))

redChannel = RandomFunction()
greenChannel = RandomFunction()
blueChannel = RandomFunction()
im = Image.new("RGB",(300,300),"white")
pix = im.load()
for i in range(im.size[0]):
    for j in range(im.size[1]):
        x = 2*i/float(im.size[0])-1
        y = 2*j/float(im.size[1])-1
        # print redChannel.evaluate(x, y)
        pix[i,j] = (int(127.5*redChannel.evaluate(x, y)+127.5),int(127.5*greenChannel.evaluate(x, y)+127.5),int(127.5*blueChannel.evaluate(x, y)+127.5))
im.save("test.jpg")