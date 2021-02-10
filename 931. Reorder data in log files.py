# -*- coding: utf-8 -*-
"""
931. Reorder data in log files
https://leetcode.com/problems/reorder-data-in-log-files/

"""

logs = ["a1 9 2 3 1","g1 act car",
 "zo4 4 7","ab1 off key dog","a8 act zoo","a2 act car"]


digit_log = []
alpha_log = []

for log in logs:
    if log.split(' ')[1].isdigit():
        digit_log.append(log)
    else:
        alpha_log.append(log)

# first sort based on identifier        
alpha_log.sort(key= lambda x: x.split(' ')[0])

# next sort based on key values
alpha_log.sort(key= lambda x: x.split(' ')[1:])
print(alpha_log + digit_log)        