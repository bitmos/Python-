# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 12:34:02 2021

@author: SHRAVAN
"""

import timedifference_function
time1=input('Enter first time in HH:mm format: ')
time1=time1.split(':')
time2=input('Enter second time in HH:mm  format: ')
time2=time2.split(':')
print('Time differnece is ',timedifference_function.timedifference(time1,time2))