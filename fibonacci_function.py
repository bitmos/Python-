# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 22:56:53 2021

@author: SHRAVAN
"""

def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))
    
   
def fibonacci(n):
    a = 0
    b = 1
     
    if n < 0:
        print("Incorrect input")
         
    elif n == 0:
        return 0
      
    elif n == 1:
        return b
    else:
        for i in range(1, n):
            c = a + b
            a = b
            b = c
        return b