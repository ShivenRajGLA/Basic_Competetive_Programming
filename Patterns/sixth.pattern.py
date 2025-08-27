number=int(input("Enter a number :"))
for i in range(1,number+1):
    for j in range(number-i):
        print(" ",end="")

    for k in range(1,2*i):
        print("*",end="")    

    print()    