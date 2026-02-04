for i in range(len(array)-1):
    flag = False;
    for j in range(len(array)-1,0,-1):
        if array[j] < array[j-1]:
            array[j],array[j-1]=array[j-1],array[j];
            flag = True;
    if flag == False:
        break;
print(array)
