# -*- coding: utf-8 -*-
"""
https://aonecode.com/amazon-online-assessment-transaction-logs

"""


logs = ["88 99 200", "88 99 300", "99 32 100", "12 12 15"]

threshold = 2

count_dict = {}

for log in logs:
    sender_id = log.split(' ')[0]
    rec_id = log.split(' ')[1]
    if sender_id == rec_id:
        if sender_id not in count_dict.keys():
            count_dict[sender_id] = 1
        else:
            count_dict[sender_id] += 1
            
    else:
        if sender_id not in count_dict.keys():
            count_dict[sender_id] = 1
        else:
            count_dict[sender_id] += 1
            
        if rec_id not in count_dict.keys():
            count_dict[rec_id] = 1
        else:
            count_dict[rec_id] += 1    


count_dict = {k:v for k,v in sorted(count_dict.items(), key = lambda x: x[0])}            

result = []

for k, v in count_dict.items():
    if v >= threshold:
        result.append(str(k))

print(result)        