def isPrime(n):
    s = str(n)
    if len(s) < 2 : return False
    s1 = s[::-1]
    return s== s1
m,n = map(int,input().split())
matrix = list()
maxi = -199
for i in range(m):
    arr= [int(x) for x in input().split()]
    matrix.append(arr)
    for i in arr:
        if isPrime(i): maxi = max (maxi , i)
if (maxi == -199) : print('NOT FOUND')
else: print(maxi)
for i in range(m):
    for j in range(n):
        if matrix[i][j] == maxi :
            print('Vi tri '+'['+str(i)+']['+str(j)+']')