number1=int(input("Enter a First Number "))
number2=int(input("Enter a Second Number "))
number3=int(input("Enter a Third Number "))
if(number1>number2 and number1>number3):
    print("Maximum Number Is :",number1)
elif(number2>number3):
    print("Maximum Number Is :",number2)  
else:
    print("Maximum Number is :",number3)    