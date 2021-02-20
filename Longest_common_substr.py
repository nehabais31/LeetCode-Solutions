# -*- coding: utf-8 -*-
"""
LeetCocde 14. Longest Common Prefix

Write a function to find the longest common prefix string 
amongst an array of strings.

If there is no common prefix, return an empty string.
"""

class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if len(strs) == 0: 
            return ""
        s1, s2 = min(strs), max(strs)
        i = 0
        while i < len(s1) and i < len(s2) and s1[i] == s2[i]:
            i += 1
        return s1[:i]
    
strs = ["flower","flow","flight"] 
strs1 = ["dog","racecar","car"]
      
sol = Solution()
result = sol.longestCommonPrefix(strs)    
print(result)            