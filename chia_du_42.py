t = 10
a=set()
while t>0:
    b = [int(x)%42 for x in input().split()]
    for x in b:
        a.add(x)
    t-=len(b)
print(len(a)) 
