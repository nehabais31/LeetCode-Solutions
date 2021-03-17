# -*- coding: utf-8 -*-
"""
Given a string s, return the longest palindromic substring in s.

"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        if len(s) == 1:
            return s
        
        res = ''
        
        for i in range(len(s)):
            # odd nbr of chars in string
            odd  = self.checkPalindrome(s, i, i)
            even = self.checkPalindrome(s, i, i+1)
            
            res = max(res, odd, even, key=len)
            
        return res 
    
    
    def checkPalindrome(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1 : right]
    

sol = Solution()

print(sol.longestPalindrome("bb"))
print(sol.longestPalindrome('ababb'))
print(sol.longestPalindrome('babad'))
print(sol.longestPalindrome(''))
print(sol.longestPalindrome('a'))
print(sol.longestPalindrome('ac'))
