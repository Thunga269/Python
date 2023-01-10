import collections
s = input()
k = int(input())
if len(s)%2!=0: s = s[:len(s)-1]
ds = collections.defaultdict(lambda : 0)
for i in range(0,len(s),2):
    x = int(s[i]+s[i+1])
    cnt = ds[x]
    ds[x] = cnt+1
ds = sorted(ds.items())
ok =0
for x in ds:
    if x[1] >= k:
        print(x[0], x[1])
        ok=1
if ok ==0 : print('NOT FOUND')