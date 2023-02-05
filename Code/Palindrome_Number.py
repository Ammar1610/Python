from math import remainder


num=int(input("Enter a number:"))
rev=0
x=num
while(num!=0):
    dig=num%10
    rev=(rev*10)+dig
    num//=10
print(rev)    
if(x==rev):
    print("Number is Palindrome")
else:
    print("Not Palindrome")   
