# -*- coding: utf-8 -*-
"""
Given a string containing digits from 2-9 inclusive, 
return all possible letter combinations 
that the number could represent. 
Return the answer in any order.

A mapping of digit to letters 
(just like on the telephone buttons) is given below. 
Note that 1 does not map to any letters.
"""

class Solution:
    def letterCombinations(self, digits):
        result = []
        if len(digits) == 0:
            return result
        
        phone_map = {2: 'abc',
                     3: 'def',
                     4: 'ghi',
                     5: 'jkl',
                     6: 'mno',
                     7: 'pqrs',
                     8: 'tuv',
                     9: 'wxyz'}
        
        self.map_digits(digits, phone_map, result)
        return result
        
    def map_digits(self, digits, phone_map, result, curr_pos = 0, curr_str = ''):
        if curr_pos == len(digits):
            result.append(curr_str)
            return
        for i in phone_map[int(digits[curr_pos])]:
            self.map_digits(digits, phone_map, result, curr_pos + 1, curr_str+i)
            
sol = Solution()
print(sol.letterCombinations('23'))