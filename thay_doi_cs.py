import math
t = int(input())
def check(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n%i==0:
            return False
        return True
def Min(x1, p, q):
    x1_min= x1.replace(p, q)
    x1_max= x1.replace(q, p)
    return x1_min, x1_max
    

for i in range(t):
    
    p, q = [int(x) for x in input().split()]
    l = input().split()
    if(len(l) == 2):
        x1 = l[0]
        x2 = l[1]
    else:
        x1 = l[0]
        x2 = input()
    p1=str(max(p, q))
    p2=str(min(p, q))
    
    x1_min, x1_max=Min(x1, p1, p2)
    x2_min, x2_max=Min(x2, p1, p2)
    # print(x1_min + " "+x1_max)
    # print(x2_min + " "+x2_max)
    print(int(x1_min)+int(x2_min), end=" ")
    print(int(x1_max)+int(x2_max))
    
    