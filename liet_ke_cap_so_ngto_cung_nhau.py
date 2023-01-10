t = int(input())
import math
a = [int(x) for x in input().split()]
a.sort()
for i in range(len(a)-1):
    for j in range(i+1, len(a)):
        if math.gcd(a[i], a[j])==1:
            print(str(a[i])+" "+str(a[j]))
            

