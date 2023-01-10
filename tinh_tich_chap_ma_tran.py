t = int(input())
for k in range(t):
    N, M = [int(x) for x in input().split()]
    a = []
    p=[]
    b = []
    for j in range(N):
        p = [int(x) for x in input().split()]
        a.append(p)
    for j in range(3):
        p = [int(x) for x in input().split()]
        b.append(p)
    s = 0
    
    for i in range(2, N) :
        for j in range(2, M) :
            s += a[i-2][j-2] * b[0][0]
            s += a[i-2][j-1] * b[0][1]
            s += a[i-2][j] * b[0][2]

            s += a[i - 1][j - 2] * b[1][0]
            s += a[i - 1][j - 1] * b[1][1]
            s += a[i - 1][j] * b[1][2]

            s += a[i][j - 2] * b[2][0]
            s += a[i][j - 1] * b[2][1]
            s += a[i][j] * b[2][2]
    print(s)

    
