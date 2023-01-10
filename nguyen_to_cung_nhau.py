t = int(input())
import math
b = input().split()
a = []
for i in b:
    a.append(int(i))
a.sort()
for i in range(len(a)-1):
    for j in range(i+1, len(a)):
        if math.gcd(int(a[i]), int(a[j]))==1:
            print(str(a[i])+" "+str(a[j]))
    
