def fibonacci_factorial(num):
    # num=int(input("Enter a number:")) #upto which series to be printed
    x=0
    y=1
    print(x)
    print(y)
    for i in range(2,num):
        sum=x+y
        x=y
        y=sum
        print(sum)
    fact=1    
    for i in range(1,num+1):
        fact*=i
    print("Factorial of",num,":",fact)    
fibonacci_factorial(5)        