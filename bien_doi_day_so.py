import math
while True:
    a = [int(x) for x in input().split()]
    if a[0]==a[1] and a[1]==0 and a[2]==0 and a[3]==0:
        break
    d=0
    while True:
        
        if a[0]==a[1] and a[1]==a[2] and a[2]==a[3]:
            break
        a1 = list(a)
        # print(a1)
        # print(a)
        a[3]=abs(a1[3]-a1[0])
        for i in range (3):
            a[i]=int(abs(a1[i]-a1[i+1]))
        
        d+=1
        
    print(d)