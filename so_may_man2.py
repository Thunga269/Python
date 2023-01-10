t = int(input())
k = 0
for l in range(t):
    n = input()
    for i in n:
        if(i=='4' or i == '7'):
            k = 1
        else:
            k = 0
            break
    if(k==1):
        print('YES')
    else:
        print('NO')
    