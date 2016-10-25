#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 19:06:17 2016

@author: naman
"""

#==============================================================================
# For each of the following expressions, indicate the value returned, or if the 
# evaluation would lead to an error, write the word 'error' (note this is a word, 
# not a string, no quotes). While you could simply type these expressions into an 
# IDE, we encourage you to answer them directly since this will help reinforce 
# your understanding of basic Python expressions.
# 
# For decimal answers, give the full result, or at least four decimal places of 
# accuracy (whichever is shortest).
# 
# Floating point errors
# Decimal numbers cannot be stored exactly in the computer because the computer 
# does not have an infiite amount of memory. So decimal numbers are rounded when 
# stored. When you do calculations with these numbers, your final result will be 
# different than the actual result. For exmaple, you may get something like 
# 5.0000000044 instead of 5.0. This is called floating-point rounding error.
# 
# 1.) 6 + 12 -3
# 
# Ans :-
# 15
# 
# 2.) 2 * 3.0
# 
# Ans :-
# 6.0
# 
# 3.) - - 4
# 
# Ans :-
# 4
# 
# 4.) 10/3
# 
# Ans :-
# 3.3333
# 
# 5.) 10.0/3.0
# 
# Ans :-
# 3.3333
# 
# 6.) (2 + 3) * 4
# 
# Ans :-
# 20
# 
# 7.) 2 + 3 * 4
# 
# Ans :-
# 14
# 
# 8.) 2**3 + 1
# 
# Ans :-
# 9
# 
# 9.) 2.1 ** 2.0
# 
# Ans :-
# 4.4100
# 
# 10.) 2.2 * 3.0
# 
# Ans :-
# 6.6
# 
# Staff Explanation:
# 
# For the last problem (10), typing the expression into your Python interpreter 
# may give a result that is not exact. For example, 6.6000000000000005 instead of 
# 6.6. This is because computers have difficulty storing fractions exactly in 
# binary. So when performing calculations, numbers first get converted to binary 
# then the calculation is performed and the result converted back into decimal. 
# However, fractions cannot be stored exactly in binary (for example, there is no 
# way to store 0.33333 repeating exactly) so we introduce these small rounding 
# errors that propagate until the final answer.
#==============================================================================
