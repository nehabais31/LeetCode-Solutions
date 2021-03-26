# -*- coding: utf-8 -*-
"""
A string s is called good if there are no two different characters in s 
that have the same frequency.

Given a string s, return the minimum number of characters 
you need to delete to make s good.

The frequency of a character in a string is the number of 
times it appears in the string. For example, in the string "aab", 
the frequency of 'a' is 2, while the frequency of 'b' is 1.
"""

class Solution:
    def minDeletions(self, s: str) -> int:
        
        import collections
        
        scanned = set()
        res = 0
        char_freq = collections.Counter(s)
        
        for ch, freq in char_freq.items():
            while freq > 0 and freq in scanned:
                freq -= 1
                res += 1
            scanned.add(freq)
            
        return res 
    

sol = Solution()
print(sol.minDeletions("aab"))   
print(sol.minDeletions("aaabbbcc"))   
print(sol.minDeletions("ceabaacb"))   
 