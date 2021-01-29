# -*- coding: utf-8 -*-
"""
Given a signed 32-bit integer x, 
return x with its digits reversed. 
If reversing x causes the value to go outside 
the signed 32-bit integer range [-231, 231 - 1], then return 0.
"""

class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x > 0 else -1
        max_int = 2**31-1 
        rev = 0
        x = abs(x)
        while x > 0:
            last_digit = x % 10
            x //= 10
            if rev > (max_int - last_digit) / 10:
                return 0
            rev = rev * 10 + last_digit
        return sign*rev
    

sol = Solution()
ans = sol.reverse(-123)
print(ans)    