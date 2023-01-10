import math
from pickletools import long4
t = int(input())
def check(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n%i==0:
            return False
        return True
for i in range(t):
    n = input()
    sum = 0
    tich = 1
    dem = 0
    for i in range(len(n)):
        if i%2==0:
            sum += int(n[i])
        else:
            if(n[i]=='0'):
                continue
            else:
                dem = 1
                tich *= int(n[i])
    print(sum, end=" ")
    if dem == 1:
        print(tich)
    else:
        print("0")