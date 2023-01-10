import math
from math import sqrt


def uscln(a, b):
    if(b==0):
        return a
    return uscln(b, a%b)

def snt(so):
    if(so<2):
        return 0
    if so == 2:
        return 1
    i = 2
    while(i<=sqrt(so)):
        if so%i==0:
            return 0
        i=i+1
    return 1

t = int(input())
for i in range(t):
    dem = 1
    n = int(input())
    for k in range(2, n):
        if(uscln(k, n) == 1):
            dem = dem+1
    #print(dem)
    if(snt(dem)==1):
        print('YES')
    else:
        print('NO')


