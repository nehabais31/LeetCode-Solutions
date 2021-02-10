# -*- coding: utf-8 -*-
"""
A peak element is an element that is strictly greater than its neighbors.

Given an integer array nums, 
find a peak element, and return its index. 
If the array contains multiple peaks, return the index to any of the peaks.
"""


class Solution:
    def findPeakElement(self, nums):
      
        low = 0
        high = len(nums)-1
        
        while low <= high:
            mid = low + (high - low)//2
            
            if (mid -1 < 0 or nums[mid] > nums[mid-1] ) and (mid+1>=len(nums) or nums[mid] > nums[mid+1]):
                return mid
            elif mid-1>=0 and nums[mid] < nums[mid-1]:
                high = mid-1
            elif mid+1 < len(nums) and nums[mid] < nums[mid+1] :
                low = mid+1
                
        return low       
    
print(Solution().findPeakElement([1,2,3,1])  )  