t = int(input())
import math
def check(n):
    if n < 2: return False
    for i in range(2, int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
for i in range(t):
    a, b = [int(x) for x in input().split()]
    uoc = math.gcd(a, b)
    s = str(uoc)
    sum = 0
    for k in s:
        sum += int(k)
    print(uoc)
    print(sum)
    if check(sum)==True:
        print("YES")
    else:
        print("NO")
