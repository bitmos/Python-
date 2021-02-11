# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 20:57:32 2021

@author: SHRAVAN
"""
n=float(input('Enter the number: '))
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        fact=1
        while(n>1):
             fact*=n
             n-=1
        return fact
print('Factorial of the given number is: ', factorial(n))