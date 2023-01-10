t = int(input())
for i in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    d= 0
    a.sort()
    for i in range(n-1):
        r = n-1
        l = i+1
        while(l<r):
            if (a[i]+a[l]+a[r])==0:
                d+=1
                l+=1
            elif (a[i]+a[l]+a[r])<0:
                l+=1
            else:
                r-=1
                

    print(d)