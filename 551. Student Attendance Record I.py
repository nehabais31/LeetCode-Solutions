# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 12:05:58 2021

@author: Home
"""


class Solution:
    def checkRecord(self, s):
        if s.count('A') >= 2:
            return False
        
        for i in range(len(s)):
            if s[i: i+3] == 'LLL':
                return False
        return True
        
sol = Solution()
print(sol.checkRecord("PPALLP"))    
print(sol.checkRecord("PPALLL"))   
print(sol.checkRecord("PPPALLL"))  