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
containers=[1, 2, 3]
itemSize=3
itemsPerContainer=[3, 2, 1]
cargoSize=3

print(loadTheCargo(num, containers, itemSize, itemsPerContainer, cargoSize))
                  