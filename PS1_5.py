# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 17:07:22 2021

@author: Administrator
"""

def Find_expression(num):
    #输出3**8个数组情况
    #迭代（计算排列组合）：https://code-examples.net/zh-CN/q/197e4
    import itertools
    he = list(itertools.product([1,-1,0], repeat=8))   
    #替换数组内符号
    strhe = []
    for i in range(len(he)):
        #print(he[i])
        he1 = ['+' if j == 1 else j for j in he[i]]
        he1 = ['-' if j == -1 else j for j in he1]
        he1 = ['' if j == 0 else j for j in he1]
        #print(he1)
        strhe.append(he1)   
    #拼接公式
    #合并http://c.biancheng.net/view/4277.html
    a = ['1','2','3','4','5','6','7','8','9']
    joi = []
    for i in range(len(strhe)):
        for j in range(len(strhe[i])):
            a[j+1] = strhe[i][j].join(a[j:j+2])
        joi.append(a[j+1])
        a = ['1','2','3','4','5','6','7','8','9']           
    #计算公式
    #计算str：https://blog.csdn.net/weixin_43097301/article/details/82933099
    res = []
    for i in range(len(joi)):
        res.append(eval(joi[i]))
    #查找结果返回公式
    #索引enumerate():https://m.jingyanlib.com/resultpage?id=CsFJGPp1X_PdaFvnJN-oLg
    count = 0
    for index, value in enumerate(res):
        if (value == num):
            print(joi[index], '=', num, sep ='')
            count +=1
    return count

x = []
Total_solutions = []
for i in range(100):
    x.append(i+1)
    Total_solutions.append(Find_expression(i+1))
# import numpy as np  
# import matplotlib.mlab as mlab  
import matplotlib.pyplot as plt 
fig = plt.figure()
plt.bar(x,Total_solutions,0.4,color="green")
plt.xlabel("number")
plt.ylabel("number of chart")
plt.title("bar chart of # of expression")
plt.show()  
# plt.savefig("barChart.jpg")
Max = max(Total_solutions)
for index, value in enumerate(Total_solutions):
   if (value == Max):
      print(index+1)
    
