# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 18:33:21 2026

@author: HP
"""

def group_anagrams(signatures):
    # Dictionary to store groups of anagrams
    # The sorted characters of a word are used as the key
    anagram_groups = {}
    for word in signatures:
        # Sort the characters to create a common key
        key = ''.join(sorted(word))
        # If this key is not present, create a new group
        if key not in anagram_groups:
            anagram_groups[key] = []
        # Add the original word to its anagram group
        anagram_groups[key].append(word)
    # Return all the groups
    return list(anagram_groups.values())
# Read strings from the user
# Enter strings separated by spaces
signatures = input().split()
# Group the anagrams and display the result
print(group_anagrams(signatures))