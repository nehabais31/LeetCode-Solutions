# -*- coding: utf-8 -*-
"""
Find square root and return the integer value if res is float
"""

x = 8
print(x**0.5)

class Solution(object):
    def mySqrt(self, x):
        l, r = 0, x
        while l <= r:
            mid = l + (r-l)//2
            if mid * mid <= x < (mid+1)*(mid+1):
                return mid
            elif x < mid * mid:
                r = mid - 1
            else:
                l = mid + 1
                
s = Solution()
print(s.mySqrt(8))