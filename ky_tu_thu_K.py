import math

t = int(input())
while t>0:
    t-=1
    n,k = map(int,input().split())
    for i in range(n-1,-1,-1):
        if k%int(math.pow(2,i))==0 :
            print(chr(65+i))
            break