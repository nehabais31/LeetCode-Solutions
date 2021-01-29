# -*- coding: utf-8 -*-
"""
58. Length of Last Word

Given a string s consists of some words separated by spaces, 
return the length of the last word in the string. 
If the last word does not exist, return 0.
"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        return len(s.strip(' ').split(' ')[-1])
        
        
    
#Driver COde
sol = Solution()
print(sol.lengthOfLastWord("Hello World"))
print(sol.lengthOfLastWord("a "))