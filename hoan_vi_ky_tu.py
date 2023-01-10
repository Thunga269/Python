
def hoan_vi(p, n):
    # a = []
    # a.append(0)
    # for i in range(1, n+1):
    #     a.append(chr(i-1+ord('X')))
    a = p
    while(1):
        for i in range(1, n+1):
            print((a[i]), end="")
        print()
        j = n-1
        while(j>0 and a[j]>a[j+1]): j-=1
        if j==0: return
        k = n
        while(a[k]<a[j]): k-=1
        tmp = a[k]
        a[k] = a[j]
        a[j] = tmp
        # numpy.sort(a[j+1:])
        for m in range(j+1, n):
            for h in range(m+1, n+1):
                if a[m]>a[h]:
                    tmp = a[m]
                    a[m] = a[h]
                    a[h] = tmp
n = input()
p = []
p.append('0')
for i in n:
    p.append(i)
hoan_vi(p, len(p)-1)
