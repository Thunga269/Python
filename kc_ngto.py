n, X = [int(x) for x in input().split()]
import math
prime = []
a = []
N = 100000
for i in range(N+1):
    a.append(int(0))
def snt():
        for i in range (2, int(math.sqrt(N))+1):
            if(a[i]==0):
                for j in range(2, int(N/i)+1):
                    a[i*j]=1
        for i in range(2, N+1):
            if(a[i]==0):
                prime.append(i)
k = 0
s= str(X) +" "
snt()
m = X
for i in range(n):
    m += prime[k]
    s += str(m)
    s += " "
    k += 1
print(s)