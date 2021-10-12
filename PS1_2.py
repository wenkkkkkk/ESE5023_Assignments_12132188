# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 14:43:58 2021

@author: Administrator
"""

#reference:1. https://blog.csdn.net/qq_43287650/article/details/82860938                
#          2. https://www.cnblogs.com/Yanjy-OnlyOne/p/11298253.html
import numpy as np
M1 = np.random.randint(0, 51, [5, 10])
M2 = np.random.randint(0, 51, [10, 5])
# M3 = np.zeros((M1.shape[0],M2.shape[1]))
def Matrix_multip(M1, M2):
    if(M1.shape[1] == M2.shape[0]):
        M3 = np.zeros((M1.shape[0],M2.shape[1]))
        i = 0
        sum = 0
        M3 = np.zeros((M1.shape[0],M2.shape[1]))
        for x in range(M1.shape[0]):
            for y in range(M2.shape[1]):
                for i in range(M1.shape[1]):
                    k = M1[x,i]*M2[i,y]
                    sum = sum + k
                M3[x,y] = sum
                i = 0
                sum = 0
                
        return M3
    else:
        print('Dimension Error')
M3 = Matrix_multip(M1, M2)
# test
M1
M2
M3 
M4 = np.dot(M1,M2)
M3 == M4 