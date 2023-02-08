#1
L=[]
n=int(input("Enter number of elements:"))
for i in range(0,n):
    ele=eval(input("Enter element:",))
    L.append(ele)
print(max(L))    

##################################################3
#2

L=[]
n=int(input("Enter number of elements:"))
for i in range(0,n):
    ele=eval(input("Enter element:",))
    L.append(ele)
find=eval(input("Enter number to search:"))
print(L.count(find))


####################################################
#Dictionary

#1
d={}
n=int(input("Enter number of elements:"))
for i in range(0,n):
    key=int(input("Enter roll:"))
    val=input("Enter name:")
    d.setdefault(key,val)
print(d)    

#####################################################
#2
d={}
n=int(input("Enter number of elements:"))
for i in range(0,n):
    key=int(input("Enter roll:"))
    val=input("Enter name:")
    d.setdefault(key,val)
find=int(input("Enter key to search:")) 
if find in list(d.keys()):
    print(d[find])
else:
    print("Key not present")       

#####################################################
#3
n=int(input("Enter a number:"))
d={}
for i in range(1,11):
    d.setdefault(i,i*n)
print(d)    

