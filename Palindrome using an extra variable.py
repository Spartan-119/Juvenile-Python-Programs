#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Palindrome problem using an extra variable

Created on Tue Aug 11 20:05:12 2020

@author: abin
"""

word = "malayalam"
x = ""
for i in range(0, len(word)):
    x = word[i] + x
    #print(x)

if (x == word):
    print("Yes its a Palindrome")
else:
    print("No, its NOT a Palindrome")
