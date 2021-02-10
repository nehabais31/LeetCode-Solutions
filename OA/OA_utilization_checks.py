# -*- coding: utf-8 -*-
"""
https://aonecode.com/amazon-online-assessment-utilization-checks

"""

def finalInstances(instances, averageUtil):
    """
    :type instances: int
    :type averageUtil: List[int]
    :rtype: int
    """    
    import math
    
    i = 0
    
    while i < len(averageUtil):
        if averageUtil[i] < 25 and instances > 1:
            instances = math.ceil(instances/ 2)
            i += 11
        elif averageUtil[i] > 60:
            instances *= 2
            if instances > (2 * 10**8):
                instances /= 2
                i += 1
            else:
                i += 11   
        elif (25 <= averageUtil[i]  <= 60) or (averageUtil[i] < 25 and instances == 1):
            i += 1
        
        
    return instances  

averageUtil = [30, 15, 18, 18, 19, 89, 15, 18, 18, 19, 89, 15, 18, 18, 19, 89, 15, 18, 18, 19, 89, 15, 18, 18, 19, 89]
instances = 1
print(finalInstances(instances, averageUtil))