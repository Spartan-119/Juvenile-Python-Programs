#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test on Lists

Created on Wed Aug 19 11:19:31 2020

@author: Abin
"""

# 1. Write a Python program to sum all the items in a list.
t = [1, 3, 5, 6, 2]
print(sum(t))

# 2. Write a Python program to multiplies all the items in a list.
result = 1
for i in range(len(t)):
    result = result * t[i]
print(result)

# 3. Write a Python program to get the largest number from a list.
sorted_list = sorted(t)
print(sorted_list[len(sorted_list) - 1])

# 4. Write a Python program to get the smallest number from a list.
print(sorted_list[0])

# 5. Write a Python program to count the number of items where the item 
# length is 4 or     more, and is also a palindrome.
# Sample List : ['abba', 'malayalam', 'aba', '1221', ‘123’, ‘98703’]
# Expected Result : 3
sample_list = ['abba', 'malayalam', 'aba', '1221', '123', '98703']

def isPalindrome(item):
    if str(item) == str(item)[::-1]:
        return True
    else:
        return False

def check_greater_than_three(item):
    if len(str(item)) > 3:
        return True
    else:
        return  False

# start a counter or accumulator
count = 0
for i in range(len(sample_list)):
    if isPalindrome(sample_list[i]) and check_greater_than_three(sample_list[i]):
        count += 1
        
print("Result is: ", count)

# 6. Write a Python program to check a list is empty or not.
if t == []:
    print("Its an empty list")
else:
    print("Its not an empty list")

# 7. Write a Python program to clone or copy a list.

cloned_list = []
for i in range(len(sample_list)):
    cloned_list.append(sample_list[i])
print(cloned_list)

# 8. Write a Python program to print a specified list after 
# removing the 0th, 4th and 5th elements.
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Expected Output : ['Green', 'White', 'Black']

new_sample_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
output_list = []

def remove_stated_items(t):
    for i in range(len(t)):
        if i == 0 or i == 4 or i == 5:
            pass
        else:
            output_list.append(t[i])
    return output_list

print(remove_stated_items(new_sample_list))
