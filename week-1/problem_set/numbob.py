#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 00:47:57 2016

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

numbob = 0

for num in range(len(s) - 2):
    if s[num] == 'b':
        if s[num + 1] == 'o':
            if s[num + 2] == 'b':
                numbob += 1
                
print("Number of times bob occurs is: " + str(numbob))