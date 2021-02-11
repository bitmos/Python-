# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 22:30:57 2021

@author: SHRAVAN
"""

import BMI_function
h=float(input("Enter height in feet: "))
height=h/3.2808
weight=float(input('Enter weight in kg: '))
a=BMI_function.BMIfunction(height,weight)

if a<18.5:
    print('Underweight')
elif 18.5<=a<25:
    print('Normal')
elif 25<=a<30:
    print('Overweight')
else:
    print('Obese')