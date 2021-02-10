# -*- coding: utf-8 -*-
"""
https://aonecode.com/amazon-online-assessment-cutoff-ranks

"""


def countLevelUpPlayers(cutOffRank, num, scores):                    
    
    if num > 10**5:
        return 0
        
    count = 0
    
    scores.sort(reverse=True)
    rank = list(range(1, len(scores)+1))
    
    for p in range(1, len(scores)):
        prev = scores[p -1]
        if scores[p] == prev:
            rank[p] = rank[p-1]
            
    for r in rank:
        if r <= cutOffRank:
            count += 1     

    
    return count   

cutOffRank = 4
num=5
scores=[2,2,3,4,5]
print(countLevelUpPlayers(cutOffRank, num, scores))