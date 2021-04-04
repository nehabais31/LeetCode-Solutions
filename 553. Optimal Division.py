# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 12:10:08 2021

@author: Home
"""


class Solution:
    def optimalDivision(self, nums):
        if len(nums) == 1:
            return str(nums[0])
        if len(nums) == 2:
            return str(nums[0])  + '/' + str(nums[1])
        
        res = str(nums[0]) + '/(' + str(nums[1])
        for i in range(2, len(nums)):
            res += '/' + str(nums[i])

        return res + ')' 
          
    
sol = Solution()
print(sol.optimalDivision([1000,100,10,2]))    