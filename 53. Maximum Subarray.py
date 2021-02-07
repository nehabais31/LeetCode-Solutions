# -*- coding: utf-8 -*-
"""
Given an integer array nums, 
find the contiguous subarray (containing at least one number)
which has the largest sum and return its sum.
"""

# =============================================================================
# Approach =>
# Iterate over the array
# whenever the previous nbr is negative, increment the loop
# if prev was positive, add it to current number:
# at last return max from the list
# =============================================================================

class Solution:
    def maxSubArray(self, nums):
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
                
        return max(nums)        
        

# Driver Code
nums = [-2,1,-3,4,-1,2,1,-5,4]
nums1 =     [1]
nums2 = [0]
nums3 = [-1]
nums4 = [-10000]

sol = Solution()
print(sol.maxSubArray(nums))