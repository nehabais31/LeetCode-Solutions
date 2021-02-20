# -*- coding: utf-8 -*-
"""
Write an algorithm to output the state of cells after the given number of days, 
without any extra memory (data structure).

https://stackoverflow.com/questions/39171403/cell-compete-problems

"""
days = 2
houses = [1,1,1,0,1,1,1,1,]

def cellComplete(houses, days):
    if len(houses) != 8 or days < 1:
        return houses
    
        
    for i in range(days):
        i = 0
        prev = 0 
        next_val = 0
        
        while i < len(houses):
            if i < len(houses)-1:
                next_val = houses[i + 1]
            elif i == len(houses) - 1:
                next_val = 0
                
            # making active and incative
            if prev == next_val:
                prev = houses[i]
                houses[i] = 0
            else:
                prev = houses[i]
                houses[i] = 1
                
            i += 1
            
    return houses

print(cellComplete(houses, days))
     