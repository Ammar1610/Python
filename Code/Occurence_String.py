a=input("Enter a string:")
l=a.split()
count=0
#for i in range(len(l)):
i=0
while(i<len(l)):
    sub1=l[i]                                                         # hello hello world
    c=l.count(sub1)
    if(l[i]==l[i+1]): 
        i+=1   
    if i==len(l):
        exit()    
    print(sub1,"frequency:",c)
    i+=1
