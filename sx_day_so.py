if __name__ =='__main__':
    t = int(input())
    while t>0:
        t-=1
        n,m= map(int,input().split())
        arr = [int(x) for x in input().split()]
        res = list()
        ok=0
        for i in range(n):
            if arr[i] <0 :res.append(arr[i])
        maxi = max(arr)
        for i in range(n):
            if arr[i]>=0:
                if arr[i] == maxi and ok ==0:
                    ok=1
                    res.append(m)
                res.append(arr[i])
        res =[str(x) for x in res]
        print(' '.join(res))