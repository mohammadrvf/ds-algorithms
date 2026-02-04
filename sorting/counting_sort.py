array = [4, 2, 2, 8, 3, 3, 1, 0, 4, 5]
maxs=array[0];
for i in range(1,len(array)):
    if maxs < array[i] :
        maxs = array[i];
count = [0] * (maxs + 1);
for i in range(len(array)):
    count[array[i]] +=1;
array=[];
for i in range(len(count)):
    array += count[i] * [i];
print(array)
