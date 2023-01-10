t = int(input())
import math
def snt(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
def check(n):
    sum = int(0)
    if snt(int(n))==False:
        return False
    s = tuple(reversed(n))
    s = ''.join(s)
    if(snt(int(s))==False):
        return False
    for k in n:
        if(k!='2'and k!='3'and k!='5' and k!='7'):
            return False
        else:
            sum += int(k)
    if snt(sum)==False:
        return False
    return True
for i in range(t):
    n = input()
    if check(n)==False:
        print("No")
    else:
        print("Yes")
        

    
