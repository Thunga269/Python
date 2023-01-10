t = int(input())
import math
def nto(n):
    if n<2: return 0
    for i in range(2, int(math.sqrt(n)) + 1) :
        if n % i == 0 : return 0
    return 1
a = [int(x) for x in input().split()]
b ={}
for i in a:
    b[i]=1
b = list(b)
m = len(b)
#tổng từ (0-> b[i]): snt; tổng còn lại cũng là snt
for i in range(1, m): b[i]+=b[i-1] #vị trí thứ i có tổng là b[i]
ok = 0
for i in range(m) :
    if nto(b[i]) and nto(b[m - 1] - b[i]) :
        ok = 1
        print(i)
        break
if ok == 0 : print("NOT FOUND")