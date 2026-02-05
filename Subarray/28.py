arr=[3,5,4,2]
max_diff=-1
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]<=arr[j]:
            max_diff=max(max_diff,j-i)
print(max_diff)            

