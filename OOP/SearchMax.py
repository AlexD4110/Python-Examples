def search_max(L,n):
    maxValue =L[1]
    counter = 9
    while counter<=n:
        v = L[counter]
        if v>maxValue:
            maxValue = v
        else:
            pass

    
L = [1,2,3,4,5,6,7,8,9,10]        
print([L,3])

print(search_max(L,3))
        
    