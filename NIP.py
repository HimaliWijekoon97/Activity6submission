#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Python3 program for implementing  
# Newton divided difference formula  
  
def proterm(i, value, x):  
    pro = 1;  
    for j in range(i):  
        pro = pro * (value - x[j]);  
    return pro;  
  

def dividedDiffTable(x, y, n): 
  
    for i in range(1, n):  
        for j in range(n - i):  
            y[j][i] = ((y[j][i - 1] - y[j + 1][i - 1]) /
                                     (x[j] - x[i + j])); 
    return y; 
  
  
def applyFormula(value, x, y, n):  
  
    sum = y[0][0];  
  
    for i in range(1, n): 
        sum = sum + (proterm(i, value, x) * y[0][i]);  
      
    return sum;  
  
  
def printDiffTable(y, n):  
  
    for i in range(n):  
        for j in range(n - i):  
            print(round(y[i][j], 4), "\t",  
                               end = " ");  
  
        print("");  
  

  
# This code is contributed by mits 

