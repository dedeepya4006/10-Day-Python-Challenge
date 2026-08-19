# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 18:13:57 2026

@author: HP
"""
def min_subarray_length(target, nums):
    left = 0
    current_sum = 0
    min_length = len(nums) + 1
    # Sliding window
    for right in range(len(nums)):
        current_sum += nums[right]
        # Shrink window when target is reached
        while current_sum >= target:
            length = right - left + 1
            # Store smallest length
            if length < min_length:
                min_length = length
            current_sum -= nums[left]
            left += 1
    # No valid subarray
    if min_length == len(nums) + 1:
        return 0
    return min_length
# Get input
target = int(input())
nums = list(map(int, input().split()))
# Print result
print(min_subarray_length(target, nums))