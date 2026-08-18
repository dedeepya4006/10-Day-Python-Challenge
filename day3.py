# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 18:54:05 2026

@author: HP
"""

def equilibrium_index(altitudes):
    # Calculate the total sum only once
    total = sum(altitudes)
    # Stores the sum of elements to the left
    left_sum = 0
    # Check each index
    for i in range(len(altitudes)):
        # Remove current element from total
        # What remains is the right-side sum
        right_sum = total - left_sum - altitudes[i]
        # Check whether left sum equals right sum
        if left_sum == right_sum:
            return i
        # Add current element to the left sum
        left_sum += altitudes[i]
    # No equilibrium index was found
    return -1
# Sample input
altitudes = [1, 7, 3, 6, 5, 6]
# Find the first equilibrium index
index = equilibrium_index(altitudes)
print("Equilibrium Index:", index)