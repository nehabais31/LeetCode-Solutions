# -*- coding: utf-8 -*-
"""
LeetCode 13: 13. Roman to Integer

Given a roman numeral, convert it to an integer.
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I': 1,
         'V': 5,
         'X': 10,
         'L': 50,
         'C': 100,
         'D': 500,
         'M': 1000}


        res = 0

        for i in range(len(s)):
             curr_val = roman[s[i]]
             if i > 0 and curr_val > roman[ s[i - 1] ]:
                 res += curr_val - 2 * roman[ s[i - 1] ]
             else:
                 res += curr_val
        return res
    
# Driver Code  
sol = Solution()

val = ['III', 'IV', 'IX', 'LVIII', 'MCMXCIV']

for v in val :
    result = sol.romanToInt(v)
    print(f'{v}: {result}\n')


