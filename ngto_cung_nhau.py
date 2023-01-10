N, K = [int(x) for x in input().split()]
import math
left = 1
for i in range(1,K+1):
    left *= 10
cnt = 0
for i in range(int(left/10), left):
    
    if math.gcd(i, N)==1:
        print(str(i)+" ", end=" ")
        cnt += 1
        if cnt == 10:
            cnt = 0
            print("")