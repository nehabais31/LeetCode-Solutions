"""
26. Remove Duplicates from Sorted Array

Given a sorted array nums, remove the duplicates in-place 
such that each element appears only once and returns the new length.

Do not allocate extra space for another array, 
you must do this by modifying the input array 
in-place with O(1) extra memory.
"""

class Solution:
    def removeDuplicates(self, nums) -> int:
        i = 0
        
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                nums[i + 1] = nums[j]
                i += 1
        print(f'Length: {i+1} \n {nums[ : i+1 ]}')
        
        
#Driver Code
nums = [1, 1, 2, 3, 3, 4, 5]        
sol = Solution()
sol.removeDuplicates(nums)    
    
            