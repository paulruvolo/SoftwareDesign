# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 17:52:54 2014

@author: pruvolo
"""

def get_doubles_then_triples(L):
    """ Returns a new list containing the original list with each element
    	multiplied by 2 concatenated with the original list with each element
	multiplied by 3 """
    return get_multiple_of_list(L,2) + get_multiple_of_list(L,3)

def get_multiple_of_list(L,n):
    for i in range(len(L)):
        L[i] *= n
    return L

if __name__ == '__main__':
    print get_doubles_then_triples([1, 4, 8])
