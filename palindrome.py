# -*- coding: utf-8 -*-
"""
Given an integer x, 
return true if x is palindrome integer.
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]
                    

# Driver Code
x = [121, -121, 10, 1221, -101]            
sol = Solution()

for num in x :
    res = sol.isPalindrome(num)     
    print(f'{num}: {res}')       