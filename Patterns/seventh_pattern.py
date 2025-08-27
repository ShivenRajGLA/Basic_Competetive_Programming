num=int(input("Enter a Number :"))
for i in range(num,0,-1):
    for j in range(num-i):
        print(" ",end="")
    
    for k in range(2*i-1):
        print("*",end="")
    print()    