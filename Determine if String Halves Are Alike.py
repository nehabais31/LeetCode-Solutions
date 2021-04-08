# -*- coding: utf-8 -*-
"""
You are given a string s of even length. Split this string into two halves of equal lengths, and let a be the first half and b be the second half.

Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains uppercase and lowercase letters.

Return true if a and b are alike. Otherwise, return false.
"""

class Solution:
    def halvesAreAlike(self, s):
        
        vowels = ['a', 'e', 'i', 'o', 'u']
        first_half = s[ : len(s)//2]
        second_half = s[ len(s)//2 : ]
        
        count_first_half = count_second_half = 0
        
        for i in range(len(s)//2):
            if first_half[i].lower() in vowels:
                count_first_half += 1
            if second_half[i].lower() in vowels:
                count_second_half += 1
                
        return count_first_half == count_second_half
            
sol = Solution()
strings = ['book', "textbook", "MerryChristmas", "AbCdEfGh"] 
    
for s in strings:
    print(f'{s}: {sol.halvesAreAlike(s)}\n')

map
