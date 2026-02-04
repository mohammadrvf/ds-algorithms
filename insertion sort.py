# inseertion sort
array = [5,2,-3,4,6,7,1,9,12,-6,5];
for i in range(1,len(array)): #o(n)
    key = array[i]; #o(1)
    j = i-1;
    while j>=0 and array[j] > key :   #o(n) 1 + 2+3+...+n= O(N) 
        array [j+1] = array[j]; #shift to right;
        j -=1;
    array[j+1]  = key;
print(array)

for i in range(len(array)-1):
    flag = False;
    for j in range(len(array-1,1,-1)):
        if array[j] < array[j-1]:
            array[j],array[j-1]=array[j-1],array[j];
            flag = True;
    if flag == False:
        print(array)

