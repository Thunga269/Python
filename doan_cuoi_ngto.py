import math
from re import S
t = int(input())
def check(n):
    if(n < 2): return False
    for i in range(2, int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
for i in range(t):
    n = input()
    if(len(n)<4):
        print("NO")
    else:
        s = n[-4:]
        s = int(s)
            # print(s)
        if check(s)==True:
            print("YES")
        else:
            print("NO")