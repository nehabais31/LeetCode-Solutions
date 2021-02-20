# -*- coding: utf-8 -*-
"""
https://aonecode.com/interview-question/load_cargo
"""



def loadTheCargo(num, containers, itemSize, itemsPerContainer, cargoSize):
                    
    total_items = []
    
    for items in range(len(itemsPerContainer)):
        loading_items = [itemsPerContainer[items]] * containers[items]
        total_items.extend(loading_items)
        
    max_items = sorted(total_items)[-cargoSize:]
    return sum(max_items)

num= 3
containers=[3,1,6]
itemSize=3
itemsPerContainer=[2,7,4]
cargoSize=6

print(loadTheCargo(num, containers, itemSize, itemsPerContainer, cargoSize))
                  