class Solution:
    def smallestSubsequence(self, s: str) -> str:
        position = {ch: i for i, ch in enumerate(s)} 
        stack = []
        
        for i , ch in enumerate(s):
            if ch  in stack: continue
            while stack and stack[-1] > ch and i < position[stack[-1]]:
                stack.pop()
            stack.append(ch)
        return ''.join(stack)

    
sol = Solution()
print(sol.smallestSubsequence("bcabc"))
print(sol.smallestSubsequence("cbacdcbc"))

