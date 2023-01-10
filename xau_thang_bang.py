import math
t = int(input())
def check(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n%i==0:
            return False
        return True
for i in range(t):
    n = input()
    s = n[::-1]
    ok = 0
    for i in range(len(n)-1):
        sub1 = abs(ord(n[i])-ord(n[i+1]))
        sub2 = abs(ord(s[i])-ord(s[i+1]))
        if str(sub1) != str(sub2):
            ok = 1
    if ok == 0:
        print("YES")
    else:
        print("NO")