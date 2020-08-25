#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Intro to Dictionaries

Created on Mon Aug 24 18:32:05 2020

@author: Abin
"""
'''    
d = {"one":"ek", "two":"do", "three":"teen"}

print()

eng2spn = dict()
print("This will print an empty dictionary: ", eng2spn)
print(len(d))
print("one" in d)
print()

vals = d.values()

print(vals)
print()
'''
def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

def print_hist(h):
    for key in sorted(h):
        print(key, h[key])

verse = "The Lord is my shepherd: I shall not want."
h = histogram(verse)
print_hist(h)

# print(histogram("abinvarghese"))

# REVERSE LOOKUP
def reverse_lookup(d, v):
    for k in d:
        if d[k] == v:
            return k
    raise LookupError("Value does NOT appear in the dictionary")
