#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 00:20:50 2016

@author: naman
"""

#==============================================================================
# Here is some code:
# 
# Code Sample
# 
# iteration = 0
# count = 0
# while iteration < 5:
#     for letter in "hello, world":
#         count += 1
#     print("Iteration " + str(iteration) + "; count is: " + str(count))
#     iteration += 1 
#     
# We wish to re-write the above code, but instead of nesting a for loop inside a 
# while loop, we want to nest a while loop inside a for loop. Which of the 
# following loops gives the same output as the Code Sample?
# 
# Try to answer the following questions by just reading the code. Reading code 
# is a very good skill to have (and will help you both in your programming career 
# and on your exams!). It is okay to check your answers that you obtain from 
# just reading the code, then in your interpreter run the code for the ones you 
# got wrong on your first attempt.
#==============================================================================

#==============================================================================
# Test 1
# 
# for iteration in range(5):
#     count = 0
#     while True:
#         for letter in "hello, world":
#             count += 1
#         print("Iteration " + str(iteration) + "; count is: " + str(count))
# 
# Ans :-
# No, Test 1 does not give the same output as the Code Sample
# 
# Test 2
# 
# for iteration in range(5):
#     count = 0
#     while True:
#         for letter in "hello, world":
#             count += 1
#         print("Iteration " + str(iteration) + "; count is: " + str(count))
#         break
# 
# Ans :-
# No, Test 2 does not give the same output as the Code Sample
# 
# Test 3
# 
# count = 0
# phrase = "hello, world"
# for iteration in range(5):
#     index = 0
#     while index < len(phrase):
#         count += 1
#         index += 1
#     print("Iteration " + str(iteration) + "; count is: " + str(count))
# 
# Ans :-
# Yes, Test 3 gives the same output as the Code Sample
# 
# Test 4
# 
# count = 0
# phrase = "hello, world"
# for iteration in range(5):
#     while True:
#         count += len(phrase)
#         break
#     print("Iteration " + str(iteration) + "; count is: " + str(count))
# 
# Ans :-
# Yes, Test 4 gives the same output as the Code Sample
# 
# Test 5
# 
# count = 0
# phrase = "hello, world"
# for iteration in range(5):
#     count += len(phrase)
#     print("Iteration " + str(iteration) + "; count is: " + str(count))
# 
# Ans :-
# Yes, Test 5 gives the same output as the Code Sample
#==============================================================================
