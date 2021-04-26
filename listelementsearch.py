# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 22:12:58 2021

@author: SHRAVAN
"""

import sys

a=list()
n=int(input("enter the list size:"))
for i in range(0,n):
    a.append(int(input('Enter the element:')))
key = int(input('Enter the key to be searched:'))

"""flag=0
j=0
for num in a:
    if(key==num):
        j+=1
        flag=1
        break
    else:
        j+=1
    
    
if(flag):
    print('Key is present at', j)
else:
    print("Key is not present")"""
    
    
    
    
    
for n in range(len(a)):
    if(a[n]==key):
        print("Element is present at :",n+1)
        sys.exit()
print("Key is not found")