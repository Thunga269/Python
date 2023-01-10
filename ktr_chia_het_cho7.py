import math
t = int(input())
for i in range(t):
    n = input()
    cnt = 0
    sum = int(n)
    while(True):
        if cnt == 1000 and sum %7!=0:
            print("-1")
            break
        if sum %7==0:
            print(sum)
            break
        cnt+=1
        s = n[::-1]
        sum += int(s)
        n = str(sum)
