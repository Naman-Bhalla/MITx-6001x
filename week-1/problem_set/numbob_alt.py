#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 00:53:18 2016

@author: naman
"""

#==============================================================================
# Assume s is a string of lower case characters.
# 
# Write a program that prints the number of times the string 'bob' occurs in s. 
# For example, if s = 'azcbobobegghakl', then your program should print
# 
# Number of times bob occurs is: 2
#==============================================================================

#==============================================================================
# Additional Comment by me :-
# Though this code looks better, but the numbob.py is much more efficient in my
# opinion as it doesn't have to calculate all 3 (num, num + 1 and num +2) everytime.
#==============================================================================

numbob = 0

for num in range(len(s) - 2):
    if (s[num] + s[num + 1] + s[num + 2]) == 'bob':
        numbob += 1
        
print("Number of times bob occurs is: " + str(numbob))