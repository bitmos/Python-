# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 10:36:53 2021

@author: SHRAVAN
"""

import Sum_of_squares_functions
number=int(input('Enter the n number: '))
Sum=Sum_of_squares_functions.sumofsquaresiterativemethod(number)
print('Sum of squares of n number in iterative method is: ',Sum)
result=Sum_of_squares_functions.sumofsquaresrecursivemethod(number)
print('Sum of squares of n number in recursive method is: ',result)
resultofformula=(number*(number+1)*((2*number)+1))/6
print('Sum of squares of n number using formula is: ',resultofformula)

