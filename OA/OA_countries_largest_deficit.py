# -*- coding: utf-8 -*-
"""
https://aonecode.com/interview-question/FindCountriesWithTheLargestDeficit
"""

# =============================================================================
# borrowers=['Alex', 'Blake', 'Casey', 'Blake', 'Alex', 'Alex']
# lenders=['Blake', 'Alex', 'Alex', 'Casey', 'Blake', 'Casey'] 
# amounts=[2, 2, 5, 7, 4, 4]
# =============================================================================


def minimumDebtMembers(borrowers, lenders, amounts):
    trade_dict = {}  
    i = 0
    
    while i < len(borrowers):
        if borrowers[i] not in trade_dict.keys():
            trade_dict[borrowers[i]] = -amounts[i]
        else:
            trade_dict[borrowers[i]] = trade_dict[borrowers[i]] - amounts[i]
                
        if lenders[i] not in trade_dict.keys():
            trade_dict[lenders[i]] = amounts[i]     
        else:
            trade_dict[lenders[i]] = trade_dict[lenders[i]] + amounts[i]
            
        i += 1    
                
    min_trade_amnt = min(trade_dict.values()) 
    if min_trade_amnt == 0:
            return ['None']
    else:
        result = [k for k, v in trade_dict.items() if v == min_trade_amnt]
        return sorted(result)  
    
#borrowers=['Alex', 'Blake','Casey', 'Blake', 'Alex', 'Alex']
#lenders=['Blake', 'Alex','Alex', 'Casey', 'Blake', 'Casey'] 
#amounts=[2,2,5,7,4,4]    

borrowers=['Alex', 'Blake']
lenders=['Blake', 'Alex'] 
amounts=[1,1]  
    
print(minimumDebtMembers(borrowers, lenders, amounts))    
            