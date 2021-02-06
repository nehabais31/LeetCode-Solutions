"""
Given an array nums of n integers, 
are there elements a, b, c in nums such that 
a + b + c = 0? 
Find all unique triplets in the array 
which gives the sum of zero.

solution set must not contain duplicate triplets.
"""

# Sorting = O(n logn)
# Searching = O(n^2) 
# Set to final list = O(n)
# Overall Time complexity = O(n^2)

class Solution:
    def threeSum(self, nums):
        result = []
        
        if len(nums) < 3:
            return result
                
        num_set = set()
        nums.sort()
        
        for i in range(len(nums)):
            low = i+1
            high = len(nums)-1
            target = nums[i] * -1

            while low < high:
                total = nums[low] + nums[high]
                if total == target:
                    num_set.add((nums[i], nums[low], nums[high]))
                    low += 1
                elif total > target:
                    high -= 1
                elif total < target:
                    low += 1
                else:
                    low += 1

        for items in num_set:
            result.append(items)
        return result    
    
  
nums = [-1,0,1,2,-1,-4]
#nums1 = [-1,0,1]
sol = Solution()
print(sol.threeSum(nums))  