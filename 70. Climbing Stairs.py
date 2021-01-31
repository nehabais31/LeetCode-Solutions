# -*- coding: utf-8 -*-
"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. 
In how many distinct ways can you climb to the top?
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        res = [0,1]
        
        for i in range(2,n+1):
            if i == 2:
                res.append(1)
            else:
                res.append(res[i-1] + res[i-2])
        return res[-1]+res[-2]
    


sol = Solution()
print(sol.climbStairs(4))