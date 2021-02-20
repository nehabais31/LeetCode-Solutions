# -*- coding: utf-8 -*-
"""
https://aonecode.com/amazon-online-assessment-zombie-matrix
"""

from collections import deque

def humanDays(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: int
    """           
    
    rows = len(matrix)
    cols = len(matrix[0])
    
    zombie = deque()
    
    humans = 0
    
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 1:
                zombie.append((r,c))
            elif matrix[r][c] == 0:
                humans += 1
                
    days = 0
    
    while zombie and humans > 0:
        days += 1
        
        for _ in range(len(zombie)):
            x, y = zombie.popleft()
            
            adjacent_cells = [[1,0], [-1,0], [0,1],[0,-1]]
            
            for dx, dy in adjacent_cells:
                xx, yy = x + dx , y + dy
                
                if xx < 0 or xx == rows or yy < 0 or yy == cols:
                    continue
                
                if matrix[xx][yy] == 1:
                    continue
                
                # update humans count
                humans -= 1
                
                # convert humans to zombie
                matrix[xx][yy] = 1
                
                # append zombie result
                zombie.append((xx, yy))
                
    return days if humans == 0 else -1

matrix = [[0, 1, 1, 0, 1],
[0, 1, 0, 1, 0],
[0, 0, 0, 0, 1],
[0, 1, 0, 0, 0]]

print(humanDays(matrix))