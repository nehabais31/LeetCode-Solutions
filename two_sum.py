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
            for j in range(i+1, len(nums)-1):
                if nums[i] + nums[j] == target:
                   result.append(i)
                   result.append(j)
                   break
        
        return result               
        
        
nums = [2,5,5,11]
target = 10
solve = Solution()
res = solve.twoSum(nums, target) 
print(res)                  