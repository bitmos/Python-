# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 11:20:28 2021

@author: SHRAVAN
"""

def time(t):
    if 6.00<=t<12.00:
        print('Good Morning')
    elif 12.00<=t<16.00:
        print('Good Afternoon')
    elif 16.00<=t<17.00:
        print('Good Evening')
    else:
        print('Good night')
    return 0