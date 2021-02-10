# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 14:04:52 2021

@author: Home
"""

def minDifficulty( A, d):
    total_items = len(A)
    inf = float('inf')
    
    if total_items < d: 
        return -1
    dp = [inf] * total_items + [0]
    
    for d in range(1, d + 1):
        for i in range(total_items - d + 1):
            maxd = 0
            dp[i] = inf
            for j in range(i, total_items - d + 1):
                maxd = max(maxd, A[j])
                dp[i] = min(dp[i], maxd + dp[j + 1])
    return dp[0]          
    
A = [10,2,20,5,15,10,1]
d = 3
print(minDifficulty( A, d))