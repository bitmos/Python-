# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 21:53:28 2021
Area of a triangle
@author: SHRAVAN
"""
side1=float(input('Enter side 1 value:'))
side2=float(input('Enter side 2 value:'))
side3=float(input('Enter side 3 value:'))

semiperimeter = (side1+side2+side3)/2
area= (semiperimeter*(semiperimeter-side1)*(semiperimeter-side2)*(semiperimeter-side3))**0.5
print('Area of triangle is:',area)