# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 17:38:48 2021

@author: Home
"""


def color(n,k, costmatrix):
    cost = [[0 for i in range(k)] for j in range(n)]
    '''
    row = house number
    column = color used
    cost of painting the first row will be trivial
    '''
    
    cost[0] = costmatrix[0][:]
    
    '''
    cost of painting further building will be depending upon
    previous colors chosen
    '''
    for house in range(n):
        for col in range(k):
            previous = cost[house-1][:col] + cost[house-1][col+1:] #cannot be of same color
            cost[house][col] = costmatrix[house][col] + min(previous)
    
    return min(cost[-1]) #last row in the cost of coloring n houses

cost_mat = [[1,2,2],[2,2,1],[2,1,2]]
print(color(3,3,cost_mat)) # 9