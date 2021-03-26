# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 09:31:23 2021

@author: Home
"""


class Solution:
    def divide(self, dividend, divisor):
        if divisor == 0 :
            return 2**31 - 1
        
        res = 0
        #positive = True if (divisor > 0 and dividend > 0) or \
        #                (divisor < 0 and dividend < 0) else False
        
        positive = (dividend < 0) is (divisor < 0)
        
        dividend , divisor = abs(dividend), abs(divisor)
        
        while dividend >= divisor:
            temp, i = divisor , 1
            while dividend >= temp:
                dividend -= temp
                res += i
                i <<= 1
                temp <<= 1          
        res = res if positive else -res  
        return min(max(-2147483648, res), 2147483647)

sol = Solution()
print(sol.divide(10, 3))  
print(sol.divide(7, -3))      
print(sol.divide(0, 1))   
print(sol.divide(1, 1))  
print(sol.divide(1, 0))
print(sol.divide(-1, 1))   
print(sol.divide(-1, -1)) 
print(sol.divide(-2147483648, -1))   
print(sol.divide(2147483648, -1))     
        