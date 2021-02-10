# -*- coding: utf-8 -*-
"""
https://aonecode.com/interview-question/schedule-tasks
"""


num = 5
power = [4,2,8,3,5]
tasks = 19
count = 0
power.sort(reverse=True)

if tasks == 0:
    print(0)
    
for i in range(len(power)):
    if tasks <= 0:
        break
    elif power[i] != 0:
       tasks -= power[i]
       power[i] //= 2
       count += 1
print(count)                   