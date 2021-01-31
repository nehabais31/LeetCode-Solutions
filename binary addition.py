# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 16:48:30 2021

@author: Home
"""

# =============================================================================
# class Solution:
#     def addBinary(self, a: str, b: str) -> str:
#         if len(a) > len(b):
#             diff = len(a) - len(b) 
#             b = "0" * diff + b
#         else:
#             diff = len(b) - len(a)
#             a = "0" * diff + a
#             
#         carry = 0
#         res = ""
#         i= len(a) - 1
#         j = len(b) - 1
#         
#         
#         while i >= 0 and j >= 0:
#             if a[i] == "1" and b[j] == "1":
#                 if carry == 0:
#                     carry = 1
#                     res += "0"
#                 else:
#                     res += "1"
#                     carry = 1
#             elif (a[i] == "1" and b[j] == "0") or (a[i] == "0" and b[j] == "1"):
#                 if carry == 0:
#                     res += "1"
#                     carry = 0
#                 else:
#                     res += "0"
#                     carry = 1
#             elif a[i] == "0" and b[j] == "0":
#                 if carry == 0:
#                     res += "0"
#                     carry = 0
#                 else:
#                     res += "1"
#                     carry = 0
#                 
#             i -= 1
#             j -= 1
#         
#         if carry == 1:
#             return str(carry) + res[::-1]   
#         else:
#             return res[::-1]
# 
     
# =============================================================================

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        result = ''

        a = list(a)
        b = list(b)

        while a or b or carry:
            if a:
                carry += int(a.pop())
            if b:
                carry += int(b.pop())

            result += str(carry %2)
            carry //= 2

        return result[::-1]

# Driver Code
sol = Solution()
a = "11"
b = "1"
print(sol.addBinary(a, b))       
            