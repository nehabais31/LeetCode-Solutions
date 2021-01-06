
'''
Given a string s, Find the length of 
the longest substring without repeating characters.
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        scanned_chars = {}
        max_len = 0
        i = 0
        
        for j in range(len(s)):
            if s[j] in scanned_chars:
                i = max(i, scanned_chars[s[j]] + 1)
            scanned_chars[s[j]] = j
            max_len = max(max_len, j - i + 1)

        return max_len

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




