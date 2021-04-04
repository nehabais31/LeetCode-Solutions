# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 18:07:02 2021

@author: Home
"""

class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        if sx > tx or sy > ty: return False
        if sx == tx: return (ty-sy)%sx == 0 # only change y
        if sy == ty: return (tx-sx)%ty == 0
        if tx > ty: 
            return self.reachingPoints(sx, sy, tx%ty, ty) # make sure tx%ty < ty
        elif tx < ty: 
            return self.reachingPoints(sx, sy, tx, ty%tx)
        else:
            return False
    
sol = Solution()

print(sol.reachingPoints(sx = 1, sy = 1, tx = 3, ty = 5))    

print(sol.reachingPoints(sx = 1, sy = 1, tx = 2, ty = 2))   

print(sol.reachingPoints(sx = 1, sy = 1, tx = 1, ty = 1))   