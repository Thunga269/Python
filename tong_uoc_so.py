
import math
N = 2000000
a = []
def check():
    for i in range(N+1):
        a.append(0)
    for i in range(2,int(math.sqrt(N))+1):
        if(a[i]==0):
            
            for j in range(2,int(N/i)):
                a[j*i]=i
                # j+=i
    j = 0
    for i in range(2, N+1):
        if(a[i]==0):
            a[i]=i
check()
b = []
t = int(input())
sum = 0
for i in range(t):
    n = int(input()) 
    while(n!=1):
        
        sum += int(a[n])
        n = int(n/a[n])
print(int(sum))
