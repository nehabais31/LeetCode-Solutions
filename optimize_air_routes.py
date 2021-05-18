'''
INPUT The input to the function/method consisits of three arguments: maxTravelDist, an integer representing the maximum operating travel distance of the given aircraft; forwardRouteList, a list of pairs of integers where the first integer represents the unique identifier of a forward shipping route and the second integer represents the amount of travel distance required bu this shipping route; returnRouteList, a list of pairs of integers where the first integer represents the unique identifer of a return shipping route and the second integer represents the amount of travel distance required by this shipping route.

OUTPUT Return a list of pairs of integers representing the pairs of IDs of forward and return shipping routes that optimally utilize the given aircraft. If no route is possible, return a list with empty pair.

Explanation: There are only three combinations [1,1],[2,1],and [3,1], which have a total of 4000, 6000, and 8000 miles, respectively. Since 6000 is the largest use that does tnot exceed 7000, [2,1] is the optimal pair.
'''

maxTravelDist = 10000 
forwardRouteList = [[1,3000],[2,5000],[3,7000],[4,10000]] 
returnRouteList = [[1,2000],[2,3000],[3,4000],[4,5000]]

# maxTravelDist = 7000 
# forwardRouteList = [[1,2000],[2,4000],[3,6000]] 
# returnRouteList = [[1,2000]]

res = {}
totalDistance = 0

for fwd in forwardRouteList:
    if fwd[1] == maxTravelDist :
        continue
    for rtn in returnRouteList:
        if rtn[1] == maxTravelDist:
            continue
        distance = fwd[1] + rtn[1]
        if distance <= maxTravelDist:
            if distance not in res.keys():
                res[distance ] = [[fwd[0], rtn[0]]]
            else:
                res[distance].append([fwd[0], rtn[0]])
            

print(res[max(res, key=res.get)])
 
 