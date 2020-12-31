# -*- coding: utf-8 -*-
"""
Given an array of integers nums and an integer target
return indices of the two numbers 
such that they add up to target
"""

class Solution:
    def twoSum(self, nums, target):
        '''
        Parameters
        ----------
        nums : TYPE - List[int]
        target : TYPE- int

        Returns
        -------
        result: List[int]
        '''
        result = []
        
        for i in range(len(nums)-1):
            for j in range(len(nums)-1):
                if nums[i] + nums[j+1] == target:
                   result.append(i)
                   result.append(j+1)
                   break
        
        return result               
        
        
nums = [2,7,11,15]
target = 17
solve = Solution()
res = solve.twoSum(nums, target) 
print(res)                  