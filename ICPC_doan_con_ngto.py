from cmath import sqrt

import math
s = input()
P = input()
s = s.split(" ")
L = int(s[0])
H = int(s[1])
prime =[]
a = []
N = int(1300000)
prime.append(0)
for i in range(0, N+1):
    a.append(int(0))
def snt():
    for i in range (2, int(math.sqrt(N))+1):
        if(a[i]==0):
            for j in range(2, int(N/i)+1):
                a[i*j]=1
    for i in range(2, N+1):
        if(a[i]==0):
            prime.append(i)
    return len(prime)

leng = snt()
print(leng)

dem = int(0)
for i in range (L, H+1):
    s1 = str(prime[i])
    if(P in s1):
        #print(s1)
        dem += 1
print(dem)

        


