# -*- coding: utf-8 -*-
"""
LeetCocde 14. Longest Common Prefix

Write a function to find the longest common prefix string 
amongst an array of strings.

If there is no common prefix, return an empty string "".
"""

class Solution:
    def longestCommonPrefix(self, strs):
        
        # To store longest common prefix
        result = ''
        
        # Base case 
        # Return null when the input list is empty
        if len(strs) == 0:
            return result
                
        # Sort the list alphabetically
        strs = list(sorted(strs))
        
        # Compare the first and last words 
        # Since we have already sorted the list,
        # common characters in first and last word will be 
        # common across all the words in the list
        
        for word in zip(strs[0], strs[-1]):
            # Compare characters
            if word[0] != word[1]:
                break
            result += word[0]
        return result    
            
# Driver code
strs = ["aaaaaflower","flow","flight"] 
strs1 = ["dog","racecar","car"]
      
sol = Solution()
result = sol.longestCommonPrefix(strs)    
print(result)        