t = int(input())
import math
def chuyen(n):
    so = 0
    for i in range(len(n)):
        so = so+int(n[i])*(2**(len(n)-1-i))
    return int(so)
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
    if(b==2):
        print(n)
    else:
        so = chuyen(n)
        if b==4:
            kq = check2(int(so), int(b))
            print(kq)
        if b==8: print(oct(so)[2:])
        if b==16: print(hex(so)[2:].upper())
        

