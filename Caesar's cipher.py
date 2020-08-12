#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Caesar's cipher

Created on Wed Aug 12 09:38:59 2020

@author: abin
"""

def encrypt(string, shift):
    cipher = ""
    for char in string:
        if char == " ":
            cipher = cipher + char
        elif char.isupper():
            cipher = cipher + chr((ord(char) + shift - 65)%26 + 65)
        else:
            cipher = cipher + chr((ord(char) + shift - 97)%26 +97)
    
    return cipher

word = input("Enter a string here: ")
rotation = int(input("Enter the rotation of encryption: "))

encrypted_word = encrypt(word, rotation)

print("Encrpted word is: ", encrypted_word)
