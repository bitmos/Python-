# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 13:22:26 2021

@author: SHRAVAN
"""
import fibonacci_function
number=int(input('Enter number'))

print("Fibonacci sequence in recursion method:")
for i in range(number):
    print(fibonacci_function.recur_fibo(i))
    

print("Fibonacci sequence in iterative method:")
for i in range(number):
    print(fibonacci_function.fibonacci(i))
