"""
35. Search Insert Position

Given a sorted array of distinct integers and a target value,
return the index if the target is found. 
If not, return the index where it would be 
if it were inserted in order.
"""

class Solution:
    def searchInsert(self, nums, target) -> int:
        low = 0
        high = len(nums) - 1
        
        while low <= high :
            mid = (low + high) // 2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                low = mid + 1   
            elif target < nums[mid]:
                high = mid - 1
                
        
        return low 
        

sol = Solution()
nums = [1,3,5,6]
target = 4

idx =  sol.searchInsert(nums, target)       
print(idx)

    