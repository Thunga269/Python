import math
a,k,n = [int(a) for a in input().split()]
i = int(a/k) + 1
sum = a
if i*k > n : print(-1)
while i*k<=n:
    print(i*k-a,end=' ')
    i=i+1

# 10/6 = 1
# i = 2
# 2*6 <= 40
# 12-10 = 2
# 3*6=18
# 18-10=8
# 4*6=24
