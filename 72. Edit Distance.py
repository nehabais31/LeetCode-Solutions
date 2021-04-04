# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 09:53:44 2021

@author: Home
"""

word1 = "horse"
word2 = "ros"

sorted_char_w1 = sorted(word1)
sorted_char_w2 = sorted(word2)

sorted_word1 = ''.join(sorted_char_w1)
sorted_word2 = ''.join(sorted_char_w2)

print(sorted_word1)
print(sorted_word2)

if len(sorted_word2) > len(sorted_word1):
    if sorted_word1 in sorted_word2:
        return 