n = int(input())
t = n
arr = list()
while t>0:
    a = [int(x) for x in input().split()]
    t -= len(a)
    arr += a
arr = list(set(arr))
arr.sort()
ok = 0
maxi = max(arr)
for i in range(1,maxi):
    if i not in arr:
        print(i)
        ok= 1;
if ok ==0 : print('Excellent!')