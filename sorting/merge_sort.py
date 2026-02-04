def merge_sort(array):
    if len(array) == 1:
        return array
    mid = len(array)//2;
    left_array = merge_sort(array[:mid]);
    right_array = merge_sort(array[mid:]);
    result = []
    i = 0;
    j = 0;
    print(f'----------  mergesort algoritm ----------')
    print(f'left array {left_array}');
    print(f'right_array {right_array}')
    while i < len(left_array) and j < len(right_array):
        if left_array[i] < right_array[j]:
            result.append(left_array[i])
            i += 1
        else:
            result.append(right_array[j])
            j += 1
    result += left_array[i:];
    result += right_array[j:]
    print(result)
    return result

print(f'finaly array {merge_sort([10,9,8,7,6,5,4,3,2,1,0])}');
