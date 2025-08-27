num=int(input("enter a number :"))
for i in range(1,num+1):
    for j in range(1,i+1):
        print("*",end="")
    for j in range(2*num-2*i):
        print(" ",end="")
    for j in range(1,i+1):    
        print("*",end="")    

    print()    