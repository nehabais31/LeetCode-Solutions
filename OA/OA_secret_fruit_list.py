# -*- coding: utf-8 -*-
"""
https://aonecode.com/amazon-online-assessment-secret-fruits
"""
def matchSecretLists(secretFruitList, customerPurchasedList):
    i = 0
    j = 0
    
    # check for null secretlist and customer purchsed list
    if len(secretFruitList) == 0:
        return True
    if len(customerPurchasedList) == 0:
        return False
    
    for c in range(len(customerPurchasedList)):
        if secretFruitList[i][j] == customerPurchasedList[c] or \
            secretFruitList[i][j] == 'anything':
                j += 1
                
                if j == len(secretFruitList[i]):
                    j = 0
                    i += 1
                if i == len(secretFruitList):
                    return True
        else:
              c -= j
              j = 0
              
    return False              


secretFruitList = [['orange','mango'], ['watermelon','mango']]
customerPurchasedList = ['orange', 'mango','apple', 'watermelon','mango']               
print(matchSecretLists(secretFruitList, customerPurchasedList))


