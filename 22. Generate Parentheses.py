class Solution:
    def generateParenthesis(self, n):
        # Maintain 2 stacks, one for opening ( and other for )
        if not n:
            return []
        
        left, right = n, n
        stack = []
        self.dfs(left, right, stack, '')
        return stack
    
    def dfs(self, left, right, stack, string):
        if right < left:
            return
        if not left and not right:
            stack.append(string)
            return
        if left:
            self.dfs(left-1, right, stack, string + '(')
        if right:
            self.dfs(left, right-1, stack, string + ')')
            
            
sol = Solution()
print(sol.generateParenthesis(3))
print(sol.generateParenthesis(1))
            
        