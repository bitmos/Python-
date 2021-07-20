# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 23:56:44 2021

@author: SHRAVAN
"""

def sumofnaturalnumbersiterativemethod(n):
    sum=0
    for i in range(0,n+1):
        sum+=i
    return sum
def sumofnaturalnumbersrecursivemethod(n):
    
   if n==1:
       return 1 
   else:
       return sumofnaturalnumbersrecursivemethod(n-1)+ n
       

    
