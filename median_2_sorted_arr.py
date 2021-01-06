'''
Given two sorted arrays nums1 and nums2 of size m and n respectively,
return the median of the two sorted arrays.
'''

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        # Combine the two arrays and sort them
        nums1.extend(nums2)
        nums1 = sorted(nums1)
        
        # Calculate median
        if len(nums1) % 2 == 0:
            median = (nums1[len(nums1)//2] + nums1[len(nums1)//2 - 1]) / 2
        else:
            median = nums1[len(nums1) // 2]     
        return median

# Driver Code
nums1 = [1,2]
nums2 = [3,4]    
sol = Solution()
res = sol.findMedianSortedArrays(nums1, nums2) 
print(res)       
        