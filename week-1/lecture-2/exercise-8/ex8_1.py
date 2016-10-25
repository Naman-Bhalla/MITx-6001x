#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 23:08:32 2016

@author: naman
"""

#==============================================================================
# Convert the following into code that uses a while loop.
# 
# print 2
# prints 4
# prints 6
# prints 8
# prints 10
# prints Goodbye!
#==============================================================================

n = 2

while n <= 10 :
    print(n)
    n += 2
print("Goodbye!")

#==============================================================================
# Staff Solution :-
# # There are many ways to solve this problem! Here is one:
# num = 2
# while num < 11:
#     print(num)
#     num += 2
# print("Goodbye!")
# 
# # Here is another:
# num = 2
# while num <= 10:
#     print(num)
#     num += 2
# print("Goodbye!")
# 
# # And another:
# num = 0
# while True:
#     num += 2
#     print(num)
#     if num >= 10:
#         print("Goodbye!")
#         break
# 
# # And one more:
# num = 1
# while num <= 10:
#     if num % 2 == 0:
#         print(num)
#     num += 1
# print("Goodbye!")
# 
# # There are always many, many different ways to solve a programming
# # problem. Here are just four examples and surely there are quite
# # a few more.
#==============================================================================
