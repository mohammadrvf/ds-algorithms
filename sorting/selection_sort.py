array = [5,2,-3,4,6,7,1,9,12,-6,5];
def selection_sort(array):
    for i in range(len(array)-1):
        key = i;
        for j in range(i+1,len(array)):
            if array[j] < array[key]:
                key = j;
        array[i],array[key]=array[key],array[i];
    return array;
print(selection_sort(array));
