# -*- coding: utf-8 -*-
"""
20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
"""

class Solution:
    def isValid(self, s: str) -> bool:
        
        

        stack = []

        valid_cases = {'(' : ')',
                       '[' : ']',
                       '{' : '}'}

        for char in s:
            # check for opening parenthesis in dictionary
            # If matches, push it to stack else pop element from stack
            # and compare them 
            if char in valid_cases:
                stack.append(char)
            elif not stack or valid_cases[stack.pop()] != char :
                return False
       
        return not stack        
  
    
str = "]"
sol = Solution()
res = sol.isValid(str)       
print(res) 
        