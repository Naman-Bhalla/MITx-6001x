#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 23:25:40 2016

@author: naman
"""

#==============================================================================
# Write a for loop that sums the values 1 through end, inclusive. end is a 
# variable that we define for you. So, for example, if we define end to be 6, 
# your code should print out the result:
# 
# 21
# which is 1 + 2 + 3 + 4 + 5 + 6.
#==============================================================================

mySum = 0

for n in range(0,end + 1):
    mySum += n
    
print(mySum)

#==============================================================================
# Staff Solution :-
# # Here is one of a few ways to solve this problem:
# total = 0
# for next in range(1, end+1):
#     total += next
# print(total)
# 
# # Here is another:
# total = end
# for next in range(end):
#     total += next
# print(total)
#==============================================================================
