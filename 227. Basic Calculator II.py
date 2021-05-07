class Solution:
    def calculate(self, s: str) -> int:
        num = 0
        stack = []
        sign = '+'
        
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            if s[i] in '+-*/' or i == len(s) - 1:
                if sign == '+':
                    stack.append(num)
                if sign == '-':
                    stack.append(-num)
                if sign == '*':
                    stack.append(stack.pop() * num)
                if sign == '/':
                    val = int(stack.pop())
                    if val//num < 0 and val%num != 0:
                        stack.append(val//num + 1)
                    else:
                        stack.append(val//num)
                num = 0
                sign = s[i]
        return sum(stack)
        
import math                
sol = Solution()
print(sol.calculate("14-3/2"))
print(sol.calculate("3+2*2"))
print(sol.calculate(" 3/2 "))
print(sol.calculate("14/3+2"))
