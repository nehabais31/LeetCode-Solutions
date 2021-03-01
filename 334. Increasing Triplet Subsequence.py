# -*- coding: utf-8 -*-
"""
Given an integer array nums, 
return true if there exists a triple of indices (i, j, k) 
such that i < j < k and nums[i] < nums[j] < nums[k]. 
If no such indices exists, return false.

 
"""


class Solution:
    def increasingTriplet(self, nums):
        first = second = float('inf')
        
        for i in nums:
            if i <= first :
                first = i
            elif i <= second:
                second = i
            else:
                return True
        return False
    
sol = Solution()
print(sol.increasingTriplet([20,100,10,12,5,13]))
    