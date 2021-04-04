# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 15:56:34 2021

@author: Home
"""


s = "Let's take LeetCode contest"

res = ''
for word in s.split(' '):
    res += word[::-1] + ' '
print(res.strip())