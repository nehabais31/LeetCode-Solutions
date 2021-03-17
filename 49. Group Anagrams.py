# -*- coding: utf-8 -*-
"""
Given an array of strings strs, 
group the anagrams together. 
You can return the answer in any order.

An Anagram is a word or phrase formed by 
rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

 
"""

class Solution:
    def groupAnagrams(self, strs):
        shuffled_word = {}

        for word in strs:
            word_sort = ''.join(sorted(word))
            if word_sort not in shuffled_word.keys():
                shuffled_word[word_sort] = [word]
            else:
                shuffled_word[word_sort].append(word)

        return shuffled_word.values()   

sol = Solution()

# Test cases
strs1 = ["eat","tea","tan","ate","nat","bat"]
strs2 = ['']
strs3 = 'a'

print(sol.groupAnagrams(strs1))    
print(sol.groupAnagrams(strs2))   
print(sol.groupAnagrams(strs3))   