# -*- coding: utf-8 -*-
"""
https://aonecode.com/aplusplus/interviewctrl/getInterview/90812391

"""
n = 3   # horizontal
m = 2   # vertical
h =  [1, 2, 3]
v = [1,2]

hor_shelves = list(range(n+2))
ver_shelves = list(range(m+2))

hor_prev = hor_shelves[0]
ver_prev = ver_shelves[0]

hor_res = []
ver_res = []

# iterate over shelves to remove list
for hor_shelve_to_remove in h:
    # Iterate over horizontal and pop the number to be removed
    # before popping store its prev and next value 
    for i in range(1,len(hor_shelves)-1):
        if hor_shelve_to_remove == hor_shelves[i]:
            hor_prev = hor_shelves[i - 1]
            hor_next = hor_shelves[i + 1]
            hor_res.append([hor_prev, hor_next])
            break

for ver_shelve_to_remove in v:    
    for i in range(1,len(ver_shelves)-1):
        if ver_shelve_to_remove == ver_shelves[i]:
            ver_prev = ver_shelves[i - 1]
            ver_next = ver_shelves[i + 1]
            ver_res.append([ver_prev, ver_next])
            break  
        

hor_min = min(hor_res, key = lambda x: x[0])[0]
hor_max = max(hor_res, key = lambda x: x[1])[1] 
hor_range = hor_max - hor_min

ver_min = min(ver_res, key = lambda x: x[0])[0]
ver_max = max(ver_res, key = lambda x: x[1])[1] 
ver_range = ver_max - ver_min

print(hor_range * ver_range * 1)
 