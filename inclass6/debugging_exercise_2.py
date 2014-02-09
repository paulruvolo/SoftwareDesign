# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 17:52:54 2014

@author: pruvolo
"""

def factorial(n):
    retval = 1
    for i in range(n):
        retval *= i
    return retval

if __name__ == '__main__':
    print factorial(5)