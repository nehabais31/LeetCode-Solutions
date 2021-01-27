"""
28. Implement strStr()

Return the index of the first occurrence of needle in haystack, 
-1 if needle is not part of haystack.
0 when needle is an empty string
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        else:
            return haystack.find(needle)

        
# Driver COde

#haystack = "hello"
#eedle = "ll"

haystack = "aaaaa"
needle = "bba"

#haystack = ""
#needle = ""            

sol = Solution()
idx = sol.strStr(haystack, needle)
print(idx)