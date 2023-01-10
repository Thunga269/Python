t = int(input())
for i in range(t):
    N = int(input())
    sum = 0.000000
    if N%2!=0:
        for i in range(1, N+1, 2):
            sum += 1/i
            
    else:
        for i in range(2, N+1, 2):
            sum += 1/i
    print("%.6f" % sum)