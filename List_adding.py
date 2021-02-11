# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 16:36:10 2021

@author: SHRAVAN
"""

List = []
def listreading(n):
    for i in range(0, n):
        print("Enter number at location", i, ":")
        item = int(input())
        List.append(item)
    return List

    
def adding(n):
    sum=0
    for i in range(0,n):
        sum+=List[i]
    return sum
        
    