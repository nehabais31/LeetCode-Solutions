"""
11. Container With Most Water

Given n non-negative integers a1, a2, ..., an , 
where each represents a point at coordinate (i, ai). 
n vertical lines are drawn such that 
the two endpoints of the line i is at (i, ai) and (i, 0). 
Find two lines, which, together with the x-axis 
forms a container, such that the container 
contains the most water.
"""

class Solution:
    def maxArea(self, height) -> int:
        low = 0 
        high = len(height)-1
        res = []
        
        while low < high:
            length = min(height[low], height[high])
            width = high - low
            area = width * length
            res.append(area)
            
            if height[low] < height[high]:
                low += 1
            else:
                high -= 1
                
        return max(res)
    
# Driver code
sol = Solution()
print(sol.maxArea([1,8,6,2,5,4,8,3,7]))    
    