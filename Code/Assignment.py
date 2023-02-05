#Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string.
l=input("Enter a string:")
print(l)                          ##########################################################
l.pop(0,2)
print(l)
l.pop()
l.pop()
print(l)

#Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
s=input("enter a string:")
first = s[0]                              ###########################################################
for i in range(0,len(s)):
    if(s[i]==first):
        s.replace(s[i],'$')
        print(s[i])
    else:
        continue    
print(s)    

#Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. 
# If the string length of the given string is less than 3,leave it unchanged.

s=input("Enter a string:")
if(len(s)>2):
    if(s.endswith('ing')):
        s+='ly'
    else:
        s+='ing'
else:
    print(s)
print(s)    

# Write a Python program to get the largest number from a list
l=[2,30,1,23,234,1,34,59]
print(max(l))

#Write a Python program to multiplies all the items in a list.
l=[2,30,1,23,234,1,34,59]
mult=1
for i in l:
    mult*=i
print(mult)    

#Write a Python program to get the second largest number from a list.
l=[2,30,1,23,234,1,34,59]
maximum=max(l)
l.remove(maximum)
second_max=max(l)
print(second_max)

#Write a program to remove all the duplicate elements from list.
l=[2,30,1,23,234,1,34,59]
s=set(l)
l2=list(s)
print(l2)

#Write a Python program to count the number of strings where the string length is 4 or more and the first and last character are same from
# a given list of strings.
l=['hello','good','morning','olo','hi','ola']
count=0
for i in l:
    if(len(i)>3):
        count+=1
    elif(i[0]==i[-1]):
        count+=1    
    else:
        continue
print(count)    


#Write a Python program to find common items from two lists.
l=[1,2,3,4]
l2=[4,5,6,7,8]
s=set(l)
s2=set(l2)
print(list(s.intersection(s2)))