import collections
s = input()
if len(s)%2!=0: s = s[:len(s)-1]
ds = collections.defaultdict(lambda : 0)
for i in range(0,len(s),2):
    x = int(s[i]+s[i+1])
    cnt = ds[x]
    ds[x] = cnt+1
for x,y in ds.items():
    print(x,y)