# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 17:52:54 2014

@author: pruvolo
"""

def cumulative_sum(L):
    for i in range(len(L)):
        L[i] = L[i-1] + L[i]
    return L

if __name__ == '__main__':
    print cumulative_sum([1, 2, 3])