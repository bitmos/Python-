# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 21:03:11 2021

@author: SHRAVAN
"""

principle=float(input('Enter the principle amount: '))
rate=float(input('Enter the rate of intrest: '))
time=float(input('Enter the time period: '))

def simpleintrest(principle,rate,time):
    si=(principle*rate*time)/100
    return si

print('Simple Intrest is: ',simpleintrest(principle, rate, time))