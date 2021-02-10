# -*- coding: utf-8 -*-
"""
https://aonecode.com/amazon-online-assessment-rover-control

"""

n = 4
commands = ['RIGHT', 'UP', 'DOWN', 'LEFT', 'LEFT', 'DOWN']

rows = 0
cols = 0

for cmd in commands:
    if cmd == 'RIGHT':
        if cols < n-1:
            cols += 1
    elif cmd == 'UP':
        if rows > 0 :
            rows -= 1
    elif cmd == 'DOWN':
        if rows < n-1 :
            rows += 1
    elif cmd == 'LEFT':
        if cols > 0:
            cols -= 1

print((rows * n) + cols)            
                        

