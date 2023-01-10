import collections
n,k= map(int,input().split())
arr=[int(x) for x in input().split()]
ds = collections.defaultdict(lambda : 0)
for i in arr:
     x = ds[i]
     ds[i] = x+1
ds = sorted(ds.items(),key=lambda kv:(kv[1],kv[0]),reverse=True)
if ds[0][1] == ds[len(ds)-1][1]:
    print('NONE')
else:
    maxi = ds[0][1]
    for i in ds:
        if i[1] != maxi:
            print(i[0])
            break