t = int(input())
a = []
prime = []
N = 1000000
import math
for i in range(N+1):
    a.append(0)
def sang():
    for i in range(2, int(math.sqrt(N))+1):
        if(a[i]==0):
            for j in range(2, int(N/i)+1):
                a[i*j]=1
sang()
for i in range(t):
    n = int(input())
    d = 0
    for i in range(2, n-6):
        
        if((a[i]==0 and a[i+6]==0) and (a[i+2]==0 or a[i+4]==0)):
            # print(i)
            d+=1
    print(d)

