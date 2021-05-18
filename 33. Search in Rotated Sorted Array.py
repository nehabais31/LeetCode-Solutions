# class Solution:
#     def search(self, nums, target):
#         start = 0
#         end = len(nums)
        
#         while start < end:
#             mid = start + (end - start) // 2
        
#             if nums[mid] < nums[0] and target < nums[0]:
#                 if nums[mid] < target:
#                     start = mid + 1
#                 elif nums[mid] > target:
#                     end = mid
#                 else:
#                     return mid
#             elif target < nums[0]:
#                 start = mid + 1
#             else:
#                 end = mid
#         return -1
            

# sol = Solution()
# print(sol.search([4,5,6,7,0,1,2], 3))
# print(sol.search([4,5,6,7,0,1,2], 0))
# print(sol.search([1], 0))

from itertools import product

x = [1, 2,3, 4]
y = [5, 6]
z = [7,8,9]

print(list(zip(x,y,z)))