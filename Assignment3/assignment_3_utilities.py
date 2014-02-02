# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 22:42:54 2014

@author: pruvolo
"""



def collapse(L):
    output = ""      # This is our initial output string
    for s in L:      # for each string in the list...
        output = output + s    #... construct a new output string 
    return output    # ... and return the final output string
