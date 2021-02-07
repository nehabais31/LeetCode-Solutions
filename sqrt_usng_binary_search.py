# -*- coding: utf-8 -*-
"""
Finding the square root using Binary Search

Time Complexity: O(log n)
"""


x = 4

low = 0 
high = x + 1

while low < high:
    mid = low + (high - low) // 2
    if mid * mid > x:
        high = mid
    else:
        low = mid + 1
        
print( low -1   )     
        