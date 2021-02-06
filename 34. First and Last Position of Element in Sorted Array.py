# -*- coding: utf-8 -*-
"""
Given an array of integers nums sorted in ascending order, 
find the starting and ending position 
of a given target value.

If target is not found in the array, return [-1, -1].
"""


class Solution:
    def searchRange(self, nums, target):
        result = [-1, -1]
        
        if len(nums) == 0:
            return result           
                 
        result[0] = self.left_search_helper(nums, target)
        result[1] = self.right_search_helper(nums, target)  
        
        return result
        
    def left_search_helper(self, nums, target):
        idx = -1
        low = 0
        high = len(nums) - 1
        
        while low <= high:
            mid = low + (high - low) // 2
            if target == nums[mid]:
                idx = mid
                high = mid -1
            elif target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        
        return idx
            
    def right_search_helper(self, nums, target):
        idx = -1
        low = 0
        high = len(nums) - 1
        
        while low <= high:
            mid = low + (high - low) // 2
            if target == nums[mid]:
                idx = mid
                low = mid + 1
            elif target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        
        return idx
        

# Driver Code        
nums = [5,7,7,8,8,10]
target = 8        
sol = Solution()
sol.searchRange(nums, target)