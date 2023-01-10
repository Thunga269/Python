import math
def Euclidean(a, b):
    tong = 0.0
    for i in range(len(a)):
        tong += (a[i]-b[i])**2
    return math.sqrt(tong)
N = int(input())
n = int(input())
a = [float(x) for x in input().split()]
m = -1.0
kq = ''
re = []
for i in range(N-2):
    s = input().split()
    c = float(Euclidean(a, s[1:]))
    m = max(m, c)
    if m == c:
        kq = s[0]
    re.append(c)
    
print(kq, re)