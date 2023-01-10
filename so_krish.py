t = int(input())
for i in range(t):
    n = input()
    sum = int(0)
    for k in n:
        t = int(k)
        s = int(1)
        for j in range(1, t+1):
            s*=j
        
        sum += s
    if(sum==int(n)):
        print("Yes")
    else:
        print("No")
