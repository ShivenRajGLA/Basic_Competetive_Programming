s=input("Enter a String : ")
length=len(s)
count = 0
for i in range(length):              
    for j in range(i, length):       
        sub = s[i:j+1]           
        if sub == sub[::-1]:     
            count += 1
print(count)
