#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exception handling in Python

Created on Wed Sep  2 10:45:21 2020

@author: abin
"""

# KeyboardInterrupt exception
try:
    inp = input()
    print("Press Ctrl+C  or interrupt the Kernel")
except KeyboardInterrupt:
    print("KeyboardInterrupt Exception caught")
else:
    print("No exception occured")
    
# Zero division error
try:
    a = 100/0
    print(a)
except ZeroDivisionError:
    print("Cannot divide anything by 0")
else:
    print("No exception occured")

# Overflow error
try:
    import math
    print(math.exp(1000))
except OverflowError:
    print("Overflow error caught")
else:
    print("No exception occured")

# Assertion Error
try:
    a = 100
    b = "Hello friend"
    assert a == b
except AssertionError:
    print("Assertion error caught")
else:
    print("No exception occured")
