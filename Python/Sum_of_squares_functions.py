# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 10:35:00 2021

@author: SHRAVAN
"""

def sumofsquaresiterativemethod(n):
    sum=0
    for i in range(0,n+1):
        sum+=(i*i)
    return sum
def sumofsquaresrecursivemethod(n):
    
   if n==1:
       return 1 
   else:
       return sumofsquaresrecursivemethod(n-1)+ (n*n)
