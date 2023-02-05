d={1:5,9:3,4:1,0:7}
d2={}
keys=d.keys()                #output will be in dictionary type
keys2=list(keys)             #changed dict into list (non reversable)       
keys2.sort()
for key in keys2:
    d2.setdefault(key,d[key])  #d[key] = value of that key
print(d2)    