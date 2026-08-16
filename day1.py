# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 20:12:11 2026

@author: HP
"""

# Input list representing battery usage steps
battery = [1, 1, 1, 1, 0, 1, 1]

# Variable to store total battery used
total = 0

# Count consecutive 1s
consecutive = 0

# Process each step
for step in battery:

    if step == 1:
        consecutive += 1

        # Normal step costs 2 units
        if consecutive < 4:
            total += 2

        # 4th consecutive step costs double due to overheating
        else:
            total += 4

    else:
        # 0 breaks the consecutive sequence
        consecutive = 0

# Display the final battery usage
print("Total Battery Used", total, "units")