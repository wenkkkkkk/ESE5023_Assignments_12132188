# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 16:44:44 2021

@author: Administrator
"""

def Least_moves(k):
    i = 0
    while k >1:
        if k%2 == 1:
            k = k - 1
            i = i + 1
        else:
            k = k / 2
            i = i + 1
    print(i)
    return i
    
 


#test
Least_moves(2)
Least_moves(5)
