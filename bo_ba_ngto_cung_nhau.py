L, R = [int(x) for x in input().split()]
import math
for i in range(L, R-1):
    for j in range(i+1, R):
        if math.gcd(i, j)==1:
            for k in range(j+1, R+1):
                if math.gcd(j, k)==1 and math.gcd(i, k)==1:
                    print("("+str(i)+", "+str(j)+", "+str(k)+")")