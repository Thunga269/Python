import math
t = int(input())
def check(n):
    s1 = n[0]
    s2 = n[1]
    for i in range(len(n)):
        if(i%2==0 and n[i]!=s1):
            return False
        else:
            if(i%2!=0 and n[i]!=s2):
                return False
    return True
for i in range(t):
    n = input()
    if check(n)==True:
        print("YES")
    else:
        print("NO")