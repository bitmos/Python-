# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 22:59:04 2021

@author: SHRAVAN
"""
import sys
a=tuple()
al=list(a)
n=int(input("enter the tuple size:"))
for i in range(0,n):
    al.append(int(input('Enter the element:')))
    
a=tuple(al)
print(a)
key = int(input('Enter the key to be searched:'))
al=list(a)  
for n in range(len(al)):
    if(al[n]==key):
        print("Element is present at :",n+1)
        sys.exit()
print("Key is not found")