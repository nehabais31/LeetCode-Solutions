# -*- coding: utf-8 -*-
"""
Given two non-negative integers num1 and num2 represented as strings, 
return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or 
convert the inputs to integer directly.
"""


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        def map_str_nbr(num): 
            
            # Digits can be from 0 to 9 so creating a dict for mapping
            mapping = {'0':0, 
                       '1':1, 
                       '2':2, 
                       '3':3, 
                       '4':4, 
                       '5':5, 
                       '6':6, 
                       '7':7, 
                       '8':8, 
                       '9':9}

            res = 0
            for i, ch  in enumerate(num):
                if ch in mapping.keys():
                    # Get string length from current position 
                    str_len = len(num[i : ])
                    num_int = mapping[ch]
                    
                    # 10 to the power string lenght calculated above
                    res += num_int * 10**(str_len-1)

            return res      
            
        num1_nbr =  map_str_nbr(num1)
        num2_nbr =  map_str_nbr(num2)

        result = num1_nbr * num2_nbr
        return str(result)    
            
sol = Solution()
print(sol.multiply('123', '456'))    
      