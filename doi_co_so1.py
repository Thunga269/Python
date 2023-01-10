t = int(input())
import math
def chuyen(n):
    so = 0
    for i in range(len(n)):
        if n[len(n)-1-i]=='1':
            so += math.pow(2,i)
    return so
def check2(n, b):
    du = n%b
    kq = ""
    while(n>0):
        kq = str(du)+kq
        n //= b
        du = n%b
    return kq
for i in range(t):
    b = int(input())
    n = input()
    so = chuyen(n)
    kq = check2(int(so), int(b))
    print(kq)
