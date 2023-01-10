if __name__ == '__main__':
    n = int(input())
    t =n
    arr=[]
    while t>0:
        t-=1
        a =[int(x) for x in input().split()]
        arr.append(a)
    k= int(input())
    sum1 =0 ; sum2=0;
    for i in range(n):
        for j in range(n):
            if i>j:
                sum1 += arr[i][j]
            if j>i:
                sum2+= arr[i][j]
    sum = abs(sum1-sum2)
    print('YES') if sum <=k else print('NO')
    print(sum)
