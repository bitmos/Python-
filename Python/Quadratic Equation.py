# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 23:17:38 2021
quadratic equation
@author: SHRAVAN
"""
import cmath
a=float(input('Enter co-efficent a:'))
b=float(input('Enter co-efficent b:'))
c=float(input('Enter co-efficent c:'))

d= (b**2)-(4*a*c)
sol1=(-b+cmath.sqrt(d))/(2*a)
sol2=(-b-cmath.sqrt(d))/(2*a)
print('Solutions of quadratic equations are: '+ str(sol1)+' and '+str(sol2))