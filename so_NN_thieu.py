t = int(input())
a = [int(i) for i in input().split()] 
b=[]
a.sort()

ok = 0
res = a[0]
for i in range(res, t+res+1):
    b.append(i)
for i in range(t):
    if(b[i]!=a[i]):
        print(b[i])
        ok = 1
        break
if(ok==0):
    print(a[-1]+1)
