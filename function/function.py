# A Function is a Block of Reusable Code / statememt  that return a specific task
# It Excecutes a code whenever the function is call 
# def Hello():
#     print("Hello Sir")

# Hello()    

# def MakeTea():
#     print("Enjoy Your Tea")

# MakeTea()    

# def hello(name):
#     print("Hello",name)

# hello("Shiven Raj")    
# hello()

# Parametres are the variables listed inside the parenthesis in the function defitions 
# Arguments are the actuals values that are passed to the fucntion when it is called 
#  Q .Write a program to print sq of the nnumbers
#  Q2. Write a program to print sqaure of all numbers from x to y
#  Q3 Write a program to implement a pythagoram theorem using function
#  Q4 Write a program to make a calculator using function

# Sol 1
# def Square(num):
#     print("The Sqaure of the Number is :",num*num)

# Square(num=int(input("Enter a Number :")))

# # Sol 2
# num1=int(input("Enter first number: "))
# num2=int(input("Enter second number: "))
# def Square2(num1,num2):
#     for i in range(num1,num2+1):
#         print("The Square of the numbers is :",i*i)
# Square2(num1,num2)        

# Sol 3
# p=int(input("enter perpendicular :"))
# b=int(input("enter base :"))
# h=int(input("enter Height :"))
# def pythagoram_theo(p,b,h):
#     if(h*h==b*b+p*p):
#         print("This satisfied the pythagoras theorem ",h*h,"==",b*b+p*p)
#     else:
#         print("Not Satisfied")    
# pythagoram_theo(p,b,h)        
