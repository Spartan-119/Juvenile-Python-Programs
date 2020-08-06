#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 12:50:11 2020

@author: abin
"""

''' FACTORIAL OF A NUMBER USING RECURSION '''
def fact(n):
    if not isinstance(n, int):
        print("Please enter a valid integer value")
    elif n < 0:
        return None
    elif n == 0 or n == 1:
        return 1
    else:
        return n * fact(n-1)

print(fact(5.2))