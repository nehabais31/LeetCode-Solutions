'''
Binary Search Implementation -> Time Complexity = O(log(min(m, n)))  m = len(A), n = len(B)
Pseudocode:
      1. Choose shortest array for Binary Search
      2. Partition the two arrays such that total elements on left side = total ele on right side
         PartitionX + PartitionY = (m + n + 1) // 2  ->(half of total len of combined arr) 
                                                        adding 1 to handle both even odd cases       
      3. If maxLeftX <= minRightY and maxLeftY <= minRightX
            we have partitioned the array at correct place Found the position
            if total lenght of combined arr = even:
                return (max(maxLeftX, maxLeftY), min(minRightX, minRightY)) // 2
            else:
                return max(maxLeftX, maxLeftY)
        elif maxLeftX > minRightY:
                we are too far on right side of PartitionX. Go on left side
        else:
                we are too far on left side of Partition X. Go on right side
'''

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        # if nums1 is bigger than nums2, swap them so that nums1 is smaller than nums2
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        
        m = len(nums1)
        n = len(nums2)
        
        start = 0
        end = m
        
        while start <= end:
            partitionX = (start + end) // 2
            partitionY = (m + n + 1)//2 - partitionX
            
            # if partitionX == 0, it means nothing is there on left side, use -inf for maxLeftX
            # if partitionX == m, it means nothing is there on right side, use +inf for maxRightX
            maxLeftX  = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
            minRightX = float('inf')  if partitionX == m else nums1[partitionX]
            
            maxLeftY  = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
            minRightY = float('inf')  if partitionY == n else nums2[partitionY]
            
            if maxLeftX <=  minRightY and maxLeftY <= minRightX:
                # We have partiitoned the array at correct place 
                # Now, get the median as avergae of max of left elements and min of right elements if combied len is even
                # else get the median as max of left elements if combined len is odd
                if (m + n) % 2 == 0:
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2
                else:
                    return float(max(maxLeftX, maxLeftY) )
                
            elif maxLeftX > minRightY:
                # We are too far on right side of partitionX. Go on left side
                end = partitionX - 1
            else:
                # We are too far on left side of partitionX. Go on right side
                start = partitionX + 1
            
sol = Solution()
print(sol.findMedianSortedArrays([1,3], [2]))
print(sol.findMedianSortedArrays([1,2], [3, 4]))
print(sol.findMedianSortedArrays([0,0], [0, 0]))
print(sol.findMedianSortedArrays([], [1]))
print(sol.findMedianSortedArrays([2], []))
            
            