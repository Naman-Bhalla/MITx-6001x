#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 22:49:39 2016

@author: naman
"""

#==============================================================================
# Below are some short Python programs. For each program, answer the associated 
# question.
# 
# Try to answer the questions without running the code. Check your answers, then 
# run the code for the ones you get wrong.
# 
# This question is going to ask you what some simple loops print out. If you're asked
#  what code like this prints:
# 
# num = 5
# if num > 2:
#     print(num)
#     num -= 1
# print(num)
# 
# write what it prints out, separating what appears on a new line by a comma and 
# a space. So the answer for the above code would be:
# 
# 5, 4
# 
# If a given loop will not terminate, write the phrase 'infinite loop' 
# (no quotes) in the box. Recall that you can stop an infinite loop in your 
# program by typing CTRL+c in the console.
#==============================================================================

#==============================================================================
# 1.)
# num = 0
# while num <= 5:
#     print(num)
#     num += 1
# 
# print("Outside of loop")
# print(num) 
# 
# Ans.
# 0, 1, 2, 3, 4, 5, Outside of loop, 6
# 
# 2.)
# numberOfLoops = 0
# numberOfApples = 2
# while numberOfLoops < 10:
#     numberOfApples *= 2
#     numberOfApples += numberOfLoops
#     numberOfLoops -= 1
# print("Number of apples: " + str(numberOfApples))
# 
# Ans.
# infinite loop
# 
# 3.)
# num = 10
# while num > 3:
#     num -= 1
#     print(num) 
#     
# Ans.
# 9, 8, 7, 6, 5, 4, 3
# 
# 4.)
# num = 10
# while True:
#     if num < 7:
#         print('Breaking out of loop')
#         break
#     print(num)
#     num -= 1
# print('Outside of loop')
# 
# Ans :-
# 10, 9, 8, 7, Breaking out of loop, Outside of loop
# 
# 5.)
# num = 100
# while not False:
#     if num < 0:
#         break
# print('num is: ' + str(num)) 
# 
# Ans.
# infinite loop
#==============================================================================

#==============================================================================
# Staff Explanation
# 
# For the last exercise, the code never breaks. You enter the loop with num value 
# of 100 and since the value of num never changes, num < 0 is never True so break 
# is never executed. Therefore you are stuck in an infinite loop.
#==============================================================================
