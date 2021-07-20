# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 21:12:54 2021

@author: SHRAVAN
"""

number=int(input('Enter the number: '))

if number>1:
    for i in range(2,number):
        if(number%i)==0:
            print('It is not a prime number')
            break
    else:
        print('It is a prime number')
            
else:
    print('It is not a prime number')