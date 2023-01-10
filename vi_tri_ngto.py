import math
t = int(input())
def  check(so):
    if(so < 2): return False
    for i in range(2, int(math.sqrt(so))+1):
        if so%i==0:
            return False
    return True

def check2(n):
    d=0
    l=0
    for i in range(0, len(n)):
        
        if check(i)==True and check(int(n[i]))==False:
            return False
        if check(i)==False and check(int(n[i]))==True:
            return False
    return True
for i in range(t):
    n = input()
    
    if check2(n):
        print("YES")
    else:
        print("NO")