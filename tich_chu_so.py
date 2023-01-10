import math
t = int(input())
for i in range(t):
    n = input()
    sum = 1
    for i in n:
        if i == '0':
            continue
        
        sum *= int(i)
    print(sum)
