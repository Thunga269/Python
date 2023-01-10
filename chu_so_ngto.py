import math
def check(n):
    n = int(n)
    for i in range(2, int(math.sqrt(n))+1):
        if n%i==0:
            return False
        return True
def check2(n):
    dem = int(0)
    for i in n:
        if i=='2'or i=='3' or i=='5'or i=='7':
            dem+=1
    if(dem>(len(n)-dem)): 
        return True
    else: 
        return False
t = int(input())
for i in range(t):
    n = input()
    l = int(len(n))
    if check(l)== True and check2(n)==True:
        print("YES")
    else:
        print("NO")

