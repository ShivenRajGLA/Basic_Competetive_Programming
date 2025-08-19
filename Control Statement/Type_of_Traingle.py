angle1=int(input("Enter first Angle :"))
angle2=int(input("Enter Second Angle :"))
angle3=int(input("Enter Third Angle :"))
sum_of_Angle=angle1+angle2+angle3
if(angle1==90 or angle2==90 or angle3==90):
    print("This is Right Angle Triangle ")
elif(angle1 or angle2 or angle3>90):
    print("This is Obtuse Triangle")
else:
    print("This is Acute Angle ")        
