from collections import Counter
# creating two files and writing in them
a=open('file1.txt','w')
a.write("Hello\n I \n am \n new coder, Hello")
b=open('file2.txt','w')
b.write("World World is old")
a.close()
b.close()

# reading the content of both files
a=open('file1.txt','r')
print(a.read())
b=open('file2.txt','r')
print(b.read())

# Counting no. of lines
a.seek(0)       #cursor at start coz cursor went to end after reading whole file in above line.
line=a.readlines()  #line will be a list
count=len(line)
print(line)
print(count)

b.seek(0)
line2=b.readlines()
count2=len(line2)
print(line2)
print(count2)

#frequency of each word in both files
print("Frequency of each word in file1 and file2:")
#a.read().split()
a.seek(0)
f=Counter(a.read().split())
print(f)
print("Most common word in file1:")
print(f.most_common(1))
#b.read().split()
b.seek(0)
f2=Counter(b.read().split())
print(f2)
print("Most common word in file2:")
print(f2.most_common(1))

#creating new file and adding content of file1 and file2 in it

a.seek(0)
b.seek(0)
x=a.read()
y=b.read()
z=x+y
c=open('file3.txt','w')
c.write(z)
c.close()
c=open('file3.txt','r')
print(c.read())
c.close()



