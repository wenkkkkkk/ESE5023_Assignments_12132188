# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 14:24:02 2021

@author: Administrator
"""
def Print_values(a, b, c):
    if(a > b):
        if(b > c):
            #a>b>c
            print(str(a) +', '+str(b) +', '+str(c))
        elif(a > c):
            #a>b, c>b, a>c
            print(str(a) +', '+str(c) +', '+str(b))
        else:
            #a>b, c>b, c>a
            print(str(c) +', '+str(a) +', '+str(b))
    elif(b > c):
        # #b>a, b>c
        # if (a > c):
        #     #a>c
        #     print(str(b) +', '+str(a) +', '+str(c))
        # else:
        #     #a<c
        #     print(str(b) +', '+str(c) +', '+str(a))
        print()
    else:
        #b>a, c>b
        print(str(c) +', '+str(b) +', '+str(a))
    
    
import random
a = random.random();
b = random.random();
c = random.random();
# c = 4
# a = 2
# b = 3
Print_values(a, b, c)

