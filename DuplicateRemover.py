def Remove_Dupes(InArray):
    TempArray = InArray
    OutArray = []
    Counter = 0
    print('\n Array Before Duplicate Removal = ', InArray)
    print('\n # of Items before Duplicate removal = ', len(InArray))
    for i in range(len(InArray) - 1):
        if InArray[i] == None:
            continue
        for j in range(i+1, len(InArray)):            
            if InArray[i] == InArray[j]:
                TempArray[j] = None
    print(TempArray)
    for item in TempArray:
        if item == None:
            continue 
        else:            
            OutArray.append(item)
            Counter += 1    
    print('\n Array After Duplicate Removal = ', OutArray)
    print('\n # of Items after Duplicate removal = ', len(OutArray))
    
    return OutArray
# Test Case
TestArrayWithDupes = [2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,11,12,13,14,15,16,18,20,11,12,13,14,15,16,17,18,19,20]
TestArrayWithoutDupes = Remove_Dupes(TestArrayWithDupes)
