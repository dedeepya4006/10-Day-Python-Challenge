# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 21:14:09 2026

@author: HP
"""

def peak_horizon_tracker(readings):
    # Store the number of days until a higher reading
    result = [0] * len(readings)
    # Stack stores indices waiting for a higher reading
    stack = []
    for i in range(len(readings)):
        # If current reading is higher, solve previous indices
        while stack and readings[i] > readings[stack[-1]]:
            j = stack.pop()
            # Days waited = current index - previous index
            result[j] = i - j
        # Keep current index for a future higher reading
        stack.append(i)
    return result
# Read any number of readings from the user
readings = list(map(int, input().split()))
# Display the result
print(peak_horizon_tracker(readings))