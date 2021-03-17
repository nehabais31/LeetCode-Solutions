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
        seen_nums = {}
        
        for i, n  in enumerate(nums):
            diff = target - n
            if diff in seen_nums:
                return [seen_nums[diff], i]
            else:
                seen_nums[n] = i
        return
    
# =============================================================================
#         result = []
#         
#         for i in range(len(nums)-1):
#             for j in range(i+1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                    result.append(i)
#                    result.append(j)
#                    break
#         
#         return result               
#         
# =============================================================================
        
nums = [3,2,4]
target = 6
solve = Solution()
res = solve.twoSum(nums, target) 
print(res)                  