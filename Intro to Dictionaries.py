#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Intro to Dictionaries

Created on Mon Aug 24 18:32:05 2020

@author: abin
"""

def reverse_lookup(d, v):
    for k in d:
        if d[k] == v:
            return k
    raise LookupError
    
