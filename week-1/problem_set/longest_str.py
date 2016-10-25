#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 01:04:02 2016

@author: naman
"""

#==============================================================================
# Assume s is a string of lower case characters.
# 
# Write a program that prints the longest substring of s in which the letters 
# occur in alphabetical order. For example, if s = 'azcbobobegghakl', then 
# your program should print
# 
# Longest substring in alphabetical order is: beggh
# In the case of ties, print the first substring. For example, if s = 'abcbcd', 
# then your program should print
# 
# Longest substring in alphabetical order is: abc
# Note: This problem may be challenging. We encourage you to work smart. If 
# you've spent more than a few hours on this problem, we suggest that you move 
# on to a different part of the course. If you have time, come back to this 
# problem after you've had a break and cleared your head.
#==============================================================================

#s = 'azcbobobegghakl'

current = s[0]
maxstr = s[0]
maxstrlen = 1

for num in range(len(s) - 1):
    if s[num + 1] >= s[num]:
        current += s[num + 1]
        if len(current) > maxstrlen: #Had we had to choose the last maximum,
            maxstrlen = len(current) #we would have used >=
            maxstr = current
    else :
        current = s[num + 1]

print("Longest substring in alphabetical order is: " + maxstr)