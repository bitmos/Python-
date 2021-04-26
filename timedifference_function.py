# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 11:39:31 2021

@author: SHRAVAN
"""

def timedifference(a,b):
    t1=int((a[0]*60)+a[1])
    t2=int(b[0]*60+b[1])
    if (t1==t2):
        return print('Both the time are same')
    else:
        if t1>t2 and t1>720:
            t2=t2+720
            diff=t2-t1
        else :
            diff=t1-t2
    
        
    return diff
       
       
       
   
        
        
    
        
    
