# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 10:06:42 2021

@author: Home
"""

arr = [3, 2, -2, 5, -3, 4]

arr.sort(reverse=True)

for d in arr:
    if -d in arr:
        print(d)
        break


    
