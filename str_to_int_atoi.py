# -*- coding: utf-8 -*-
"""
LeetCode: 8. String to Integer (atoi)

The algorithm for myAtoi(string s) is as follows:

1. Read in and ignore any leading whitespace.
2. Check if the next character (if not already at the end of the string) is '-' or '+'. 
   Read this character in if it is either. 
   This determines if the final result is negative or positive respectively. 
   Assume the result is positive if neither is present.
3. Read in next the characters until the next non-digit charcter or 
  the end of the input is reached. The rest of the string is ignored.
4. Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). 
   If no digits were read, then the integer is 0. 
   Change the sign as necessary (from step 2).
5. If the integer is out of the 32-bit signed integer range [-2**31, 2**31 - 1], 
   then clamp the integer so that it remains in the range. 
    Specifically, integers less than -2**31 should be clamped to -2**31, 
    and integers greater than 231 - 1 should be clamped to 2**31 - 1.
    Return the integer as the final result.
"""

class Solution:
    def myAtoi(self, s: str) -> int:
        res = 0
        sign = 1
        start = False

        for i in s:
            if i.isnumeric():
                if not start :
                    start = True
                res = res * 10 + int(i)
            elif i == ' '  and not start:
                continue
            elif i == '+'  and not start:
                start = True
            elif i == '-' and not start:
                start = True
                sign = -1
            else:
                break

        res = res * sign

        if  res > (2**31 - 1):
            print( 2**31 - 1)
        elif res < (-2**31):
            print( -2**31)
        else:
            print( res)
            
                
# Driver Code
sol = Solution()
sol.myAtoi('+-12')
sol.myAtoi('+23')
sol.myAtoi('-31')
sol.myAtoi("42")       
sol.myAtoi(".1")
sol.myAtoi("   -42")    
sol.myAtoi("3.142")  
sol.myAtoi("4193 with words")    
sol.myAtoi("words and 987")    
sol.myAtoi("-91283472332")  
sol.myAtoi("91283472332")  
