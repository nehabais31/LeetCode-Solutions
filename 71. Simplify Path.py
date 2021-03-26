# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 09:50:04 2021

@author: Home
"""

class Solution:
    def simplifyPath(self, path: str) -> str:
        # '.' , '...',  do nothing
        # '..' pop from stack if stack not empty
        
              
        stack = []
        for ch in path.split('/'):
            if ch == '..' and stack:
                stack.pop()
            elif ch not in ['.', "", '..']:
                stack.append(ch)
                
        return '/' + '/'.join(stack)      
                

sol = Solution()
print(sol.simplifyPath("/home/"))

print(sol.simplifyPath("/../"))

print(sol.simplifyPath("/home//foo/"))
print(sol.simplifyPath("/a/./b/../../c/"))   