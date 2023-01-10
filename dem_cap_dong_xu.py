t = int(input())
a =list()
cnt = 0
def ToHop(n):
    def GiaiThua(k):
        sum =1
        for i in range(1,k+1): sum*=i
        return sum
    return int(GiaiThua(n)/GiaiThua(n-2)/2)
for i in range(t):
    s = input()
    if(s.count('C'))>=2:
        cnt += ToHop(s.count('C'))
    a.append(s)

for i in range(t):
    d=0
    for j in range(t):
        if a[j][i]=='C': d+=1
    if d >= 2:
        cnt += ToHop(d)
print(cnt)

