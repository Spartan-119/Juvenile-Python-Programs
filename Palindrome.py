#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 20:05:12 2020

@author: abin
"""

''' Method 1 using an extra variable '''

'''
word = "malayalam"
x = ""
for i in range(0, len(word)):
    x = word[i] + x
    print(x)

if (x == word):
    print("Yes its a Palindrome")
else:
    print("No, its NOT a Palindrome")
'''
    
''' Method 2 using slicing '''

'''
word = "malayalaam"
reversed_word = word[:: -1]
if word == reversed_word:
    print("Yes, its a palindrome")
else:
    print("No, its NOT a palindrome")
'''

''' Method 3 using RECURSION '''
def reverse_string(string):
    # base case
    if len(string) == 0:
        return string
    else:
        return reverse_string()