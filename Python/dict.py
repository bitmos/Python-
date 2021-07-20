# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 23:08:08 2021

@author: SHRAVAN
"""

a={}
n=int(input("enter the dict size:"))
for i in range(n):
    key=input('Enter the key:')
    value=input("Enter the value:")
    a.update({key:value})
    
print(a)


keyname = input('Enter the key to be searched:')
#for i in range(len(a)):

if keyname in a.keys():
     print('Key value is ',a[key])
        
        
    
else:print('Key is not found')