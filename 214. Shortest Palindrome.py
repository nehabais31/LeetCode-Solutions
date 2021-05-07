class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s or len(s) == 1 or s == s[::-1]:
            return s
        
        reverse_s = s[::-1]
         
        for i in range(len(s)):
            res = reverse_s[:i+1] + s
            if res == res[::-1]:
                return res
        
            
sol = Solution()
print(sol.shortestPalindrome('abcd'))
print(sol.shortestPalindrome('aacecaaa'))
print(sol.shortestPalindrome(''))
print(sol.shortestPalindrome('a'))
print(sol.shortestPalindrome('aba'))