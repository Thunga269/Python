import math
t = int(input())
def check(n):
    if len(n)%2==0:
        return False
    if n[0]==n[1]:
        return False
    k = n[0]
    for i in range(0, len(n)-1, 2):
        if n[i]!=k:
            return False
    return True
for i in range(t):
    n = input()
    if check(n)==True:
        print("YES")
    else:
        print("NO")
