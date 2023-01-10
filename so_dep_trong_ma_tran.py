
m,n = map(int,input().split())
matrix = list()
maxi = -199
mini = 99999999999
for i in range(m):
    arr= [int(x) for x in input().split()]
    matrix.append(arr)
    maxi = max(maxi , max(arr))
    mini = min(mini, min(arr))
lucky = maxi - mini
ok = 0
for i in matrix:
    if lucky in i:
        ok =1
        break
if ok ==0 : print('NOT FOUND')
else : print(lucky)
for i in range(m):
    for j in range(n):
        if matrix[i][j] == lucky:
            print('Vi tri '+'['+str(i)+']['+str(j)+']')