import math
t = int(input())
def  check(so):
    for i in range(2, int(math.sqrt(so))+1):
        if so%i==0:
            return False
    return True
def check1(n):

    for i in range(len(n)):
        if i%2!=0 and int(n[i])%2==0:
            return False
        if i%2==0 and int(n[i])%2!=0:
            return False
    return True
for i in range(t):
    n = input()
    sum = 0
    if check1(n) ==True:
        for k in n:
            sum += int(k)
        if check(sum):
            print("YES")
    else:
        print("NO")