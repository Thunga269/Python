from itertools import combinations
def check(s):
    com = combinations(range(s),2)
    return len(list(com))
t = int(input())
dem, a = 0, []
for i in range(t):
    s = input()
    a.append(s)
    c = s.count('C')
    dem += check(c)

for i in range(t):
    k = 0
    for j in range(t):
        if a[j][i]=='C':
            k += 1
    dem += check(k)
print(dem)

