d={1:5,9:3,4:1,0:5}
d2={}
key=list(d.keys())
val=list(d.values())
set=set(val)
print(set)
for i in set:
    for j in key:
        d2.setdefault(j,d[j])