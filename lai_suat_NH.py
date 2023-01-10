from tokenize import Double


t = int(input())
import math
for i in range(t):
    
    N, X, M = [float(x) for x in input().split()]
    # lai = Double (N)
    
    a = 1+X/100
    kq = math.log(M/N, a) #loga co so a cua b
    if(int(kq) <kq):

        print(int(kq)+1)
    else:
        print(kq)

