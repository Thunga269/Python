for _ in range(int(input())):
    n = int(input())
    a = [int(x) for x in (input().split())]
    kq = [1]*n
    vt = [-1]
    for i in range(n):
        while len(vt)>1 and a[vt[len(vt)-1]] <= a[i]:
            vt.pop()
        kq[i] = i - vt[len(vt)-1]
        vt += [i]
    print(*kq)

# 100 80 60 70 60 75 85
 