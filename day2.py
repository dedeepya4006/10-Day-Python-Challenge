# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 18:42:18 2026

@author: HP
"""

def compress(s):
    result = ""
    count = 1
    # Go through the string from the second character
    for i in range(1, len(s) + 1):
        # Continue counting if the character is the same
        if i < len(s) and s[i] == s[i - 1]:
            count += 1
        else:
            # Add the character
            result += s[i - 1]
            # If character appears more than once, add its count
            if count > 1:
                # Store the count digits temporarily
                digits = []
                n = count
                # Extract digits without using str()
                while n > 0:
                    digits.append(n % 10)
                    n = n // 10
                # Add digits in the correct order
                for j in range(len(digits) - 1, -1, -1):
                    result += chr(digits[j] + 48)
            # Reset count for the next character
            count = 1
    return result
# Input
s = input()
# Print the compressed string
print(compress(s))