"""
27. Remove Element

Given an array nums and a value val, 
remove all instances of that value in-place and 
return the new length.

Do not allocate extra space for another array, 
you must do this by modifying the input array in-place 
with O(1) extra memory.
"""

class Solution:
    def removeElement(self, nums, val: int) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.remove(val) 
            else :
                i += 1
        print(nums)        
        return len(nums) 

# Driver COde
nums = [0,1,2,2,3,0,4,2]
val = 2
sol = Solution()
print(sol.removeElement(nums, val))