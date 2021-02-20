# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 18:45:09 2021

@author: Home
"""


class Solution:
    def kClosest(self, points, K) :
        return sorted(points, key = lambda x: x[0]**2 + x[1]**2)[:K]
                

points = [[3,3],[5,-1],[-2,4]]
K = 2
print(Solution().kClosest(points, K))
    