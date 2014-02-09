# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 17:52:54 2014

@author: pruvolo
"""

def get_primes(n):
    retval = []
    isPrime = True

    for i in range(1,n+1):
        for j in range(2,i):
            if i % j == 0:
                isPrime = False
        if isPrime:
            retval.append(i)
    return retval


if __name__ == '__main__':
    print get_primes(7)