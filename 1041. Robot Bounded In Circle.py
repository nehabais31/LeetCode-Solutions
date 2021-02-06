# -*- coding: utf-8 -*-
"""
On an infinite plane, a robot initially stands at (0, 0) 
and faces north. 
The robot can receive one of three instructions:

"G": go straight 1 unit;
"L": turn 90 degrees to the left;
"R": turn 90 degrees to the right.

The robot performs the instructions given in order, 
and repeats them forever.

Return true if and only if there exists a circle 
in the plane such that the robot never leaves the circle.

"""

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x,y = 0,0
        direction = (0,1)
        
        for i in instructions:
            if i == "G":
                x = x + direction[0]
                y = y + direction[1]
            elif i == "L":
                direction = (-direction[1], direction[0])
            else:
                direction = (direction[1], -direction[0])
                
        return (x == y == 0) or (direction != (0,1))       


# Driver COde
instructions1 = "GGLLGG"
instructions2 = "GG"
instructions3 = "GL"

 
sol = Solution()
print(sol.isRobotBounded(instructions3))
    
