def rotatedDigits( N) :
    list1 = set([1, 0, 8])
    list2 = set([0, 1, 8, 2, 5, 6, 9])
    count = 0
        
    for i in range(N+1):
        s = set([int(j) for j in str(i)])
        if s.issubset(list2) and not s.issubset(list1):
            count += 1
                
    return count

print(rotatedDigits(10))