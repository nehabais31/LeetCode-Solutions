class Solution:
    def diffWaysToCompute(self, expression):
        memo = {}
        
        if expression.isdigit():
            return [int(expression)]
        if expression in memo:
            return memo[expression]
        
        res = []
        for i in range(len(expression)):
            if expression[i] in '+-*':
                res1 = self.diffWaysToCompute(expression[ :i])
                res2 = self.diffWaysToCompute(expression[i+1: ])
                
                for j in res1:
                    for k in res2:
                        res.append(self.helper(j, k, expression[i]))
        memo[expression] = res
        return res
                
    def helper(self, a, b, op):
        if op == '+':
            return a + b
        if op == '-':
            return a - b
        if op == '*':
            return a * b
        
sol = Solution()
print(sol.diffWaysToCompute("2-1-1"))
print(sol.diffWaysToCompute("2*3-4*5"))