# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 23:11:44 2021

@author: Home
"""
numOfPoints = 3

points = ["p1", "p2","p3"]

xCoordinates = [3,2,1]

yCoordinates = [3,2,3]

numOfQueriedPoints = 3

queriedPoints = ["p1", "p2","p3"]

points_dict = {}

for idx, point in enumerate(points):
    if point not in points_dict.keys():
        points_dict[point] = [xCoordinates[idx], yCoordinates[idx]]

result = []

for idx, p in enumerate(queriedPoints):
    temp = 999999
    for k in points_dict:
        if p == k:
            continue
        p_x = points_dict[p][0]
        p_y = points_dict[p][1]
        
        if p_x == points_dict[k][0] or p_y == points_dict[k][1] :
            dist = (p_x - points_dict[k][0])**2 + \
                  (p_x - points_dict[k][1])**2 
           
            if dist < temp:
                temp = k
                
    if temp == 999999:
        temp = None
    result.append(temp)    
print(result)        
                       
 