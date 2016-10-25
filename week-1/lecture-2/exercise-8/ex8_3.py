#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 23:14:01 2016

@author: naman
"""

#==============================================================================
# Write a while loop that sums the values 1 through end, inclusive. end is a 
# variable that we define for you. So, for example, if we define end to be 6, 
# your code should print out the result:
# 
# 21
# which is 1 + 2 + 3 + 4 + 5 + 6.
# 
# For problems such as these, do not include input statements or define variables 
# we will provide for you. Our automating testing will provide values so write 
# your code in the following box assuming these variables are already defined.
#==============================================================================

n = 0
mySum = 0

while n <= end:
    mySum += n
    n += 1
    
print(mySum)

#==============================================================================
# Staff Solution :-
# # Here is one of a few ways to solve this problem:
# total = 0
# current = 1
# while current <= end:
#     total += current
#     current += 1
# 
# print(total)
#==============================================================================
