# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 16:45:51 2021

@author: SHRAVAN
"""
import List_adding
n = int(input("Enter the list size : "))
print('Enter the elements of the list')
List=List_adding.listreading(n)
sum=List_adding.adding(n)
print(List,'\n',sum)