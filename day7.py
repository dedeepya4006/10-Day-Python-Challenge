# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 20:04:41 2026

@author: HP
"""

def max_water_container(height):
    left = 0
    right = len(height) - 1
    max_area = 0
    while left < right:
        # Calculate width
        width = right - left
        # Container height is the shorter line
        current_height = min(height[left], height[right])
        # Calculate area
        area = current_height * width
        # Update maximum area
        max_area = max(max_area, area)
        # Move the pointer at the shorter line
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area
# Accepting input
height = list(map(int, input("Enter heights: ").split()))
# Calculate and display maximum water
result = max_water_container(height)
print("Maximum water:", result)