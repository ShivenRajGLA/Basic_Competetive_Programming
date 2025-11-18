arr=[]
n=int(input("enter n :"))
for i in range(n):
    ele=int(input())
    arr.append(ele)
print(arr)    
unique=0
for num in arr:
    unique ^=num
print(unique)