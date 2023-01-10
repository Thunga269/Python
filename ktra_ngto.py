import math
t = int(input())
for i in range(t):
    n = input()
    s = n[-4:]
    s = s.lstrip()
    # if(len(s)==0): s = "0"
    so = int(s)
    # print(so)
    ok = 0
    if(so==0 or so==1): print("NO")
    else:

        for i in range(2, int(math.sqrt(so))+1):
            if so%i==0:
                ok = 1
                print("NO")
                break

        if ok == 0:
            print("YES")
    def snt():
        for i in range (2, int(math.sqrt(N))+1):
            if(a[i]==0):
                for j in range(2, int(N/i)+1):
                    a[i*j]=1
        for i in range(2, N+1):
            if(a[i]==0):
                prime.append(i)
        return len(prime)