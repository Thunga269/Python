t = int(input())
for i in range(t):
    n = int(input())
    a = [int(i) for i in input().split()] 
    b = [int(i) for i in input().split()] 
    a.sort()
    b.sort()
    ok = 1
    for i in range(n):
        if(a[i]>b[i]):
            ok = 0
            print("NO")
            break
    if(ok == 1):
        print("YES")
   