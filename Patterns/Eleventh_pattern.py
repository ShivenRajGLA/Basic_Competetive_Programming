num=int(input("Enter a Number :"))
for i in range(1,num+1):
    for j in range(num-i+1):
        print("*",end="")
    for j in range(2*i-2):
        print(" ",end="")
    for j in range(num-i+1):
        print("*",end="")  
    print()          

