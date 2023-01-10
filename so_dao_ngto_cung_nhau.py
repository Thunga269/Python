t = int(input())
import math
for i in range(t):
    n = input()
    s = n[::-1]
    n = int(n)
    s = int(s)
    if math.gcd(n, s)==1:
        print("YES")
    else:
        print("NO")