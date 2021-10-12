# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 16:14:57 2021

@author: Administrator
"""

import numpy as np
def jc(k):
    d = 1
    for a in range(k):
        d = d*(a+1)
    return d
#杨辉三角第一行不是第0行    
def Pascal_triangle(k):
    k = k-1
    if (k < 0):
        print('error：line number must bigger than 0')
    else:
        tri = []
        for a in range(k+1):
            b = jc(k)/jc(k-a)/jc(a)
            tri.append(int(b))
        return tri
        print(tri)

# #第一行是第0行    
# def Pascal_triangle(k):
#     tri = []
#     for a in range(k+1):
#         b = jc(k)/jc(k-a)/jc(a)
#         tri.append(int(b))
#     return tri