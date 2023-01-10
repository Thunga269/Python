import math

base = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
t = int(input())
while t>0:
    t-=1
    n,factor = map(int,input().split())
    size = int(math.log(n,factor))+1
    res =''
    for i in range(size-1,-1,-1):
        if n>= math.pow(factor,i):
            mod = int(n/math.pow(factor,i))
            res += str(base[mod])
            n -= mod*int(math.pow(factor,i))
        else:
            res += '0'
    print(res)