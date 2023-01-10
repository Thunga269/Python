import math
t = int(input())
prime = []
a = []
N = 1000000
for i in range(N+1):
    a.append(int(0))
def sang():
    for i in range(2, int(math.sqrt(N))+1):
        if(a[i]==0):
            for j in range(2, int(N/i)+1):
                a[i*j]=1

    for i in range(2, N+1):
        if(a[i]==0):
            prime.append(i)
sang()
# for i in range(10):
#     print(prime[i])
for i in range(t):
    n = int(input())
    j = int(0)
    ss="1 * "
    dem = int(0)
    while(n>1):
        while(n%prime[j]==0):
            n /= prime[j]
            dem+=1
        if dem > 0:
            ss+=str(prime[j]) +"^"+str(dem)
            ss+=" * "
        j+=1
        dem = 0
    ss = ss[:len(ss)-2]
    print(ss)
        
        
