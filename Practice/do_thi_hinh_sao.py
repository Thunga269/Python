# vô hướng, chỉ có 1 đỉnh nối đến tất cả đỉnh còn lại
n, m, ok = int(input()), {}, 1
for i in range(1,n):
    x, y = [int(x) for x in input().split()]
    if x in m: m[x]+=1
    else: m[x]=1
    if y in m: m[y]+=1
    else: m[y]=1
check = False
for i in m.values():
    if i == n-1:
        check = True
        print("Yes")
        break
if not check: print("No")    
