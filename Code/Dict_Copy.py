d= dict([('a',12),('c',16),('d',7)])
d.setdefault('e',44)
e1 =d.copy()
if(d==e1):
    print("yes")

print(e1)

