# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/rotting-oranges/
"""

from collections import deque

class Solution:
    def orangesRotting(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        
        fresh_count = 0
        rotten = deque()   # to store rotten oranges coordinates
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    rotten.append((r,c))
                elif grid[r][c] == 1:
                    fresh_count += 1
                    
        minutes = 0
        
        # if there are rotten oranges in queue and there are still fresh 
        # oranges left, keep iterating
        while rotten and fresh_count > 0:
            minutes += 1
            
            for _ in range(len(rotten)):
                x,y = rotten.popleft()
                
                adjacent_coord = [[1,0], [-1,0], [0,1], [0,-1]]
                
                for dx, dy in adjacent_coord:
                    # coordinates for adjacent cell
                    xx, yy = x + dx, y + dy
                    
                    # check for cell if it is out of boundary
                    if xx < 0 or xx == rows or yy < 0 or yy == cols:
                        continue
                    
                    # Ignore a cell if it is empty or contain rotten oranges
                    if grid[xx][yy] == 0 or grid[xx][yy] == 2:
                        continue
                    
                    # update the fresh count
                    fresh_count -= 1
                    
                    # mark the fresh orange in grid as rotten
                    grid[xx][yy] = 2
                    
                    # add the rotten ones to queue
                    rotten.append((xx, yy))
                    
        return minutes if fresh_count == 0 else -1


sol = Solution()
grid = [[2,1,1],[0,1,1],[1,0,1]]
grid1 = [[0,2]]
print(sol.orangesRotting(grid1))                    
           
                    
        