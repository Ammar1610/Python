#1
first_name=input("Enter your first name:")
last_name=input("Enter your last name:")
print(last_name ,first_name)

########################################
#2
num=int(input("Enter a number"))
if(num%2==0):
    print("Even")
else:
    print("Odd")    


#########################################
#3
rad=int(input("Enter radius:"))
area=3.14*(rad**2)
print("Area = ",area )    

#########################################
#5
num=int(input("Enter a number:"))
num2=int(input("Enter a number:"))
num3=int(input("Enter a number:"))

sum=num+num2+num3
if(num==num2==num3):
    print(num*3)
else:
    print(sum)    

#########################################
#8
x1=int(input("Enter value of X1:"))
y1=int(input("Enter value of Y1:"))
x2=int(input("Enter value of X2:"))
y2=int(input("Enter value of Y2:"))

distance=(((x2-x1)**2)+((y2-y1)**2))**0.5
print(distance)

#########################################
#7
l=[1,2,3,4,4,4,4,6,7,4]
count=0
for i in l:
    if(i==4):
        count+=1
    else:
        pass
print(count)    

#########################################
#4
num=int(input("Enter a number:"))
diff=((num-17)**2)**0.5
if(num>17):
    print(diff*2) 
else:
    print(diff)    


#########################################

numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,  
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,  
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,  
    958,743, 527] 

for i in numbers:
    if(i==237):
        exit()
    elif(i%2==0):
        print(i)
    else:
        continue    
