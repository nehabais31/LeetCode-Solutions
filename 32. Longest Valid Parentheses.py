# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 09:25:25 2021

@author: Home
"""

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        left = 0
        right = 0
        max_length = 0
        
        # left to right traversing
        for i in range(len(s)):
            if s[i] == '(' :
                left += 1
            else:
                right += 1
            
            # if left = right then get max of maxlength and 2 * right
            if left == right :
                max_length = max(max_length, 2 * right)
            
            # if right becomes greater tha 0, reset left and right
            if right > left:
                left = right = 0
                
        # right to left ttraversal
        left = right = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == ')':
                right += 1
            else:
                left += 1
            
            # if left = right then get max of maxlength and 2 * left
            if left == right :
                max_length = max(max_length , 2 * left)
            
            # If left > right, reset leeft and right
            if left > right:
                left = right = 0
                
        return max_length        
    
    
sol = Solution()
s1 = "(()"    
s2 = ")()())"
s3 = ""

print(sol.longestValidParentheses(s1))
print(sol.longestValidParentheses(s2))
print(sol.longestValidParentheses(s3))