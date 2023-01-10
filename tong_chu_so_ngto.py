import math
t = int(input())
def check(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True
for i in range(t):
    n = input()
    sum = 0
    for i in n:
        sum += int(i)
    if check(sum)==True:
        print("YES")
    else:
        print("NO")