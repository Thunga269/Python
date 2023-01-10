import math
t = int(input())
def check(n):
    if(n < 2): return False
    for i in range(2, int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
for i in range(t):
    n = input()
    if len(n)<4:
        print("NO")
    else:
        dau = int(n[:3])
        cuoi = int(n[-3:])
        if check(dau)==True and check(cuoi)==True:
            print("YES")
        else:
            print("NO")