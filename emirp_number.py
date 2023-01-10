t = int(input())
import math

a = []
prime = []
N = 1000000
# def sang():
#     S = ""
#     for i in range(N+1):
#         a.append(int(0))
#     for i in range(2, int(math.sqrt(N))+1):
#         if a[i]==0:
#             for j in range(2, int(N/i)+1):
#                 a[i*j]=1
#     for i in range(2, N+1):
#         if a[i]==0:
#             prime.append(i)
#     return len(prime)
# l = sang()
# max = max(prime)
def check(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
for i in range(t):
    m = int(input())
    kq = ""
    for i in range(m+1):
        if (check(i)==True and kq.find(str(i))<0):
            n = str(i)
            s = n[::-1]
            if(int(s)<= m and s!=n):
                if(check(int(s))==True):
                    kq += n+" "+s+" "
    print(kq)


    
