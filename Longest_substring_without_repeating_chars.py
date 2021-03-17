# -*- coding: utf-8 -*-
"""
Given a string s, 
find the length of the longest substring 
without repeating characters.
 
"""

class Solution:
    def lengthOfLongestSubstring(self, s):
        longest = 0
        
        # Pointers to move over string
        left = right = 0
        
        # set to store unique vales of seen characters
        seen_chars = set()
        
        # Initially left right at 0
        # Iterate over string, if right pointers char is not in seen_chars
        # add it and increment right pointer
        # check longest value as max of longest and right - left ssubstrings
        # if char is in seen_chars, remove element from left 
        # incremnt left poiner
        
        while right < len(s):
            if s[right] not in seen_chars:
                seen_chars.add(s[right])
                right += 1
                longest = max(longest, right - left)
            else:
                seen_chars.remove(s[left])
                left += 1
        return longest   

# Driver code
s1 = 'abcabcbb'  
s2 = 'pwwkew'
s3 = 'bbbbb'
s4 = ''

sol = Solution()
res1 = sol.lengthOfLongestSubstring(s1)
print(f'Longest length of subsring in {s1}: {res1}\n')

res2 = sol.lengthOfLongestSubstring(s2)
print(f'Longest length of subsring in {s2}: {res2}\n')

res3 = sol.lengthOfLongestSubstring(s3)
print(f'Longest length of subsring in {s3}: {res3}\n')

res4 = sol.lengthOfLongestSubstring(s4)
print(f'Longest length of subsring in {s4}: {res4}')


        

                
        
        
        