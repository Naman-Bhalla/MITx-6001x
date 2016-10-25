#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 00:28:51 2016

@author: naman
"""
#==============================================================================
# Assume s is a string of lower case characters.
# 
# Write a program that counts up the number of vowels contained in the string s. 
# Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, 
# if s = 'azcbobobegghakl', your program should print:
# 
# Number of vowels: 5
#==============================================================================

numVowels = 0
for letter in s :
    if letter =='a' or letter == 'e' or letter == 'i' \
    or letter == 'o' or letter == 'u':
        numVowels += 1
print("Number of vowels: " + str(numVowels))