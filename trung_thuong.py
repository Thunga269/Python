t = int(input())
import collections
for i in range(t):
    n = int(input())
    a=collections.defaultdict(int)
    maxi = 0
    for j in range(n):
        x = int(input())
        a[x]+=1
        maxi = max(maxi, a[x])
    # print(sorted(a.items()))
    a = collections.OrderedDict(sorted(a.items()))
    # print(a.items())
    for x,y in a.items():
        if y == maxi :
            print(x)
            break