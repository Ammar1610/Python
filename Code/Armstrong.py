num=int(input("Enter a number:"))
x=num
sum=0
power=int(input("Enter number of digits:"))    
while(num!=0):
    dig=num%10
    sum=(dig**power)+sum
    num//=10
if(x==sum):
    print(x,"Is an Armstrong number")
else:
    print(x,"Is not an Armstrong number")    