# -*- coding: utf-8 -*-
"""
461. Hamming Distance

"""


x = 1
y = 4


# xor Sets each bit to 1 if only one of two bits is 1
x_xor_y = bin(x^y) 

count = 0
for i in x_xor_y:
    if i == '1':
        count += 1
print( count  )      
        