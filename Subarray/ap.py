# input array
arr = [3,5,1]
n = len(arr)
arr.sort()          
diff= arr[1] - arr[0]
ap = 1  
for i in range(1, n-1):
    if arr[i+1] - arr[i] != diff:
        is_ap = 0 
        break
print(ap)
